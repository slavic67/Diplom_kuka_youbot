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
        temp=find_all_object(img)
        print(temp)
        if temp !=[]:
            return_list=temp
        end=time.time()

        cv2.putText(img, "{} fps".format(round(1/(end-start),2)), (20,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0, 255), 2)


        cv2.imshow("Image", img)
        cv2.waitKey(1)


def start_server(HOST):
    global return_list
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(HOST)
    server.listen()
    weight = 640
    height = 480
    # if aspect ratio 16:9
    weight_diapason = 16 * 9.25
    height_diapason = 9 * 9.25
    # if aspect ratio 4:3
    #weight_diapason = 4 * 34
    #height_diapason = 3 * 34


    while True:
        conn,addr=server.accept()
        print('Connected from -',addr)
        delta_angle=[(return_list[0][0]-weight//2)/weight*weight_diapason,(return_list[0][1]-height//2)/height*height_diapason]
        return_list=[[weight//2,height//2]]
        resp=pickle.dumps(delta_angle)
        conn.send(resp)
        conn.close()



if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    HOST = (socket.gethostname(), 10000)
    return_list = []


    thread1=threading.Thread(target=tracking_object)
    thread1.start()
    thread2=threading.Thread(target=start_server,kwargs={'HOST':HOST})
    thread2.start()

