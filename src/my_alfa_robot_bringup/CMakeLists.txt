cmake_minimum_required(VERSION 3.8)
project(my_alfa_robot_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch rviz worlds #rviz'i de vermem gerekiyor ki bu da paket içinde yğklensin diye
  DESTINATION share/${PROJECT_NAME}/ # DESTİNATİON DENİLEN ADRES ASLINDA BİZİM PROJEMİZİN GENEL ADRESİNİ İFADE EDİYOR
)

ament_package()
