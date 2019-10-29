#!/usr/bin/env python
# encoding: utf-8

from api.robot_interface import *
from api.robot_parament import *
from copy import deepcopy
import time
from ZG_TOOLS.ARM_angle_cal import cal_roll_agl, cal_R, get_bag
import numpy as np

robot_serialname = "COM5"

arm_controler = ARMcontroler(robot_serialname)

action_seq = deepcopy(defaultAction)
# add_angle = 3

arm_controler.CMD_reset()

acts = []
#初始位置
acts.append([40, 140, 0, 140, 180, 90])
#p 为目标的三维坐标
p = np.array([100,0, -200])
  
# get_bag 计算到达目标点的各关节角度
ANGLE = get_bag(p)
#q1 range[-10,200] 向前角度增大   初始值40 
#q2 range[10,160] 向内角度增大  初始值140 
#q3 range[-20,200] 从上往下看，顺时针方向角度增大 初始值90 
#q4 range[10，200]   向后角度增大  初始值140   
#q5 range[-20,200] 从上往下看，顺时针方向角度增大   初始值 90
#q6 range[-20,150] 往内角度增大  初始值 90
acts.append(ANGLE)

acts.append([40, 140, 90, 140, 90, 90])
for act in acts:
    print(act)
armID = [arm["R1"], arm["R2"], arm["R3"], arm["R4"], arm["R5"], arm["R6"]]

###执行移动，将转角发送给机械手
for act in acts:
    print(act)
    ID_angle = dict(zip(armID, act))
    print(ID_angle)
    arm_controler.CMD_SERVO_MOVE(ID_angle)
    time.sleep(5)
    #arm_controler.CMD_reset()
    
arm_controler.CMD_reset()

