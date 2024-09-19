#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from char_to_string_interfaces_pkg.msg import WeatherForecast
import time

class WeatherForecastSubscriber(Node):
    def __init__(self):
        super().__init__("weather_sub")

        self.subscriber_ = self.create_subscription(WeatherForecast, "/weather_data", self.callback_weather_forecast_read, 10)

        self.get_logger().info("Listener Python node has been started")

        self.subscriber_ #kullanılmayan değişken uyarısını engelle


    
    def callback_weather_forecast_read(self,msg):
        """
        Used to process incoming weather data at the ROS2 Subscriber node
        """
        temperature = msg.temperature
        humidity = msg.humidity
        wind_speed = msg.wind_speed   

        self.get_logger().info(f'Received data - Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %, Wind Speed: {wind_speed:.2f} km/h')


def main(args=None):
    rclpy.init(args=args)
    weather_subscriber = WeatherForecastSubscriber()
    rclpy.spin(weather_subscriber)
    weather_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
