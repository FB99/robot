#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: keyboard_controler.py
@time: 2018/3/26 下午6:51
@description:

    old version

'''

from .robot_interface import *
from .robot_parament import *
from .dashgo_interface import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import *
import sys


# ls /dev/tty.*

class keyboard_controler(QWidget):
    def __init__(self, robot_serialname, dashgo_serialname, action_seq=defaultAction, add_angle=3):
        # init arm
        self.arm = ARMcontroler(robot_serialname)
        self.action_seq = action_seq
        self.add_angle = add_angle
        self.arm.CMD_reset()

        # init dashgo
        self.dg = dashgo(dashgo_serialname)
        print("start\r 用键盘控制,g获得两轮走过的长度，获取障碍距离")
        self.dg.get_length()

        # init UI
        super().__init__()
        self.background_image_path = "./image/robot.png"
        self.screen_size = (400, 600)
        self.initUI()

    def initUI(self):
        # self.app = QApplication(sys.argv)
        # self.w = QWidget()
        # self.w.setWindowTitle('Server Robot Controler')
        # self.w.screen_size = (self.background.get_rect().right, self.background.get_rect().bottom)
        # self.w.setGeometry(400,600, 0, 32)
        # self.w.setStyleSheet("background-image:url(%s)" % self.background_image_path)
        # self.w.show()
        print("here")
        # sys.exit(self.app.exec_())

        self.setGeometry(300, 300, 300, 200)
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.setWindowTitle('Server Robot Controler')
        self.show()







    def keyPressEvent(self, event):
        print("按下：" + str(event.key()))
        # 举例

        if event.key() == Qt.Key_E and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["L1"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)

        if event.key() == Qt.Key_E:
            self.action_seq[armNum["L1"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)

        if event.key() == Qt.Key_W:
            self.action_seq[armNum["L2"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_W and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["L2"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Q:
            self.action_seq[armNum["L3"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Q and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["L3"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_A:
            self.action_seq[armNum["L4"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_A and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["L4"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_S:
            self.action_seq[armNum["L5"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_S and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["L5"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_D:
            self.action_seq[armNum["L6"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_D and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["L6"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)

        if event.key() == Qt.Key_Z:
            self.action_seq[fingerNum["L1"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Z and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["L1"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_X:
            self.action_seq[fingerNum["L2"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_X and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["L2"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_C:
            self.action_seq[fingerNum["L3"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_C and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["L3"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_V:
            self.action_seq[fingerNum["L4"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_V and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["L4"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_B:
            self.action_seq[fingerNum["L5"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_B and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["L5"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)

        if event.key() == Qt.Key_I:
            self.action_seq[armNum["R1"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_I and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["R1"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_O:
            self.action_seq[armNum["R2"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_O and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["R2"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_P:
            self.action_seq[armNum["R3"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_P and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["R3"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_L:
            self.action_seq[armNum["R4"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_L and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["R4"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_K:
            self.action_seq[armNum["R5"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_K and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["R5"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_J:
            self.action_seq[armNum["R6"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_J and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[armNum["R6"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)

        if event.key() == Qt.Key_Slash:
            self.action_seq[fingerNum["R1"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Slash and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["R1"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Period:
            self.action_seq[fingerNum["R2"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Period and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["R2"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Comma:
            self.action_seq[fingerNum["R3"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_Comma and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["R3"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_M:
            self.action_seq[fingerNum["R4"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_M and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["R4"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_N:
            self.action_seq[fingerNum["R5"]] += self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)
        if event.key() == Qt.Key_N and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.action_seq[fingerNum["R5"]] -= self.add_angle
            self.arm.CMD_SERVO_MOVE(self.action_seq)



        if event.key() == Qt.Key_R and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            print("pressed: shift + r")



        if event.key() == Qt.Key_R:
            self.arm.CMD_reset()
            self.action_seq = defaultAction



        # if event.key() == Qt.Key_Up:
        #     self.add_angle += 1
        # if event.key() == Qt.Key_Down:
        #     self.add_angle -= 1


        # 用于展示
        if event.key() == Qt.Key_1:
            ID_angle = {armNum["L4"]: 50, armNum['R4']: 100}
            self.arm.CMD_SERVO_MOVE(ID_angle)
        if event.key() == Qt.Key_2:
            ID_angle = {armNum["L5"]: 30, armNum['L6']: 30, armNum['R1']: 50}
            self.arm.CMD_SERVO_MOVE(ID_angle)
        if event.key() == Qt.Key_3:
            self.arm.CMD_ACTION_GROUP_RUN(1, 1)

        if event.key() == Qt.Key_Up:
            self.dg.go_forward()
        if event.key() == Qt.Key_Down:
            self.dg.go_forward(False)
        if event.key() == Qt.Key_Left:
            self.dg.turn(False)
        if event.key() == Qt.Key_Right:
            self.dg.turn()
        if event.key() == Qt.Key_Space:
            self.dg.stop()
        if event.key() == Qt.Key_G:
            self.dg.get_length()
        if event.key() == Qt.Key_B:
            print(self.dg.collision_detect())



if __name__ == "__main__":
    pass


