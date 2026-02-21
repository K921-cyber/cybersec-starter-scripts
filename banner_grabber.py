# banner_grabber.py
import socket
import threading
from queue import Queue

# A common list of ports to scan
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
lock = threading.Lock()
q = Queue()

def port_scan(port):
    """
    Scans a single port and tries to grab a banner.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # Returns 0 if port is open
        if result == 0:
            banner = ""
            try:
                # Send some data to provoke a response
                s.send(b'Hello\r\n')
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Could not grab banner"
            
            with lock:
                print(f"[+] Port {port} is open - Service: {banner}")
        s.close()
    except Exception as e:
        pass

def worker():
    """Worker thread to pull ports from the queue and scan them."""
    while not q.empty():
        port = q.get()
        port_scan(port)
        q.task_done()

if __name__ == "__main__":
    target = input("Enter target IP address: ")
    print(f"\nScanning {target}...\n")

    # Add ports to the queue
    for port in COMMON_PORTS:
        q.put(port)

    # Create and start threads
    for _ in range(30): # 30 threads for faster scanning
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
    
    q.join() # Wait for the queue to be empty

    print("\nScan complete.")




