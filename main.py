import cv2
import time
from neural_network_yolo import find_all_object


cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    img = cv2.resize(img, (640, 480))
    img = cv2.flip(img, 1)

    start=time.time()
    return_list=find_all_object(img)
    end=time.time()

    cv2.putText(img, "{} fps".format(round(1/(end-start),2)), (20,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0, 255), 2)
    if return_list!=[]:
        print(return_list[0])

    cv2.imshow("Image", img)
    cv2.waitKey(1)