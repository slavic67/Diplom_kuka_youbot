import socket
import pickle

HOST=(socket.gethostname(),10000)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(HOST)
print('Connected to',HOST)

resp=client.recv(4096)
a=pickle.loads(resp)
print(pickle.loads(resp))
