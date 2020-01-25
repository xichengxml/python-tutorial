import numpy as np

# ---------------------------
# @description Numpy对矩阵的基本操作
# @author xichengxml
# @date 2019/10/6 下午 04:34
# ---------------------------


# 将二维数组转换为矩阵
data = [[1, 2, 3], [4, 5, 5]]
print(np.array(data))

# 定义全零矩阵
print(np.zeros((3, 5)))
# 定义全1矩阵
print(np.ones((4, 6)))
# 定义全空矩阵，由于空值计算不安全，因此会填入默认值
# 三维矩阵
print(np.empty((5, 6, 7)))