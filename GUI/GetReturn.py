from PyQt5.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import Qt


class GetReturn(QDialog):
    return_s = pyqtSignal(object)
    return_b = pyqtSignal(object)

    def __init__(self, model, parent=None):
        super().__init__(parent=parent)

        self.model = model
        self.main_layout = QVBoxLayout()
        self.layout_s = QHBoxLayout()
        self.layout_b = QHBoxLayout()
        self.label_s = QLabel('加号闪烁次数：')
        self.pushbutton_s1 = QPushButton('1次（A）')
        self.pushbutton_s2 = QPushButton('2次（S）')
        self.pushbutton_s3 = QPushButton('3次（D）')
        self.pushbutton_s4 = QPushButton('4次（F）')
        self.layout_s.addWidget(self.pushbutton_s1)
        self.layout_s.addWidget(self.pushbutton_s2)
        self.layout_s.addWidget(self.pushbutton_s3)
        self.layout_s.addWidget(self.pushbutton_s4)
        self.label_b = QLabel('铃声次数(不需要作答的时候忽略)：')
        self.pushbutton_b1 = QPushButton('1次（J）')
        self.pushbutton_b2 = QPushButton('2次（K）')
        self.pushbutton_b3 = QPushButton('3次（L）')
        self.pushbutton_b4 = QPushButton('4次（;）')
        self.layout_b.addWidget(self.pushbutton_b1)
        self.layout_b.addWidget(self.pushbutton_b2)
        self.layout_b.addWidget(self.pushbutton_b3)
        self.layout_b.addWidget(self.pushbutton_b4)
        self.main_layout.addWidget(self.label_s)
        self.main_layout.addLayout(self.layout_s)
        self.main_layout.addWidget(self.label_b)
        self.main_layout.addLayout(self.layout_b)
        self.setLayout(self.main_layout)
        self.flag_s = False
        self.flag_b = False
        if model in [1, 2]:
            self.flag_s = True
        if model in [3, 4]:
            self.flag_s = True
            self.flag_b = True

    # self.emit_return_s(82)
    # self.label_b = QLabel('铃声闪烁次数：')

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_A:
            if self.flag_s:
                self.flag_s = False
                self.emit_return_s(1)
        if QKeyEvent.key() == Qt.Key_S:
            if self.flag_s:
                self.flag_s = False
                self.emit_return_s(2)
        if QKeyEvent.key() == Qt.Key_D:
            if self.flag_s:
                self.flag_s = False
                self.emit_return_s(3)
        if QKeyEvent.key() == Qt.Key_F:
            if self.flag_s:
                self.flag_s = False
                self.emit_return_s(4)
        if QKeyEvent.key() == Qt.Key_J:
            if self.flag_b:
                self.flag_b = False
                self.emit_return_b(1)
        if QKeyEvent.key() == Qt.Key_K:
            if self.flag_b:
                self.flag_b = False
                self.emit_return_b(2)
        if QKeyEvent.key() == Qt.Key_L:
            if self.flag_b:
                self.flag_b = False
                self.emit_return_b(3)
        if QKeyEvent.key() == 59:#;
            if self.flag_b:
                self.flag_b = False
                self.emit_return_b(4)
        if self.flag_b == False and self.flag_s == False:
            self.close()

    def emit_return_s(self, x):
        self.return_s.emit(x)

    def emit_return_b(self, x):
        self.return_b.emit(x)
