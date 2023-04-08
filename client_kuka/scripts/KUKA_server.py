#!/usr/bin/env python

from __future__ import print_function

from kuka.srv import AngleValues,AngleValuesResponse
import rospy

def handle_exchange_values(req):
    print("Returning [%s + %s = %s]"%(req.A4, req.A5, (req.A4 + req.A5)))
    return AngleValuesResponse(A4_new=req.A4+1.04,A5_new=req.A5+1.05)

def KUKA_server():
    rospy.init_node('Server_for_kuka_arm')
    s = rospy.Service('kuka_arm', AngleValues, handle_exchange_values)
    print("The server has been started")
    rospy.spin()

if __name__ == "__main__":
    KUKA_server()