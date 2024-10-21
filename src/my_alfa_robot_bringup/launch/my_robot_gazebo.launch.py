from launch import LaunchDescription 
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    # Dosya yolları
    urdf_path = os.path.join(get_package_share_path('my_alfa_robot_description'),
                            'urdf', 'alfa_main.xacro')
    urdf_config_path = os.path.join(get_package_share_path('my_alfa_robot_description'), 
                                   'rviz', 'urdf_config.rviz')
    world_path = os.path.join(get_package_share_path('my_alfa_robot_bringup'),
                             'worlds', 'test_world.world') # Gazebo için dünya dosyası

    # Robot description oluşturulması
    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    # Node'lar
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
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
        arguments=['-d', urdf_config_path],
        output='screen'
    )

    # Gazebo'yu başlatma
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('gazebo_ros'),
            '/launch/gazebo.launch.py'  # Gazebo'yu başlatmak için ROS2'nin sağladığı launch dosyası
        ]),
        launch_arguments={'world': world_path}.items()
    )

    # Robotu Gazebo'ya spawn etme
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_robot'],
        output='screen'
    )

    # Launch description oluşturma
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node,
        gazebo_launch,   # Gazebo'yu başlatma
        spawn_robot      # Robotu Gazebo'ya yükleme
    ])




"""Açıklamalar:
 ile paket dizinlerini alıyoruz.
Node: ROS2'de bir düğüm (node) başlatmak için kullanılır.
IncludeLaunchDescription: Diğer launch dosyalarını (burada Gazebo'yu) dahil etmek için kullanılır.
Command: Xacro dosyasını işlemek ve robot açıklamasını almak için kullanılır.

Command ve PathJoinSubstitution'ı Import Et
Command ve PathJoinSubstitution'ı ROS2 launch modüllerinden doğru şekilde import etmemiz gerekiyor. 
Bu hatayı düzeltmek için launch dosyanıza şu satırları eklemeniz gerekiyor:

Gazebo Başlatma: gazebo_ros paketinden gazebo.launch.py dosyasıyla Gazebo başlatılır.
Dünya dosyası olarak test_world.world kullanılıyor. Bu dosya, my_alfa_robot_bringup paketinin worlds klasöründe olmalı.
Robotu Spawn Etme: spawn_entity.py ile robotu Gazebo'ya yüklemek için robot_description parametresini kullanıyoruz. 
Bu, yukarıda tanımladığımız URDF dosyasına dayanıyor.
RViz Başlatma: Daha önceki RViz ayarlarınıza ek olarak urdf_config.rviz dosyasıyla RViz başlatılıyor."""