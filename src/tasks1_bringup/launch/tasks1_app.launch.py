from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(): #zorunluluk 

    """Çalıştıracağım tüm düğümleri bunun içinde belitiriz"""

    ld = LaunchDescription() #obje tanımlamalıyım 

    weather_forecast_pub = Node( #öncelikle publisher başlatılmalı
        package="tasks1_py_pkg",
        executable="weather_forecast_pub",
     
    )

    weather_forecast_sub = Node( 
        package="tasks1_py_pkg",
        executable="weather_forecast_sub",
    )

    char_to_string_server = Node( 
        package="tasks1_py_pkg",
        executable="char_to_string_server",
    )

    char_to_string_client = Node( 
        package="tasks1_py_pkg",
        executable="char_to_string_client",
    )

    ld.add_action(weather_forecast_pub)
    ld.add_action(weather_forecast_sub)
    ld.add_action(char_to_string_server)
    ld.add_action(char_to_string_client)


    return ld #yukarıdaki action'ların gerçekleşmesi için bu satırı kullanırım