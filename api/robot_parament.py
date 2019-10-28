#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: robot_parament.py
@time: 2018/3/26 下午6:45
@description:
'''



# 600~2400代表0~180



# arm编号与命令的对应字典
arm = {"R1": '0D', "R2": '0E',"R3": '0F', "R4": '18', "R5": '19', "R6": '1A',
       "RF1": '1F', "RF2": '1E',"RF3": '1D', "RF4": '1C', "RF5": '1B',
       "L1": '0C', "L2": '0B', "L3": '0A', "L4": '07', "L5": '06', "L6": '05',
       "LF1": '00', "LF2": '01', "LF3": '02', "LF4": '03', "LF5": '04'}




re_arm = {"0D":"R1","0E":"R2","0F":"R3","18":"R4","19":"R5","1A":"R6",
          "1F":"RF1","1E":"RF2","1D":"RF3","1C":"RF4","1B":"RF5",
          "0C":"L1","0B":"L2","0A":"L3","07":"L4","06":"L5","05":"L6",
          "00":"LF1","01":"LF2","02":"LF3","03":"LF4","04":"LF5",
}


armDefault = {"R1": 40, "R2": 140, "R3": 90, "R4": 140, "R5": 90, "R6": 90,
              "RF1": 140, "RF2": 140, "RF3": 140, "RF4": 40, "RF5": 40,
              "L1": 140, "L2": 40, "L3": 90, "L4": 40, "L5": 90, "L6": 90,
              "LF1": 40, "LF2": 40, "LF3": 40, "LF4": 140, "LF5": 140
              }



#全部都有位姿的，按照右臂、右手，左臂，左手，顺序调整
allmove_seq = ['0D', '0E', '0F', '18', '19', '1A', '1F', '1E', '1D', '1C', '1B',
             '0C', '0B', '0A', '07', '06', '05', '00', '01', '02', '03', '04']

defaultAction = {'0D': 40, '0E': 140, '0F': 90, '18': 140, '19': 90, '1A': 90,
                 '1F': 140, '1E': 140, '1D': 140, '1C': 40, '1B': 40,
                '0C': 140, '0B': 40, '0A': 90, '07': 40, '06': 90, '05': 90,
                 '00': 40, '01': 40, '02': 40, '03': 140, '04': 140}



# 5555470316D00707E80306DC0505DC050CD0070BE8030ADC051ADC0518D00719DC050ED0070FDC050DE80303D00704D0071CE8031BE8031ED0071DD00701E8031FD00702E80300E803

reset_cmd = "5555470316D00707E80306DC0505DC050CD0070BE8030ADC051ADC0518D00719DC050ED0070FDC050DE80303D00704D0071CE8031BE8031ED0071DD00701E8031FD00702E80300E803"




# 加一个angle必须要在一位小数的约束。0.3度的控制
def angle2pwm(angle):
    pwm = int(angle * 10) + 600
    return pwm

# 角度转成16进制命令
def angle2cmd_hex(angle):
    return cmd2cmd_hex(angle2pwm(angle))

# 数转成16进制命令
def number2cmd_hex(number):
    if number < 16:
        return "0"+str(hex(number))[2:3].upper()
    else:
        return str(hex(number))[2:].upper()

# 命令转成16进制命令
def cmd2cmd_hex(number):
    tempstr = str(hex(number)[2:]).upper().zfill(4)  # 用0补齐4位
    low_eight = tempstr[2:]
    high_eight = tempstr[:2]
    return low_eight, high_eight




