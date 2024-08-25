#!/usr/bin/python3

# 1. Library
import rclpy
from rclpy.node import Node #rclpy içinden Node metodunu çağırmak
from example_interfaces.msg import String


class StrReadPublisher(Node):# 1 #Node'u buraya girdiğimde aslında bu class gerçekleştirilebilir hale geliyor.
    def __init__(self):
        super().__init__("str_read_publisher") #2

        self.publisher_ = self.create_publisher(String, "/terminal_str", 10 )
        
        self.timer = self.create_timer(1, self.publisher_str_read)
        
        self.get_logger().info("Starting string reading from terminal")


    def publisher_str_read(self):
        msg = String()
        input = input("Lütfen Sring Giriniz:")
        msg.data = input
        self.publisher_.publish(msg)


# 2. Metodu yaz
def main(args=None):
    rclpy.init(args=args) #bir metodu başlatmak için yapmam gereken şey
    node = StrReadPublisher() # 3 #node'u oluşturmak için
    rclpy.spin(node)#bu düğümün yaşam döngüsünü başlatırım
    rclpy.shutdown() # ben düğümü kapattığımda veya durdurduğumda shutdown'a gelecek ve düğümü yok edecek



# 3. if __name__ block 

if __name__ == "__main__": 
    main()
