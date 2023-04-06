import cv2
import time
from neural_network_yolo import find_all_object
import threading
import pickle
import socket



def tracking_object():
    global return_list
    while True:
        _, img = cap.read()
        img = cv2.resize(img, (640, 480))
        img = cv2.flip(img, 1)

        start=time.time()
        return_list=find_all_object(img)
        end=time.time()

        cv2.putText(img, "{} fps".format(round(1/(end-start),2)), (20,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0, 255), 2)
        #if return_list!=[]:
           # print(return_list[0])

        cv2.imshow("Image", img)
        cv2.waitKey(1)


def start_server(HOST):
    global return_list
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(HOST)
    server.listen()
    while True:
        conn,addr=server.accept()
        print('Connected from -',addr)
        resp=pickle.dumps(return_list)
        conn.send(resp)
        print(return_list)
        conn.close()


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    HOST = (socket.gethostname(), 10000)
    return_list = []

    thread1=threading.Thread(target=tracking_object)
    thread1.start()
    thread2=threading.Thread(target=start_server,kwargs={'HOST':HOST})
    thread2.start()

    while True:
        print(return_list)
        time.sleep(0.1)