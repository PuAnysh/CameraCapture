import cv2
import time
from PyQt5.QtCore import QObject, pyqtSignal, QThread


class Camera(QThread):
    def __init__(self):
        super(Camera, self).__init__()
        # 获取摄像头对象，0 系统默认摄像头
        self.cap = cv2.VideoCapture(0)
        self.out = None


    def openFile(self, filepath):
        if not self.cap.isOpened():
            self.cap.open()
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        outputPath = filepath
        # 20fps ,640*480size
        self.out = cv2.VideoWriter(outputPath, fourcc, 20.0, (640, 480))
        # 判断摄像头是否打开，没有则打开


    def run(self):
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:
                # 翻转图片
                # frame = cv2.flip(frame,0)
                # write the flipped frame
                self.out.write(frame)


    def releaseDevice(self):
        # 释放设备

        self.cap.release()
        self.out.release()

