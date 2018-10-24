import socket
import time

UDP_IP = "10.0.0.67"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    message_received = str(data.decode())
    ts2 = time.time()
    if(message_received.startswith('TS:')):
        ts1 = float(message_received[3:])
        ts3 = time.time()
        message_to_send = '|'.join([str(ts1),str(ts2),str(ts3)])
        print("received ttl request:", str(data.decode()))
    else:
        print("received time request")
        message_to_send = str(time.time())
    sock.sendto(message_to_send.encode(), addr)
