import cv2,platform
import urllib
import numpy as np
from sensor_msgs.msg import Image
import roslib
import sys
import rospy
# import cv
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import detect_ball
import os
import cv2
import finalcode

class ipcamera(object):
    def __init__(self, url):
        try:
            self.stream=cv2.VideoCapture(url)
        except:
            rospy.logerr('Unable to open camera stream: ' + str(url))
            sys.exit() #'Unable to open camera stream')
        if not self.stream.isOpened():
            print "Error opening resource: " + str(url)
            print "Maybe opencv VideoCapture can't open it"
            sys.exit()
        #
        print "Correctly opened resource, starting to show feed."
        self.bytes=''
        self.image_pub = rospy.Publisher("ipcam10_vid", Image,queue_size=1000)
        self.bridge = CvBridge()

one_rot = 5
data = []
t = 0
if __name__ == '__main__':
    try:
        camUrl='https://192.168.0.10:8080/video'
        rospy.init_node('ip_cam_10', anonymous=True)
        ip_camera = ipcamera(camUrl)

        while not rospy.is_shutdown():
            ip_camera.stream.set(cv2.CAP_PROP_POS_MSEC, 500)
            rval, frame = ip_camera.stream.read()
            if rval:
                #cv2.imshow("Stream: webcam", frame)
                (rval,frame) = ip_camera.stream.read()
                
                image, frame = detect_ball.detect_ball(frame)
                if (np.any(frame)):
                    #image = detect_ball.getWindow(image, frame)
                    multWindow = detect_ball.getMultiWindow(image, frame)
                    path = '/home/ameya/Desktop/MRT/current/' + str(t)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    for j in range(len(multWindow)):
                        cv2.imwrite(path + '/' + str(j) + ".jpg",multWindow[j])
                #cv2.imwrite("/home/ameya/Desktop/MRT/current/" + str(t) + ".jpg",image)
                #data.append(image)np.save('/home/ameya/Desktop/MRT/current/outputnoball' + str(t) +'.npy', detect_ball.getMultiWindowArray(image, frame))
                np.save('/home/ameya/Desktop/MRT/current/outputnoball' + str(t) +'.npy', detect_ball.getMultiWindowArray(image, frame))
                if (t == one_rot): # completed one round
                    #np.save('/home/ameya/Desktop/MRT/current/outputnoball' + str(t) +'.npy', detect_ball.getMultiWindowArray(image, frame))
                    # call supervised with numpy array and publish result back
                    break
                ip_camera.image_pub.publish(ip_camera.bridge.cv2_to_imgmsg(frame, "8UC1"))
                t = t + 1
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        ip_camera.stream.release()
        
        cv2.destroyAllWindows()
        k = 0
        trace = 0
        keepit = 0
        dance = 0
        while k <one_rot:
            dance =  trace          
            trace = max(trace,finalcode.testvalue(np.load("/home/ameya/Desktop/MRT/current/outputnoball"+str(k)+".npy")))
            if trace>dance:
                store = k
            k = k+1
        print(store) 
    except rospy.ROSInterruptException:
        pass