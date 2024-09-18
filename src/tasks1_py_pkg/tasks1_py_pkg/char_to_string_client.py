#!/usr/bin/python3

# 1. Library
import rclpy
from rclpy.node import Node #rclpy içinden Node metodunu çağırmak
from char_to_string_interfaces_pkg.srv import CharToString

"""
Client code that receives a string of numbers and characters from the user, sends it to the service and prints the result on the screen
"""

class CharToStringClientNode(Node): 
    def __init__(self):
        super().__init__('char_to_string_client')
        self.client = self.create_client(CharToString, 'char_to_string')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for Server - [Char To String]")


    def send_request(self):
        self.request = CharToString.Request() #!!

        # Kullanıcıdan sayı ve karakter dizisini alıyoruz
        self.request.number = int(input('Enter a number: '))
        self.request.characters = input('Enter a characters: ')
        future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    client = CharToStringClientNode()
    response = client.send_request()
    client.get_logger().info(f'Result: {response.result}')
    rclpy.shutdown()

if __name__ == '__main__':
    main()

