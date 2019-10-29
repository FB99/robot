from .GetAllCoo import get_allCoo
import numpy as np

L1 = 170
L2 = 170
D = 165
H = 0
p1 = np.array([0, -D, -H])
orient = np.array([-1, 0, 0])
#坐标转换
def Rx(theta):
    return np.array([[1,      0,              0       ],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta),  np.cos(theta)]])
#坐标转换
def Ry(theta):
    return np.array([[ np.cos(theta), 0, np.sin(theta)],
                     [      0,        1,      0       ],
                     [-np.sin(theta), 0, np.cos(theta)]])
 #坐标转换
def Rz(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0], 
                     [np.sin(theta),  np.cos(theta), 0],
                     [     0             , 0,        1]])

def cal_R(alpha, beta, gamma):
    return np.dot(np.dot(Rx(alpha), Ry(beta)), Rz(gamma))

#弧度转角度
def arc2C(value):
  return value / np.pi * 180
#计算前三个关节转角
def get_q123(q4, R4):
    R = np.dot(R4, np.transpose(Rx(q4)))
    print(R)
    # q1 = np.arctan(R[0, 2] / R[2, 2])
    # q2 = np.arctan(-R[1, 2]/ (R[0, 2] * np.sin(q1) + R[2, 2] * np.cos(q1)))
    # q3 = np.arctan(R[1, 0] / R[1, 1])
    # return q
    def f(q,R):
        s1 = np.sin(q[0])
        c1 = np.cos(q[0])
        s2 = np.sin(q[1])
        c2 = np.cos(q[1])
        s3 = np.sin(q[2])
        c3 = np.cos(q[2])
        return [c1*c3 + s1*s2*s3 - R[0][0],
                s1*s2*c3 - c1*s3 - R[0][1],
                s1*c2 - R[0][2],
                c2*s3 - R[1][0],
                c2*c3 - R[1][1],
                -s2 - R[1][2],
                c1*s2*s3 - s1*c3 - R[2][0],
                s1*s3 + c1*s2*c3 - R[2][1],
                c1*c2 - R[2][2]]

    print(R[1][2])
    q2 = np.arcsin(-R[1][2])
    c2 = np.cos(q2)
    Q1 = [np.arcsin(R[0][2] / c2), np.pi - np.arcsin(R[0][2] / c2)]
    Q3 = [np.arcsin(R[1][0] / c2), np.pi - np.arcsin(R[1][0] / c2)]
    '''
    for q1 in Q1:
        for q3 in Q3:
            if np.sum(f([q1, q2, q3], R)) < 0.01:
                return q1, q2, q3
    '''       
    for q1 in Q1:
        for q3 in Q3:
            temp = f([q1, q2, q3], R)
            temp = np.dot(temp, np.transpose(temp))
            if np.sum(temp) < 0.01:
                return q1,q2,q3
    print("NOOOOO solution")
    return None, None, None

def get_bag(p6):
    r = p6 - p1
    C = np.linalg.norm(r)
    if C >= L1 + L2:
    	print("error 1:the position is too far")
    	return None
    cos_theta = -(L2 **2 + C ** 2 - L1 ** 2) / 2 / C / L2
    all_X, all_Y, all_Z = get_allCoo(cos_theta, r)

    cos_value = np.dot(all_Z, orient)
    idx = np.argmax(cos_value)
    
    q4 =  np.pi - np.arccos((L1 ** 2 + L2 **2 - C ** 2) / 2 / L1 / L2) 
    R4 = np.transpose([all_X[idx], all_Y[idx], all_Z[idx]])
    q1, q2, q3 = get_q123(q4, R4)
    if q1 is None:
    	print('error 2: No proper angle for q1')
    	return None
    #### check:
    Rq3 = np.dot(np.dot(Ry(q1), Rx(q2)), Rz(q3))
    Rq4 = np.dot(np.dot(np.dot(Ry(q1), Rx(q2)), Rz(q3)), Rx(q4))

    result = p1-np.array([Rq3[0][2],Rq3[1][2],Rq3[2][2]])*170-np.array([Rq4[0][2],Rq4[1][2],Rq4[2][2]])*170

    q5 = np.arctan(-R4[2, 0] / R4[2, 1])
    R5 = np.dot(R4, Rz(q5))
    q6 = np.arctan(-R5[0, 1] / R5[0, 2])
    print("q123456 as follows:")
    print([arc2C(q1),arc2C(q2),arc2C(q3),arc2C(q4),arc2C(q5),arc2C(q6)])
    #return [40 - arc2C(q1), np.clip(140 + arc2C(q2), 0, 160),  -arc2C(q3), 140 + arc2C(q4), 180 - arc2C(q5), 90 + arc2C(q6)]
    return [np.clip(transq2(40 - 1.11*arc2C(q1)),0,200), np.clip(140 + 1.11*arc2C(q2), 0, 160),  
            np.clip(transq2(0 - 1.11*arc2C(q3)),0,200), np.clip(transq2(140 - 1.11*arc2C(q4)),10,200),
             180 - 1.11*arc2C(q5), 90 + 1.11*arc2C(q6)]

#q1 range[-10,200] 向前角度增大   初始值40 
#q2 range[10,160] 向内角度增大  初始值140  
#q3 range[-20,200] 从上往下看，顺时针方向角度增大 初始值90 
#q4 range[10，200]   向后角度增大  初始值140   
#q5 range[-20,200] 从上往下看，顺时针方向角度增大   初始值 90
#q6 range[-20,150] 往内角度增大  初始值 90

def transq2(q):
    if q < 0:
        q+= 360.0
    elif q >= 360.0:
        q-= 360.0
    return q

def cal_roll_agl(p6, R6):
    r = p1 - p6
    C = np.linalg.norm(r)
    q4 = np.arccos((L1 ** 2 + L2 **2 - C ** 2) / 2 / L1 / L2) - np.pi
    q5 = 0
    q6 = 0
    R = np.dot(R6, np.transpose(Rx(q4)))
    if R[2, 2] == 0:
        q1 = -np.pi / 2
    else:
        q1 = np.arctan(R[0, 2] / R[2, 2])
    if R[0, 2] * np.sin(q1) + R[2, 2] * np.cos(q1) == 0:
        q2 = np.pi / 2
    else:
        q2 = np.arctan(-R[1, 2]/ (R[0, 2] * np.sin(q1) + R[2, 2] * np.cos(q1)))
    q3 = np.arctan(R[1, 0] / R[1, 1])
    return [40 - arc2C(q1), np.clip(140 + arc2C(q2), 0, 160),  -arc2C(q3), 140 + arc2C(q4), 180 - arc2C(q5), 90 + arc2C(q6)]


if __name__ == '__main__':

    p = np.array([170, 5, 0])
    R = np.transpose(np.array([[0, 0, 1],
                               [0, -1, 0],
                               [0, -1, 0]]))
    print(cal_roll_agl(p, R))
    p = np.array([250, 0, -100])
    R = np.transpose(np.array([[0, -np.sqrt(2) / 2, -np.sqrt(2) / 2],
                               [0, np.sqrt(2) / 2, -np.sqrt(2) / 2],
                               [1, 0, 0]]))
    print(cal_roll_agl(p, R))
