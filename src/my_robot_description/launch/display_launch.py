from launch import LaunchDescription #
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node #sağlıklı bir şekilde düğüm oluşturabilmem için eklemeliyim
from launch.substitution import Command

import os  #bu paketi bir directory üretmek için kullanırım.
from ament_index_python.packages import get_package_share_path  #bu paket bizim belirlediğimiz pakete dair path'in tespit edilmesi için kullanılır.

def generate_launch_description():
    urdf_path = os.path.join(get_package_share_path('my_robot_description'),
                            'urdf', 'my_robot.urdf')
    urdf_config_path = os.path.join(get_package_share_path('my_robot_description'), 
                                   'rviz', 'urdf_config.rviz')
    
    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str) #bu satırın aktif olması içn bu kütüphanenin eklenmesi lazım: from launch_ros.parameter_descriptions import ParameterValue


    robot_state_publisher_node = Node(
        package="robot_state_publisher",  #bu paket default yani ros2 ile birlikte gelir
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', urdf_config_path] #rviz_config_path'de argümanlarımın bulunduğun söylüyorum
    )


    return LaunchDescription([ #burada döndürüecek olan düğümleri öncelikle yukarıda oluşturmam gerekiyor. 
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])