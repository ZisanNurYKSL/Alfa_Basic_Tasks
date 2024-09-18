#!/usr/bin/python3

# 1. Library
import rclpy
from rclpy.node import Node #rclpy içinden Node metodunu çağırmak
from char_to_string_interfaces_pkg.srv import CharToString

"""
Service code that creates and returns a string by concatenating characters when the same characters are entered according to the number entered by the user
"""

class CharToStringSeverNode(Node): 
    def __init__(self):
        super().__init__("char_to_string_server") 

        self.comming_msg = ""


        self.server_ = self.create_service(CharToString, "char_to_string", self.callback_char_to_string)
        self.get_logger().info("Char to String server has been started !")

    
    def callback_char_to_string(self, request, response):
        characters = request.characters #karakterleri alıyorum
        number = request.number 
        for i in range(number):
            self.comming_msg += characters
        response.result = self.comming_msg #!!
        return response

    
def main(args=None):
    rclpy.init(args=args)
    node = CharToStringSeverNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()




