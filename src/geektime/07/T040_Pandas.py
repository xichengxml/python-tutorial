from pandas import Series, DataFrame
import numpy as np

# ---------------------------
# @description Series的层次化索引
# @author xichengxml
# @date 2019/10/7 上午 11:50
# ---------------------------


series = Series(np.random.randn(10),
                index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                       [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print('-----------------------------')
print(series)

print('----------可以通过索引访问--------')
print(series.b)

print('----------转化成二维矩阵----------')
print(series.unstack())

print('-------从二维矩阵再转回一维--------')
print(series.unstack().stack())
