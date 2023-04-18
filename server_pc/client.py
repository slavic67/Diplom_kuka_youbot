import socket
import numpy as np

HOST=(socket.gethostname(),10000)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(HOST)
resp=client.recv(4096)
msg=resp.decode('utf-8').split()
msg[0]=float(msg[0])
msg[1]=float(msg[1])
delta_A4,delta_A5=msg[0]*np.pi/180,msg[1]*np.pi/180
print(delta_A4,delta_A5)