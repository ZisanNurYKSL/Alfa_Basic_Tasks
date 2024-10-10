from setuptools import find_packages, setup

package_name = 'camera_py_pkg'

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
            "cam_publish = camera_py_pkg.camera_broadcast:main",
            "img_subscribe = camera_py_pkg.img_viz:main",
            "gray_level = camera_py_pkg.gray_level_converter:main"
        ],
    },
)
