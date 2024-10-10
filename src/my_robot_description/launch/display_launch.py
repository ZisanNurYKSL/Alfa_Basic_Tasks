from launch import LaunchDescription #
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node #sağlıklı bir şekilde düğüm oluşturabilmem için eklemeliyim
from launch.substitution import Command

import os  #bu paketi bir directory üretmek için kullanırım.
from ament_index_python.packages import get_package_share_path  #bu paket bizim belirlediğimiz pakete dair path'in tespit edilmesi için kullanılır.
