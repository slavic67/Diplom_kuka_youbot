import socket
import pickle

HOST=(socket.gethostname(),10000)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(HOST)
s.listen()
print("i'm listenning your connections")

d= [[10,10],[15,15]]

while True:
    conn,addr=s.accept()
    print('Connected from -',addr)
    resp=pickle.dumps(d)
    conn.send(resp)
    conn.close()