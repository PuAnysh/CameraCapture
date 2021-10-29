import cv2
import time


# 定义摄像头类
class cameraComput(object):
    def __init__(self):
        # 获取摄像头对象，0 系统默认摄像头
        self.cap = cv2.VideoCapture(0)
        # 判断摄像头是否打开，没有则打开
        if not self.cap.isOpened():
            self.cap.open()

    def getFrame(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imshow("frame", frame)
            time.sleep(5)
        return frame

    # 录制一段时长的
    def saveVideo(self, filepath, delays):
        # Define the codec and create VideoWriter object
        # 视频编码
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        outputPath = filepath
        # 20fps ,640*480size
        out = cv2.VideoWriter(outputPath, fourcc, 20.0, (640, 480))
        startTime = time.time()
        while (self.cap.isOpened):
            ret, frame = self.cap.read()
            if ret:
                # 翻转图片
                # frame = cv2.flip(frame,0)
                # write the flipped frame
                out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
            if time.time() - startTime > delays:
                break
        out.release()
        return True

    # 保存一个快照
    def saveSnapshot(self, filepath):
        if self.cap.isOpened:
            ret, frame = self.cap.read()
            if ret:
                cv2.imwrite(filepath, frame)
            else:
                print("save snapshot fail")
                return False
        return True

    def releaseDevice(self):
        # 释放设备
        self.cap.release()

    def reOpen(self):
        if not self.cap.isOpened():
            print("re opened device")
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.cap.open()
#
# c = cameraComput()
# c.saveVideo('tet.mp4',33)
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget    #导入相应的包
from PyQt5.QtWidgets import QApplication , QMainWindow
from GUI.GUI_main import *

if __name__ == '__main__':
   """
   主函数
   """
   app = QApplication(sys.argv)
   #app = QApplication(sys.argv)，每一个pyqt程序必须创建一个application对象，
   #sys.argv是命令行参数，可以通过命令启动的时候传递参数。
   mainWindow = GUI_main()
   mainWindow.show()  #用来显示窗口
   sys.exit(app.exec_())#exec_()方法的作用是“进入程序的主循环直到exit()被调