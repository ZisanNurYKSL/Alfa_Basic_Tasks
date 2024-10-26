#!/usr/bin/python3
"""Burada iki şey yapacağım öncelikle yayınlanan lidar değerlerini abone olarak döndüren değerleri görmek.
Bunları gördükten sonra cmd_vel topiğine abone olarak bazı açısal ve doğrusal hız değerleri yayınlayacağım ve bu değerlere göre robotumuz gidecek veya duracak """

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LidarDataNode(Node):
    def __init__(self):
        super().__init__("lidar_data_node")
        self.get_logger().info("Lidar node has been start info")

        self.subscriber_ = self.create_subscription(LaserScan, "/lidar/out", self.callback_data, 10) #burada /lidar/out'a subscribe oldum

        self.publishers_ = self.create_publisher(Twist, "/cmd_vel", 10 ) #genle olarak /cmd_vel topic'inden hız verileri okunur.

    def callback_data(self,msg): #lidar data'ları bir msg içerisinde olacak 

        min_lidar_data_ = min(msg.ranges) #lidar'ın döndürdüğü mesafe değerleri ranges'in içerisinde saklı
        
        self.get_logger().info("LIDAR data: " + str(min_lidar_data_)) #min_lidar_data'yı doğrudan gönderemiyorum en azından info ile bunu str'ye çeviriyorum.
   
        """Aracın hızı 2m'ye düşene kadar araç belli bir hızla ilerlemeli ve mesafe 2m'ye düşünce aracım durmalı """
        
        velocity = Twist() #Twist sınıfını kullanrak bir velocity nesnesi oluşturdum
        velocity.linear.x = 0.5
        velocity.linear.y = 0.0
        velocity.angular.z = 0.0 #kara aracının dönüşü için açısal z değeri kullanılır. 

        if min_lidar_data_ <= 2.5:
              velocity.linear.x = 0.0
              velocity.linear.y = 0.0
              velocity.angular.z = 0.0 


        self.publishers_.publish(velocity)
 
def main(args=None):
    rclpy.init(args=args)
    node = LidarDataNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "main":
    main()
