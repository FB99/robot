import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import cv2

def depthToCloud(depth):
    center = [239, 319]
    #depth= np.array(depth, dtype=np.float64)
    constant = 570.3
    (imh, imw) = depth.shape
    #depth[depth == 0] = np.nan
    pcloud = np.zeros((imh,imw, 3),dtype=np.int32)
    xgrid = np.dot(np.transpose([np.arange(imh)]), np.ones((1, imw))) - center[0]
    ygrid = np.dot(np.ones((imh, 1)), [np.arange(imw)]) - center[1]
    pcloud[:,:,0] = xgrid * depth / constant
    pcloud[:,:,1] = ygrid * depth / constant
    pcloud[:,:,2] = depth
    distance = np.sqrt(np.sum(pcloud **2, 2))
    return pcloud,  distance

def globalXYZ(imh, imw, depth):
    return [(imh - 239) * depth / 570.3, (imw - 319) * depth / 570.3, depth]

if __name__ == '__main__':
    depth = cv2.imread('./DP.png', -1)
    pcloud, distance = depthToCloud(depth)
    lst = []
    for p in pcloud:
        for q in p:
            if q[2] != 0:
                lst.append(q)
    lst = np.array(lst)
    print(lst.shape)
    #开始绘图
    fig=plt.figure(dpi=120)
    ax=fig.add_subplot(111,projection='3d')
    #标题
    #利用xyz的值，生成每个点的相应坐标（x,y,z）
    ax.scatter(lst[:, 0], lst[:, 1], lst[:, 2], c='b', marker='.')#, s=2, linewidth=0, alpha=1, cmap='spectral')
    #显示
    plt.show()
