from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from GUI.model_GUI import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont


class GUI_main(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # super()方法返回了父类对象并调用了父类的构造方法
        self.__init_ui()

    def __init_ui(self):
        self.example_PushButton = QPushButton('学习模式')
        self.test1_PushButton = QPushButton('模式一')
        self.test2_PushButton = QPushButton('模式二')
        self.test3_PushButton = QPushButton('模式三')
        self.test4_PushButton = QPushButton('模式四')

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.example_PushButton)
        self.v_layout.addWidget(self.test1_PushButton)
        self.v_layout.addWidget(self.test2_PushButton)
        self.v_layout.addWidget(self.test3_PushButton)
        self.v_layout.addWidget(self.test4_PushButton)


        self.example_PushButton.clicked.connect(self.on_example_0_pushbutton_clicked)
        self.test1_PushButton.clicked.connect(self.on_example_1_pushbutton_clicked)
        self.test2_PushButton.clicked.connect(self.on_example_2_pushbutton_clicked)
        self.test3_PushButton.clicked.connect(self.on_example_3_pushbutton_clicked)
        self.test4_PushButton.clicked.connect(self.on_example_4_pushbutton_clicked)
        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('注意力集中程度测评')
        self.setLayout(self.v_layout)
        self.show()

    def on_example_0_pushbutton_clicked(self):
        dialog = Model_GUI(model_type=0, parent=None)
        dialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
        dialog.showFullScreen()
        # dialog.show()
        dialog.exec()

    def on_example_1_pushbutton_clicked(self):
        dialog = Model_GUI(model_type=1, parent=None)
        dialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
        dialog.showFullScreen()
        # dialog.show()
        dialog.exec()
    def on_example_2_pushbutton_clicked(self):
        dialog = Model_GUI(model_type=2, parent=None)
        dialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
        dialog.showFullScreen()
        # dialog.show()
        dialog.exec()
    def on_example_3_pushbutton_clicked(self):
        dialog = Model_GUI(model_type=3, parent=None)
        dialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
        dialog.showFullScreen()
        # dialog.show()
        dialog.exec()
    def on_example_4_pushbutton_clicked(self):
        dialog = Model_GUI(model_type=4, parent=None)
        dialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
        dialog.showFullScreen()
        # dialog.show()
        dialog.exec()
