import socket
from datetime import datetime

# Common ports and their associated services
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}


def scan_target(target, ports):
    """
    Scans a target IP address for open ports.
    """

    print(f"\nScanning target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    for port in ports:

        # Create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout so scan is faster
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        # If connection succeeds, port is open
        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"Port {port} OPEN ({service})")
            open_ports.append(port)

        sock.close()

    if not open_ports:
        print("No open ports found.")

    print("-" * 50)
    print("Scan finished.")


if __name__ == "__main__":

    target = input("Enter target IP: ")

    ports = list(COMMON_SERVICES.keys())

    scan_target(target, ports)