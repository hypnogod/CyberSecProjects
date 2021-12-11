import socket
import sys
from datetime import datetime
from pyfiglet import figlet_format
import threading
from queue import Queue

print_lock = threading.Lock()

print(figlet_format("PORT SCANNER"))

# get the host
x = str(input("Enter your target IP address or URL here: "))
try:
    target = socket.gethostbyname(x)
except (UnboundLocalError, socket.gaierror):
    print("\nInvalid format. Please use a correct IP or web address\n")
    sys.exit()

# Diffrent section
print("-" * 60)
print("Scanning Target: " + str(target))
print("Scanning started at: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
print("-" * 60)

# set up socket
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conx = s.connect((target, port))
        with print_lock:
            print("port:",port,"is open!")
        conx.close()
    except (ConnectionRefusedError, AttributeError, OSError):
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(200):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()

for worker in range(1,65536):
    q.put(worker)

# wait until the thread terminates.
q.join()
