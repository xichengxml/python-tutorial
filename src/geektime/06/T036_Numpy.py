import numpy as np

# ---------------------------
# @description numpy的索引和切片
# @author xichengxml
# @date 2019/10/6 下午 04:42
# ---------------------------


data = np.arange(10)
print(data)
# 下标从零开始
print(data[5])
# 修改切片数据
data[5: 8] = 10

# 切片做副本，只修改副本数据，不修改原数据
data_slice = data[1: 3].copy()
data_slice[:] = 15

print(data)
print(data_slice)

