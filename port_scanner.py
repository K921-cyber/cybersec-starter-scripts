# port_scanner.py

import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389]

def scan_ports(host, ports):
    """Scan specified ports on a host."""
    print(f"🔍 Scanning {host}...")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"❌ Port {port} is closed")
        sock.close()
    return open_ports

if __name__ == "__main__":
    target = input("Enter target hostname or IP: ")

    scan_ports(target, COMMON_PORTS)







