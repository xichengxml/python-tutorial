# ---------------------------
# @description 迭代器
# @author xichengxml
# @date 2019/10/5 下午 07:56
# ---------------------------

list_a = [1, 2, 3, 4, 5]
iterator = iter(list_a)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except Exception as e:
    print(e)

# 可以使用迭代器的才可以使用for-each，和java相同
for i in list_a:
    print(i)
