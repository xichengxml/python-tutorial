from pandas import Series, DataFrame

# ---------------------------
# @description Series的基本操作
# @author xichengxml
# @date 2019/10/6 下午 07:21
# ---------------------------


# 自定义索引
data = [1, 2, 3, 4]
series = Series(data, index=('a', 'b', 'c', 'd'))
print(series)
print('a' in series)
print(1 in series)
print('f' in series)


# 字典通过series转化
dict01 = {'beijing': 100000, 'shanghai': 80000, 'tianjin': 90000, 'chongqing': 70000}
s = Series(dict01)
print(s)
s.index = ('bj', 'sh', 'tj', 'cq')
print(s)



