
#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""ROS2 Image Subscriber 
It is a show_img.py script that by default subscribes to the /img_camera topic but

 can take the name of the topic to subscribe to as a parameter. 

vis_img
"""

# Import Modules:
import numpy as np
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import argparse
import sys
#Classes:
class ImageViz(Node):
     """Image visualization Class.
     
     The ImageSubscriber class acts as a subscriber node in ROS2. That is, it subscribes to 
     
     a specific ROS2 community and processes messages from that community.
     
     The purpose of this class
     
     is to receive images from a ROS2 topical and display them on the screen.
     """

     def __init__(self, topic_name):
        super().__init__('vis_img')
        self.topic_name = topic_name
        # Create subscription with dynamic topic name
        self.subscription = self.create_subscription(Image, topic_name, 
                                                     self.listener_callback, 10)
        self.subscription  # prevent unused variable warning


     def listener_callback(self, msg):
        """Listener Callback:
        
        listener_callback fonksiyonu, abone olunan topikten bir mesaj geldiğinde çağrılır.
        
        Bu fonksiyon, mesajdaki görüntü verisini işler ve bu görüntüyü ekranda gösterir.
        """
        height = msg.height
        width = msg.width
        channel = msg.step // msg.width #Number of channels is calculated
        frame = np.reshape(np.frombuffer(msg.data, dtype=np.uint8), (height, width, channel))
        self.get_logger().info(f"{self.topic_name} Received")
            
        # Display image using OpenCV
        cv2.imshow(self.topic_name, frame)
        cv2.waitKey(1)  # Press any key to close window


# Main Method:
def main(args=None):
    print("Starting ROS2 Image Subscriber")
    print(f"Command line arguments: {sys.argv}")

    rclpy.init(args=args)
    
    parser = argparse.ArgumentParser(description='ROS2 Image Subscriber')
    parser.add_argument('--topic', type=str, default='/img_camera',
                        help='Name of the ROS topic to subscribe to')
    
    # Parse known args, ignoring ROS2 args
    parsed_args, _ = parser.parse_known_args()
    
    print(f"Parsed arguments: {parsed_args}")
    print(f"Topic to subscribe: {parsed_args.topic}")
    
    image_subscriber = ImageViz(parsed_args.topic)
    
    print("Node created, starting spin")
    try:
        rclpy.spin(image_subscriber)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
    finally:
        print("Shutting down")
        image_subscriber.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()
#Driver Program:

if __name__ == '__main__':
    main()