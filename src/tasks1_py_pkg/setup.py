from setuptools import find_packages, setup

package_name = 'tasks1_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zisannur',
    maintainer_email='zisannuryuksel2323@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talker = tasks1_py_pkg.str_read_publisher:main",
            "listener = tasks1_py_pkg.str_hear_subscriber:main",
            "char_to_string_server = tasks1_py_pkg.char_to_string_server:main",
            "char_to_string_client = tasks1_py_pkg.char_to_string_client:main",
            "weather_forecast_sub = tasks1_py_pkg.weather_forecast_sub:main",
            "weather_forecast_pub = tasks1_py_pkg.weather_forecast_pub:main"



        ],
    },
)
