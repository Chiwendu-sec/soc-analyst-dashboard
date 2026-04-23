import socket
from concurrent.futures import ThreadPoolExecutor

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389]

risk_ports = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    135: "RPC",
    139: "NETBIOS",
    445: "SMB",
    3389: "RDP"
}

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))
    sock.close()

    if result == 0:
        return {
            "port": port,
            "service": risk_ports.get(port, "Unknown"),
            "status": "OPEN",
            "risk": "HIGH" if port in risk_ports else "LOW"
        }

    return None


def scan_target(target):
    results = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(scan_port, target, p) for p in ports]

        for f in futures:
            r = f.result()
            if r:
                results.append(r)

    return results