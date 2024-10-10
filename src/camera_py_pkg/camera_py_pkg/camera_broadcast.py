
#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Camera Image Reader Publisher with ROS2

A publisher that reads the image from the camera in 

frames and publishes them to the /img_camera topic
"""

#import Modules:
import os
import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

#Global Variables:
DEVICE_INDEX = 0 #Specifies which camera
TOPIC = '/img_camera'
QUEUE_SIZE = 1
PERIOD = 0.1 #Seconds

#Classes:
class CameraBroadcaster(Node):
    """Camera Broadcaster Class.

    This class contains all methods to publish camera data and info in ROS 2 
    topic in sensor_msgs.msg/Image format. 
    
    """
    
    def __init__(self, capture, topic=TOPIC, queue=QUEUE_SIZE, period=PERIOD):
        """Constructor.

        Args:
            capture: OpenCV Videocapture object.

        """
        super().__init__('camera_publisher')
        
        # Initialize publisher
        self.publisher_ = self.create_publisher(Image, topic, queue)
        self.timer = self.create_timer(period, self.timer_callback)
        
        # Set image counter and videocapture object
        self.capture = capture
        self.i = 0

    def timer_callback(self):
        """Timer Callback Function
        This method captures images and publishes required data in ROS2 topic"""

        if self.capture.isOpened():

            #Read image data
            ret, frame = self.capture.read()

            #Process image data and convert to ROS2 message
            msg = Image()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "camera_frame"
            msg.height = np.shape(frame)[0]
            msg.width = np.shape(frame)[1]
            msg.encoding = "bgr8"
            msg.is_bigendian = False
            msg.step = np.shape(frame)[2] * np.shape(frame)[1]
            msg.data = np.array(frame).tobytes()

            #Publish message
            self.publisher_.publish(msg)
            self.get_logger().info(f'{self.i} Images Published')

        #Increment image counter
        self.i = self.i + 1

# Main Method:

def main(args=None):
    
    #Create OpenCV Vidoecapture object
    capture = cv2.VideoCapture(DEVICE_INDEX) #VideoCapture is used to capture video streams
    capture.set(cv2.CAP_PROP_BUFFERSIZE,2) #Used to set some properties of the VideoCapture object.

    #Initilalize node and start publishing 
    rclpy.init(args=args)
    camera_publisher = CameraBroadcaster(capture)
    rclpy.spin(camera_publisher)

    #Shutdown node and release resources
    camera_publisher.destroy_node()
    rclpy.shutdown()
    capture.release() #When the program ends, this command is used to properly close the camera connection. 


#Driver Program:

if __name__ == '__main__':
    main()











 