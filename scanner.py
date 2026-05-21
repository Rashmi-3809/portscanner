import socket
import threading

target = input("Enter Target IP: ")
print("\n=== Advanced Port Scanner Started ===\n")

open_ports = []

# Function to scan port
def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

            try:
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    └─ Service: {banner}")
                else:
                    print("    └─ Service: Unknown")
            except:
                print("    └─ Service: Not detected")

            open_ports.append(port)

        s.close()

    except:
        pass


# Threading for speed
for port in range(1, 500):
    t = threading.Thread(target=scan, args=(port,))
    t.start()


print("\n=== Scan Completed ===")
