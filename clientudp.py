import socket
import time
import settime
from datetime import datetime

UDP_IP = "10.0.0.83"
UDP_PORT = 5005
rtt_array=[]
TIMEZONE = 3


#calcula rtt
for i in range(0,5):
    ts1 = time.time()
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(('TS:'+str(ts1)).encode(), (UDP_IP, UDP_PORT))

    #aguarda recebimento
    datarcv, server = sock.recvfrom(1024)
    message_from_server = str(datarcv.decode())
    ts4 = time.time()
    ts_array = message_from_server.split('|')
    ts1 = float(ts_array[0])
    ts2 = float(ts_array[1])
    ts3 = float(ts_array[2])
    rtt = ((ts4-ts1)-(ts3-ts2))/2
    print('rtt calculada:',rtt)
    rtt_array.append(rtt)

#pede horario do servidor
sock.sendto('TIME'.encode(), (UDP_IP, UDP_PORT))

rtt_med = (sum(rtt_array)/5.0)
print('RTT média:',rtt_med)
#aguarda recebimento
datarcv, server = sock.recvfrom(1024)
ts_from_server = float(datarcv.decode()) + (TIMEZONE * 3600) + rtt_med
date = datetime.fromtimestamp(ts_from_server)
time_tuple = (date.year,  # Year
            date.month,  # Month
            date.day,  # Day
            date.hour,  # Hour
            date.minute,  # Minute
            date.second,  # Second
            0,  # Millisecond
            )

settime.set_time(time_tuple)
