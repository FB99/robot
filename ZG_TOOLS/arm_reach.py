"""
类中包含属性：抓手的几何参数，各关节长度

包含方法：
1，坐标转换及长度计算
2，利用opencv库或是姿势评估模型 获取目标点位置
3，利用坐标转换及长度计算 算出当前抓手的手指位置
4，计算当前位置和目标点位置的欧式距离，作为reward，返回给主程序
"""
import numpy as np
from PIL import Image
import shutil

class Arm_Reach():
    def angle2tip
    def get_distance(self):
        
    def xyz2trz
    def trz2xyz
