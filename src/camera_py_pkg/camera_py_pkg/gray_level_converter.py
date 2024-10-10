
#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""Script to Subscribe to image_camera Topic and 

Convert Incoming Image to Gray Level 

gray level converteer"""

# import Modules:
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 
import numpy as np

# Classes:
"""Receives and processes images from camera_publisher and 

publishes them to a new topic. 

This class inherits from camera_publisher."""

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('gray_level')
        
        # Create subscriber to /img_camera topic
        self.subscription = self.create_subscription(Image,'/img_camera',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        
        # Create publisher to /img_gray_level topic
        self.publisher_ = self.create_publisher(Image, '/gray_level', 10)
        
        # Initialize CvBridge
        self.bridge = CvBridge()



    def listener_callback(self, msg):
        """This function indicates that the color format of the image is 
        
        BGR and then converts it to a gray level image and broadcasts it."""
        self.get_logger().info("Received an image!")
        
        # Convert ROS Image message to OpenCV image
        cv2_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        
        # Convert grayscale image back to ROS Image message
        gray_img_msg = self.bridge.cv2_to_imgmsg(gray_img, encoding="mono8")
        
        # Publish the grayscale image to /img_gray_level topic
        self.publisher_.publish(gray_img_msg)
        self.get_logger().info("Published grayscale image")


# Main Method:
def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)

    image_processor.destroy_node()
    rclpy.shutdown()


#Driver Program:

if __name__ == '__main__':
    main()


        
