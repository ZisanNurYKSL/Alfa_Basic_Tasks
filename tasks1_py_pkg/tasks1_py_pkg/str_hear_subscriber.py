#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class StrHearSubscriber(Node):
    def __init__(self):
        super().__init__("str_hear_subscriber")
        self.subscriber_ = self.create_subscription(String, "/terminal_str", self.callback_str_read, 10)

        self.get_logger().info("Started listening to the terminal")

    
    def callback_str_read(self,msg):
        self.get_logger().info(msg.data)





def main(args=None):
    rclpy.init(args=args)
    node = StrHearSubscriber()
    rclpy.spin(node)
    rclpy.shutdown



if __name__ == "__main__":
    main()