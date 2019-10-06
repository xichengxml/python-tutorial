import numpy as np

# ---------------------------
# @description numpy入门
# @author xichengxml
# @date 2019/10/6 下午 01:27
# ---------------------------


# 根据输入类型自动转换
array01 = np.array([1, 2, 3])
print(array01)
print(array01.dtype)

array02 = np.array([1.5, 2.5, 3.5])
print(array02)
print(array02.dtype)

# 还可以累加
print(array01 + array02)

