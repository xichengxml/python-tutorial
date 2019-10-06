from pandas import Series, DataFrame
import pandas as pd

# ---------------------------
# @description pandas简介
# pandas的两个核心库 Series和DataFrame
# @author xichengxml
# @date 2019/10/6 下午 04:49
# ---------------------------


data = [1, 2, 3]
# 对numpy的arange的增强，数据有index, 更便于操作
series = Series(data)
print(series)
print(series.values)
print(series.index)

# 可以做字典key的有：int float string tuple
# 不可做字典key的有: 列表， 集合。因为可变
