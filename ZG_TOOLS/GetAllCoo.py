import numpy as np

eps =0.000000001

def get_allCoo(cos_theta, p):
    # preprocess
    p = np.array(p, dtype=np.float64)
    p /= np.linalg.norm(p)
    if cos_theta > 0:
        cos_theta = -cos_theta

    all_Z = []
    all_Y = []
    all_X = []
    # 濡傛灉浜屾鏂圭▼浜屾椤圭郴鏁颁负0
    if np.abs(np.abs(p[0]) - 1) < eps:
        x = cos_theta
        #for y in range(, 0.001, 0):
        y = -np.sqrt(1 - cos_theta ** 2)
        while y < 0:
            z = np.sqrt(1 - cos_theta ** 2 - y ** 2)
            sub_Z = np.array([x, y, z])
            sub_X = np.cross(sub_Z, p)
            sub_X /= np.linalg.norm(sub_X)
            if sub_X[2] < 0 and sub_X[1] < 0:
                y += 0.001
                continue
            sub_Y = np.cross(sub_Z, sub_X)
            sub_Y /= np.linalg.norm(sub_Y)
            all_X.append(sub_X)
            all_Y.append(sub_Y)
            all_Z.append(sub_Z)
            y += 0.001
    # 濡傛灉浜屾椤圭郴鏁颁笉涓�0
    else:
        delta2 = np.sqrt((1 - p[0] ** 2) * (1 - cos_theta ** 2))
        #for x in range(, 0.001, ):
        x = p[0] * cos_theta - delta2
        while x < p[0] * cos_theta + delta2:
            delta1 = np.sqrt(delta2 ** 2 - (x - p[0] * cos_theta) ** 2)
            y = (p[1] * (cos_theta - p[0] * x) - np.abs(p[2]) * delta1) / (1 - p[0] ** 2)

            if np.abs(p[2]) < eps:
                z = -np.sqrt(1 - x ** 2 - y ** 2)
            else:
                z = (cos_theta - p[0] * x - p[1] * y) / p[2]

            sub_Z = np.array([x, y, z])
            sub_X = np.cross(sub_Z, p)
            sub_X /= np.linalg.norm(sub_X)
            if sub_X[2] < 0 and sub_X[1] < 0:
                x += 0.001
                continue
            sub_Y = np.cross(sub_Z, sub_X)
            sub_Y /= np.linalg.norm(sub_Y)
            all_X.append(sub_X)
            all_Y.append(sub_Y)
            all_Z.append(sub_Z)
            x += 0.001

    return all_X, all_Y, all_Z
