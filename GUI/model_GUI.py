import random
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QTimer
from GUI.GetReturn import GetReturn
from CaptureVideo.Camera import Camera
from datetime import datetime
import shutil
import time


class Model_GUI(QDialog):

    def __init__(self, model_type, parent=None):
        super().__init__(parent=parent)
        self.time_p = 200
        self.model_type = model_type
        self.timer = QTimer()
        self.timer.timeout.connect(self.currTime)
        self.timer.start(self.time_p)
        self.flag = False
        self.total_Experiment = 10
        self.ans_s = []
        self.ans_b = []
        self.sparkle_list = []
        self.bell_list = []
        self.return_sparkle = -1
        self.return_bell = -1
        self.is_first = True
        self.camera = None
        if self.model_type != 0:
            self.camera = Camera()
            self.camera.openFile('test.avi')
            self.camera_timer = QTimer()
            self.camera_timer.timeout.connect(self.getFrame)
            self.camera_timer.start(33)

        for i in range(self.total_Experiment):
            tmp_s = random.randint(1, 4)
            tmp_b = random.randint(1, 4)
            skip = random.randint(0, 2)
            self.ans_s.append(tmp_s)
            self.ans_b.append(tmp_b)
            tmp_list_s = []
            tmp_list_b = [] + [False] * skip
            for i in range(tmp_s):
                tmp_list_s += [True, False, False]
            for i in range(tmp_b):
                tmp_list_b += [True, False, False]
            if len(tmp_list_s) > len(tmp_list_b):
                tmp_list_b += [False] * (len(tmp_list_s) - len(tmp_list_b))
            else:
                tmp_list_s += [False] * (len(tmp_list_b) - len(tmp_list_s))
            self.sparkle_list.append(tmp_list_s)
            self.bell_list.append(tmp_list_b)
        if self.model_type != 0:
            self.camera = Camera()
            self.camera.openFile('test.mp4')
            self.camera_timer = QTimer()
        self.is_bell = True
        if self.model_type == 1:
            self.is_bell = False
        if self.model_type == 2:
            self.is_bell = True
            self.bell_list = self.sparkle_list
        if self.model_type == 3:
            self.is_bell = True
        self.experiment_idx = 0
        self.sparkle_idx = 0
        self.log_file = open('temp.log', 'w')
        self.log_file.write(str(self.ans_s)+'\n')
        self.log_file.write(str(self.ans_b)+'\n')


        # super()方法返回了父类对象并调用了父类的构造方法
        # self.__init_ui()

    def __init_ui(self):
        pass

    def paintEvent(self, QPaintEvent):
        if self.flag:
            w = self.width()
            h = self.height()
            painter = QPainter(self)
            painter.setPen(QColor(166, 66, 250))
            _w = w / 4
            _h = h / 4
            painter.begin(self)
            painter.drawLine(w / 2 + _w, h / 2, w / 2 - _w, h / 2)
            painter.drawLine(w / 2, h / 2 + _h, w / 2, h / 2 - _h)
            painter.end()

    def currTime(self):
        self.update()
        if self.is_first:
            for i in range(3):
                print('\a')
                time.sleep(2)
            # self.camera_timer.timeout.connect(self.getFrame)
            # self.camera_timer.start(33)

            QMessageBox.information(self, '标题', '开始本次实验', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if not self.camera is None:
                self.camera.start()
            self.log_file.write(str(datetime.now()) + '\n')
        self.is_first = False
        self.flag = self.sparkle_list[self.experiment_idx][self.sparkle_idx]
        if self.bell_list[self.experiment_idx][self.sparkle_idx] and self.is_bell:
            print('\a')
        self.sparkle_idx += 1
        self.update()
        if self.sparkle_idx == len(self.sparkle_list[self.experiment_idx]):
            self.timer.stop()
            self.log_file.write(str(datetime.now()) + '\n')
            if self.model_type == 0:
                QMessageBox.information(self, '标题', '闪烁{}次，响铃{}次'.format(self.ans_s[self.experiment_idx],
                                                                         self.ans_b[self.experiment_idx]), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            getDialog = GetReturn(self.model_type, parent=self)
            getDialog.return_s.connect(self.setReturn_s)
            getDialog.return_b.connect(self.setReturn_b)
            getDialog.show()
            getDialog.exec()
            self.log_file.write(str(self.return_sparkle)+' '+str(self.return_bell) + '\n')
            self.log_file.write(str(datetime.now()) + '\n')
            # print(used)
            self.experiment_idx += 1
            self.sparkle_idx = 0
            if self.experiment_idx == self.total_Experiment:
                if not self.camera is None:
                    self.camera.quit()
                    self.camera_timer.stop()
                    self.camera.releaseDevice()
                    self.log_file.close()
                    self.saveFile()
                self.close()
            self.timer.start(self.time_p)

    def setReturn_s(self, x):
        self.return_sparkle = x

    def setReturn_b(self, x):
        self.return_bell = x

    def getFrame(self):
        self.camera.run()

    def saveFile(self):

        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                "数据1保存",
                                                                "test1.mp4",
                                                                "MP4(*.mp4);")
        shutil.copyfile('test.mp4', fileName_choose)
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                "数据2保存",
                                                                "test1.txt",
                                                                "TXT(*.txt);")
        shutil.copyfile('temp.log', fileName_choose)
