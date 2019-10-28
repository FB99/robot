#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: angleListDemo.py
@time: 2018/11/1 2:10 PM
@description:
'''
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


# [95.0, 59.471220634490692, 58.570434385161491, 82.923264590375027, 121.42956561483852, 90.0]
# [95.0, 59.471220634490692, 59.48976259388445, 74.165166486898499, 120.51023740611555, 90.0]
# [50.0, -0.89339464913091149, 59.48976259388445, 74.165166486898499, 120.51023740611555, 90.0]
# [50.0, -0.89339464913091149, 61.032339353935967, 79.460868900273624, 118.96766064606403, 90.0]


'''
acts =[[85, 159, 56, 78, 124, 90],
        [90, 159, 59, 98, 121, 90]
       #[40, 179, 60, 74, 120, 90],
       #[40, 179, 63, 83, 117, 90]
       ]
'''
acts = []
acts.append([40, 140, 0, 140, 180, 90])
p = np.array([100,0, -200])
#actual x 反向  y -330 z 反向
# [100,0,-200]  [100,0,-100] 
# [100,-165,-100] wrong 后方  [150,-165,-150] 右边水平
# [100,-215,-100]  输出  [-100. -115.  100.]  [50,-215,-150]
# [100, -215, -130]  向左  
# np.piacts.append(get_bag(p))
ANGLE = get_bag(p)
#print('ang:', ANGLE)
#ANGLE = [119, 160, 10, 29, 90, 90]
#q1 range[-10,200] 向前角度增大   初始值40  145 = 90 degree naturally
#q2 range[10,160] 向内角度增大  初始值140  30 = 90 degeree naturally
#q3 range[-20,200] 从上往下看，顺时针方向角度增大 初始值90  -10, 190 = 90 degree
#q4 range[10，200]   向后角度增大  初始值140   40 = 90 degree
#q5 range[-20,200] 从上往下看，顺时针方向角度增大   初始值 90
#q6 range[-20,150] 往内角度增大  初始值 90
acts.append(ANGLE)
# acts.append(ANGLE)
# R = np.transpose(np.array([[-np.sqrt(2) / 2, -2 / 3, np.sqrt(3) / 3],
#               [0, 1 / 3, np.sqrt(3) / 3],
#               [np.sqrt(2) / 2, -2 / 3, np.sqrt(3) / 3]]))
# acts.append(cal_roll_agl(p, R))

# p = np.array([150, -50, -100])
# R = np.transpose(np.array([[-np.sqrt(2) / 2, 0, np.sqrt(2) / 2],
#               [np.sqrt(6) / 6, -np.sqrt(6) / 3, np.sqrt(6) / 6],
#               [np.sqrt(3) / 3, np.sqrt(3) / 3, np.sqrt(3) / 3]]))

# p = np.array([170, 5, 0])
# R = np.transpose(np.array([[0, 0, 1],
#                            [0, -1, 0],
#                            [0, -1, 0]]))
# acts.append(cal_roll_agl(p, R))
# p = np.array([250, 0, -100])
# R = np.transpose(np.array([[0, -np.sqrt(2) / 2, -np.sqrt(2) / 2],
#                            [0, np.sqrt(2) / 2, -np.sqrt(2) / 2],
#                            [1, 0, 0]]))
# acts.append(cal_roll_agl(p, R))

acts.append([40, 140, 90, 140, 90, 90])
for act in acts:
    print(act)
armID = [arm["R1"], arm["R2"], arm["R3"], arm["R4"], arm["R5"], arm["R6"]]

print("#################")
print(acts)
print("#################")
for act in acts:
    print(act)
    ID_angle = dict(zip(armID, act))
    print(ID_angle)
    arm_controler.CMD_SERVO_MOVE(ID_angle)
    time.sleep(5)
    #arm_controler.CMD_reset()
    
arm_controler.CMD_reset()

