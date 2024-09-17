#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class StrHearSubscriber(Node):
    def __init__(self):
        super().__init__("str_hear_subscriber")
        self.subscriber_ = self.create_subscription(String, "/terminal_str", self.callback_str_read, 10)

        self.get_logger().info("Listener Python node has been started")

        self.subscriber_ #kullanılmayan değişken uyarısını engelle


    
    def callback_str_read(self,msg):
        now = time.time()
        current_time = time.localtime(now)
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
        self.get_logger().info('I heard: "%s" - Time: %s' % (msg.data, formatted_time))



def main(args=None):
    rclpy.init(args=args)
    node = StrHearSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown



if __name__ == "__main__":
    main()
