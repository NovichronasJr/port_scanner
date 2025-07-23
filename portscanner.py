import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
    try:
        host = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Could not resolve hostname.")
        sys.exit(1)
else:
    print("Usage: python script.py <hostname>")
    sys.exit(1)

# Print scanning info
print("=" * 50)
print(f"Scanning Target :: {host}")
print(f"Scan started at :: {datetime.now()}")
print("=" * 50)

# Try scanning ports
try:
    for port in range(1, 65536):  # 65536 not 65535 to include port 65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit(0)
except socket.error:
    print("Couldn't connect to server.")
    sys.exit(1)
