#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from char_to_string_interfaces_pkg.msg import WeatherForecast
import random
import time

class WeatherForecastPublisher(Node):
    def __init__(self):
        super().__init__("weather_publisher")
        self.publisher_ = self.create_publisher(WeatherForecast, "/weather_data", 10)
        self.timer = self.create_timer(5.0, self.publish_weather_data)

    def publish_weather_data(self):
        msg = WeatherForecast()
        msg.temperature = random.uniform(-10.0, 40.0)  # Sıcaklık
        msg.humidity = random.uniform(0.0, 100.0)      # Nem
        msg.wind_speed = random.uniform(0.0, 20.0)     # Rüzgar hızı       
        
        self.publisher_.publish(msg) #??

        self.get_logger().info(f'Publishing: Temperature: {msg.temperature:.2f} °C,, Humidity: {msg.humidity:.2f} %, Wind Speed: {msg.wind_speed:.2f} km/h')

def main(args=None):
    rclpy.init(args=args)
    weather_publisher = WeatherForecastPublisher()
    rclpy.spin(weather_publisher)
    weather_publisher.destroy_node() 
    rclpy.shutdown()

if __name__ == '__main__':
    main()
