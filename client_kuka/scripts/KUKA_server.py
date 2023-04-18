#!/usr/bin/env python

from __future__ import print_function

from kuka.srv import AngleValues,AngleValuesResponse
import rospy
import socket
import numpy as np 
import time

def handle_exchange_values(req):
    try:
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(HOST)
        resp=client.recv(4096)
        msg=resp.decode('utf-8').split()
        msg[0]=float(msg[0])
        msg[1]=float(msg[1])
        delta_A4,delta_A5=msg[0]*np.pi/180,msg[1]*np.pi/180
        print(delta_A4,delta_A5)

        return AngleValuesResponse(A4_new=req.A4+delta_A4,A5_new=req.A5+delta_A5)
    except Exception as e:
        print(e)
        return AngleValuesResponse(A4_new=req.A4,A5_new=req.A5)

    

def KUKA_server():
    rospy.init_node('Server_for_kuka_arm')
    s = rospy.Service('kuka_arm', AngleValues, handle_exchange_values)
    print("The server has been started")
    rospy.spin()

if __name__ == "__main__":
    HOST=(socket.gethostname(),10000) 
    KUKA_server()
