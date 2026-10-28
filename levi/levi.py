import argparse
import socket
import sys
from datetime import datetime

DEFAULT_PORTS = "1-1024"
DEFAULT_TIMEOUT = 0.5  # second

def parse_args():
    parser = argparse.ArgumentParser(prog="levi")
    parser.add_argument("target",help="Scanned IP (ex. 127.0.0.1)")
    parser.add_argument("-p", "--ports",default=DEFAULT_PORTS,help=f"Ports: 80 | 22,80,443 | 1-1024 (default: {DEFAULT_PORTS})")
    parser.add_argument("-t", "--timeout",type=float,default=DEFAULT_TIMEOUT,help=f"Waiting time per port, second (default: {DEFAULT_TIMEOUT})")
    return parser.parse_args()

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] '{target}' could not be resolved. Control the address.")
        sys.exit(1)

def parse_ports(port_str):
    ports = []
    try:
        for part in port_str.split(","):
            part = part.strip()
            if not part: # if its empty
                continue

            if "-" in part: # port interval
                start, end = part.split("-", 1)
                start, end = int(start), int(end)
                if start > end:
                    raise ValueError
                ports.extend(range(start, end + 1))

            else:
                ports.append(int(part)) # single port

    except ValueError:
        print(f"[!] Invalid port expression: '{port_str}'")
        sys.exit(1)

    for port in ports: # check that every port is in the valid range 
        if not 1 <= port <= 65535:
            print(f"[!] Port has to be between 1-65535: {port}")
            sys.exit(1)

    if not ports: # if the list is empty
        print("[!] No ports to scan.")
        sys.exit(1)

    return sorted(set(ports))  # delete the repetations and sort (default is from smaller value >> bigger)


def scan_port(ip, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # tries to connect a tcp connection to given ip's specified port
            # when a socket is opened using "with" (also its called as context manager in net) it close socket after the block is ended anyway
            sock.settimeout(timeout) # if no answer arrive wait for 'timeout' unit
            return sock.connect_ex((ip, port)) == 0 # starts the 3-way handshake; returns 0 on success, otherwise an error code (111 on Linux, 61 on macOS)
    except OSError: # if a network error occur, then the program doesn't crash. It assumes that port is closed and continue
        return False

def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp") # takes a port number and returns the name of the service usually assigned to that port by looking it up in a local list /etc/services.
    except OSError:
        return "unknown"

def print_banner(target, ip, ports):
    print("=" * 50)
    print("  levi — port scanner")
    print("=" * 50)
    print(f"  Target           : {target}")
    print(f"  IP               : {ip}")
    print(f"  Port Number      : {len(ports)}")
    print(f"  Initialization   : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("-" * 50)

def print_summary(open_ports, start_time):
    duration = datetime.now() - start_time
    print("-" * 50)

    if open_ports:
        port_list = ", ".join(str(p) for p in open_ports) # concatinate port numbers >> string list
        print(f"[x] {len(open_ports)} Open port detected: {port_list}")
    else:
        print("[-] No open ports detected.")
    print(f"[i] Duration: {duration.total_seconds():.2f} sec")

def main():
    args = parse_args() # listen the cli.

    ip = resolve_target(args.target) # turns name into ip.
    ports = parse_ports(args.ports) # turns port string into a list

    print_banner(args.target, ip, ports)
    start_time = datetime.now()

    open_ports = []
    for port in ports:
        if scan_port(ip, port, args.timeout):
            service = get_service_name(port)
            print(f"[+] {port:>5}/tcp  open   {service}")
            open_ports.append(port)

    print_summary(open_ports, start_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by the user.")
        sys.exit(0)