#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: robotDemo.py
@time: 2018/10/10 5:56 PM
@description:
'''

import sys
import os
from PyQt5.QtWidgets import QWidget,  QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QLCDNumber, QDateTimeEdit, QTextBrowser
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import QTimer
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
from copy import deepcopy

from PyQt5.QtCore import QBasicTimer, QDateTime
import time
import datetime

from api.robot_interface import *
from api.robot_parament import *


class Controller(QTabWidget):

    def __init__(self, robot_serialname, action_seq=defaultAction, add_angle=3):
        super(Controller, self).__init__()

        # 初始化设备
        ###############################################################
        # init arm
        self.arm = ARMcontroler(robot_serialname)
        self.action_seq = deepcopy(action_seq)
        self.add_angle = add_angle
        self.arm.CMD_reset()


        # init camera


        ###############################################################

        # init UI
        self.tab_robot = QWidget()
        self.tab_sensor = QWidget()
        self.addTab(self.tab_robot, "ROBOT")
        self.addTab(self.tab_sensor, "SENSOR")

        self.init_robot_UI()
        self.init_sensor_UI()

        self.setGeometry(200, 200, 1200, 800)
        self.setWindowTitle("服务机器人控制器")
        self.center()
        self.set_event()
        self.show()

    # 用于定义界面
    def init_robot_UI(self):

        vleftbox = QVBoxLayout()
        self.label_kinect = QLabel("Kinect 信号")
        self.label_kinect.setAutoFillBackground(False)

        self.label_map = QLabel("Map 信号")

        vleftbox.addWidget(self.label_kinect)
        vleftbox.addWidget(self.label_map)

        vrightbox = QVBoxLayout()

        h1rightbox = QHBoxLayout()

        grid_larm = QGridLayout()
        grid_larm.setSpacing(5)

        self.bt_L1 = QPushButton("L1")
        self.bt_L2 = QPushButton("L2")
        self.bt_L3 = QPushButton("L3")
        self.bt_L4 = QPushButton("L4")
        self.bt_L5 = QPushButton("L5")
        self.bt_L6 = QPushButton("L6")
        self.bt_LF1 = QPushButton("LF1")
        self.bt_LF2 = QPushButton("LF2")
        self.bt_LF3 = QPushButton("LF3")
        self.bt_LF4 = QPushButton("LF4")
        self.bt_LF5 = QPushButton("LF5")

        grid_larm.addWidget(self.bt_L3, 0, 2, 1, 1)
        grid_larm.addWidget(self.bt_L2, 0, 3, 1, 1)
        grid_larm.addWidget(self.bt_L1, 0, 4, 1, 1)
        grid_larm.addWidget(self.bt_L4, 1, 2, 1, 1)
        grid_larm.addWidget(self.bt_L5, 2, 2, 1, 1)
        grid_larm.addWidget(self.bt_L6, 3, 2, 1, 1)
        grid_larm.addWidget(self.bt_LF1, 4, 0, 1, 1)
        grid_larm.addWidget(self.bt_LF2, 4, 1, 1, 1)
        grid_larm.addWidget(self.bt_LF3, 4, 2, 1, 1)
        grid_larm.addWidget(self.bt_LF4, 4, 3, 1, 1)
        grid_larm.addWidget(self.bt_LF5, 4, 4, 1, 1)

        h1rightbox.addLayout(grid_larm)
        h1rightbox.setSpacing(20)

        grid_rarm = QGridLayout()
        grid_rarm.setSpacing(5)

        self.bt_R1 = QPushButton("R1")
        self.bt_R2 = QPushButton("R2")
        self.bt_R3 = QPushButton("R3")
        self.bt_R4 = QPushButton("R4")
        self.bt_R5 = QPushButton("R5")
        self.bt_R6 = QPushButton("R6")
        self.bt_RF1 = QPushButton("RF1")
        self.bt_RF2 = QPushButton("RF2")
        self.bt_RF3 = QPushButton("RF3")
        self.bt_RF4 = QPushButton("RF4")
        self.bt_RF5 = QPushButton("RF5")

        grid_rarm.addWidget(self.bt_R1, 0, 0, 1, 1)
        grid_rarm.addWidget(self.bt_R2, 0, 1, 1, 1)
        grid_rarm.addWidget(self.bt_R3, 0, 2, 1, 1)
        grid_rarm.addWidget(self.bt_R4, 1, 2, 1, 1)
        grid_rarm.addWidget(self.bt_R5, 2, 2, 1, 1)
        grid_rarm.addWidget(self.bt_R6, 3, 2, 1, 1)
        grid_rarm.addWidget(self.bt_RF1, 4, 0, 1, 1)
        grid_rarm.addWidget(self.bt_RF2, 4, 1, 1, 1)
        grid_rarm.addWidget(self.bt_RF3, 4, 2, 1, 1)
        grid_rarm.addWidget(self.bt_RF4, 4, 3, 1, 1)
        grid_rarm.addWidget(self.bt_RF5, 4, 4, 1, 1)

        h1rightbox.addLayout(grid_rarm)

        vrightbox.addLayout(h1rightbox)

        h2rightbox = QHBoxLayout()

        grid_dg = QGridLayout()

        self.bt_forward = QPushButton("前进", self)
        self.bt_back = QPushButton("后退", self)
        self.bt_left = QPushButton("左转", self)
        self.bt_right = QPushButton("右转", self)

        grid_dg.addWidget(self.bt_forward, 0, 1)
        grid_dg.addWidget(self.bt_left, 1, 0)
        grid_dg.addWidget(self.bt_right, 1, 2)
        grid_dg.addWidget(self.bt_back, 2, 1)

        h2rightbox.addLayout(grid_dg)

        grid_reset = QGridLayout()

        self.bt_stop = QPushButton("底盘停止")
        self.bt_reset = QPushButton("机器人复位")

        grid_reset.addWidget(self.bt_stop, 0, 1)
        grid_reset.addWidget(self.bt_reset, 1, 1)

        h2rightbox.addLayout(grid_reset)

        vrightbox.addLayout(h2rightbox)

        label_log = QLabel("操作日志:")

        vrightbox.addWidget(label_log)

        self.browser_log = QTextBrowser()
        vrightbox.addWidget(self.browser_log)

        hallbox = QHBoxLayout()

        hallbox.addLayout(vleftbox)
        hallbox.addLayout(vrightbox)
        hallbox.setStretchFactor(vleftbox, 10)
        hallbox.setStretchFactor(vrightbox, 1)

        self.tab_robot.setLayout(hallbox)

    def init_sensor_UI(self):
        hallbox = QHBoxLayout()

        self.tab_sensor.setLayout(hallbox)

    ###############################################################
    # 定义UI的有关函数

    # 让窗口在屏幕正中间
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # display to the center
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 关闭提示
    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            # if self.cap.isOpened():
            #     self.cap.release()
            # if self.timer_camera.isActive():
            #     self.timer_camera.stop()
            event.accept()

    ###############################################################

    ###############################################################
    # 定义按键事件绑定和具体操纵功能
    ###############################################################
    # 用于定义按键事件绑定
    def set_event(self):

        # 绑定机械臂事件
        self.bt_L1.clicked.connect(lambda: self.arm_control("L1"))
        self.bt_L2.clicked.connect(lambda: self.arm_control("L2"))
        self.bt_L3.clicked.connect(lambda: self.arm_control("L3"))
        self.bt_L4.clicked.connect(lambda: self.arm_control("L4"))
        self.bt_L5.clicked.connect(lambda: self.arm_control("L5"))
        self.bt_L6.clicked.connect(lambda: self.arm_control("L6"))
        self.bt_LF1.clicked.connect(lambda: self.arm_control("LF1"))
        self.bt_LF2.clicked.connect(lambda: self.arm_control("LF2"))
        self.bt_LF3.clicked.connect(lambda: self.arm_control("LF3"))
        self.bt_LF4.clicked.connect(lambda: self.arm_control("LF4"))
        self.bt_LF5.clicked.connect(lambda: self.arm_control("LF5"))

        self.bt_R1.clicked.connect(lambda: self.arm_control("R1"))
        self.bt_R2.clicked.connect(lambda: self.arm_control("R2"))
        self.bt_R3.clicked.connect(lambda: self.arm_control("R3"))
        self.bt_R4.clicked.connect(lambda: self.arm_control("R4"))
        self.bt_R5.clicked.connect(lambda: self.arm_control("R5"))
        self.bt_R6.clicked.connect(lambda: self.arm_control("R6"))
        self.bt_RF1.clicked.connect(lambda: self.arm_control("RF1"))
        self.bt_RF2.clicked.connect(lambda: self.arm_control("RF2"))
        self.bt_RF3.clicked.connect(lambda: self.arm_control("RF3"))
        self.bt_RF4.clicked.connect(lambda: self.arm_control("RF4"))
        self.bt_RF5.clicked.connect(lambda: self.arm_control("RF5"))

      #   self.bt_stop.clicked.connect(lambda: self.dg_stop())
        self.bt_reset.clicked.connect(lambda: self.reset_robot())


    # 定义具体操纵功能


    def arm_control(self, num):
        self.action_seq[arm[num]] += self.add_angle
        self.arm.CMD_SERVO_MOVE(self.action_seq)
        tempstr = ""
        for key, value in self.action_seq.items():
            tempstr = tempstr + re_arm[key] + ":" + str(value) + ","

        self.browser_log.append(tempstr)

    def reset_robot(self):
        self.arm.CMD_reset()
        self.action_seq = deepcopy(defaultAction)

        self.browser_log.append("复位")



    ###############################################################




if __name__ == "__main__":

    robot_serialname = "COM5"
    # robot_serialname = "/dev/tty.usbserial-1460"


    app = QApplication(sys.argv)
    con = Controller(robot_serialname=robot_serialname)
    sys.exit(app.exec_())
