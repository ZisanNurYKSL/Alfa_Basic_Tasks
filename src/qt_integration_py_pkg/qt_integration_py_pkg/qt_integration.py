# -*- coding: utf-8 -*-

import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image as RosImage
from cv_bridge import CvBridge
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap

# class ImageSubscriber(Node):
#     def __init__(self):
#         super().__init__('image_subscriber')
#         self.subscription = self.create_subscription(RosImage, '/img_camera', self.listener_callback, 10)
#         self.bridge = CvBridge()
        
#         # Initialize the PyQt window
#         self.init_ui()

#     def init_ui(self):
#         # Create the main window
#         self.window = QWidget()
#         self.window.setWindowTitle('ROS2 Image Viewer')
#         self.window.resize(800, 600)

#         # Create a vertical layout
#         layout = QVBoxLayout()

#         # Create a QLabel to display images
#         self.label = QLabel()
#         layout.addWidget(self.label)  # Add QLabel to the layout

#         # Set the layout on the main window
#         self.window.setLayout(layout)
        
#         # Show the window
#         self.window.show()

#     def listener_callback(self, msg):
#         # Convert ROS Image message to OpenCV format
#         cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
#         # Convert OpenCV image to QImage
#         height, width, channel = cv_image.shape
#         bytes_per_line = 3 * width
#         q_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

#         # Update the QLabel with the new image
#         self.label.setPixmap(QPixmap.fromImage(q_image))

# def main(args=None):
#     rclpy.init(args=args)
#     image_subscriber = ImageSubscriber()
    
#     # Start the PyQt application loop
#     app = QApplication(sys.argv)
    
#     # Run the ROS2 node in a separate thread if needed (not shown here)
    
#     rclpy.spin(image_subscriber)  # Keep spinning while waiting for messages
    
#     image_subscriber.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()



import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image as RosImage
from cv_bridge import CvBridge
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox, QMainWindow

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 410, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 471, 351))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 410, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 470, 561, 70))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect button click event
        self.ui.pushButton.clicked.connect(self.on_push_button_clicked)
        # Initialize ROS2 node
        rclpy.init()
        self.node = Node("my_gui_node")
        self.publisher_ = self.node.create_publisher(String, "/girilen_metin", 10)
        self.subscription = self.node.create_subscription(RosImage, '/img_camera', self.listener_callback, 10)
        self.bridge = CvBridge()

    def on_push_button_clicked(self):
        topic_name = self.ui.lineEdit.text()  # Get the topic name entered by the user
        if not topic_name:
            QMessageBox.warning(self, "Hata", "Lütfen bir topic adı girin.")
        else:
            self.ui.textEdit.setPlainText(f"Girilen topic: {topic_name}")
            msg = String()
            msg.data = topic_name
            self.publisher_.publish(msg)
            # Here you can add subscription to the topic if needed

    def closeEvent(self, event):
        rclpy.shutdown()  # Stop the ROS2 node when the application is closed
        event.accept()

    def listener_callback(self, msg):
        # Convert ROS Image message to OpenCV format
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # Convert OpenCV image to QImage
        height, width, channel = cv_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        # Update the QLabel with the new image
        self.ui.label.setPixmap(QPixmap.fromImage(q_image))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    while rclpy.ok():
        rclpy.spin_once(window.node, timeout_sec=0.1)
        app.processEvents()
    window.node.destroy_node()
    rclpy.shutdown()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
""" import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import rclpy
from rclpy.node import Node
from your_interface import Ui_MainWindow  # Qt Designer'dan oluşturduğunuz arayüz dosyası

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buton tıklama olayını bağlama
        self.ui.pushButton.clicked.connect(self.on_push_button_clicked)

        # ROS2 düğümünü başlat
        rclpy.init()
        self.node = Node("my_gui_node")

    def on_push_button_clicked(self):
        topic_name = self.ui.lineEdit.text()  # Kullanıcının girdiği topic adı
        if not topic_name:
            QMessageBox.warning(self, "Hata", "Lütfen bir topic adı girin.")
        else:
            self.ui.textEdit.setPlainText(f"Girilen topic: {topic_name}")
            # Burada topic'e abone olma işlemleri yapılabilir

    def closeEvent(self, event):
        rclpy.shutdown()  # Uygulama kapatıldığında ROS2 düğümünü durdurun
        event.accept()
        
        
        
        
        
        class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buton tıklama olayını bağlama
        self.ui.pushButton.clicked.connect(self.on_push_button_clicked)
        #self.ui.label.setText("Ahmeett")
        
        #ROS2 düğümünü başlat
        rclpy.init()
        self.node = Node("my_gui_node")

    def on_push_button_clicked(self):
        topic_name = self.ui.lineEdit.text()  # Kullanıcının girdiği topic adı
        if not topic_name:
            QMessageBox.warning(self, "Hata", "Lütfen bir topic adı girin.")
        else:
            self.ui.textEdit.setPlainText(f"Girilen topic: {topic_name}")
            # Burada topic'e abone olma işlemleri yapılabilir
        comming_string= self.ui.lineEdit.text()
        self.ui.label.setText(comming_string)

    def closeEvent(self, event):
        rclpy.shutdown()  # Uygulama kapatıldığında ROS2 düğümünü durdurun
        event.accept()"""