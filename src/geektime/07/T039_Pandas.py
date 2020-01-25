from pandas import Series, DataFrame
from numpy import nan

# ---------------------------
# @description DataFrame操作矩阵
# DataFrame操作多维矩阵，Series操作一维矩阵
# @author xichengxml
# @date 2019/10/7 上午 08:28
# ---------------------------


data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

print("---------以表格形式展示数据-------------")
print(DataFrame(data))

print('------排序数据 首先以city升序，city相同以year，前两个都相同以pop升序-----')
print(DataFrame(data, columns=['city', 'year', 'pop']))

print('-------可以通过.或者key的方式访问数据-----------')
frame01 = DataFrame(data)
print(frame01.year)
print(frame01['city'])

print('-------增加一列，可以增加无关列，或者根据某一列的计算值增加新列-------')
frame02 = DataFrame(data)
frame02['newColumn'] = 'newColumn'
frame02['capital'] = (frame02.city == 'beijing')
print(frame02)

print('------------矩阵转置---------------')
pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}
       }
print(DataFrame(pop).T)

'''
Series的空值NA的丢弃和填充 一维矩阵
'''
series01 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])

print('-------------重新索引，填充空值----------------')
print(series01.reindex(['a', 'b', 'c', 'd', 'e']))

print('--------重新索引，空值填充固定值0---------')
print(series01.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0))

series02 = Series(['red', 'green', 'blue'], index=[0, 2, 4])
print('------重新索引，空值填充邻近值 bfill填充后面的值，ffill填充前面的值 back front------')
print(series02.reindex(range(6), method='bfill'))

series03 = Series([1, nan, 3])
print('------------丢弃空值----------------')
print(series03.dropna())

'''
DataFrame的空值NA的丢弃和填充 多维矩阵
'''
data = [[1., 6.5, 3], [1., nan, nan], [nan, nan, nan]]
frame03 = DataFrame(data)

frame03[4] = nan
print('------------填充一列空值---------------')
print(frame03)

print('------丢弃空值 默认丢弃所有空值，含空值的行会丢弃整行-----')
print(DataFrame(data).dropna())

print('------丢弃空值，只丢弃整行为空的-------')
print(DataFrame(data).dropna(how='all'))

print('--------------填充空值-----------------')
print(DataFrame(data).fillna(0))


