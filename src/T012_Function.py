from functools import reduce


# 如果是非必传参数，可以加上默认值；拥有默认值的参数应放在必传参数之后
def func01(a, c, b=2):
    print("a = %s, b = %s, c = %s" % (a, b, c))


func01(1, 3)


# 可变参数，在参数前加*即可
def multi_param(first, *others):
    print("param first: %s, params others: %s" % (first, others))
    print("param len: %s" % (1 + len(others)))


multi_param(1, 2, 3)


# 自定义步长为浮点数
def float_step_range(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in float_step_range(10, 20, 0.5):
    print(i)


# 简单函数转化为lambda表达式
# 等价于 lambda: True
def true():
    return True


# 等价于 lambda x, y: x + y
def add(x, y):
    return x + y


# 等价于lambda x: x <= (month, day)
def func(x):
    month = 12
    day = 31
    return x <= (month, day)


# 等价于lambda item: item[1]
def func2(item):
    return item[1]


# map-reduce
list_a = [1, 2, 3]
print(list(map(lambda x: x, list_a)))
list_b = [4, 5, 6]
print(list(map(lambda x, y: x + y, list_a, list_b)))

print(reduce(lambda x, y: x + y, list_a, 1))

# zip
for i in zip(list_a, list_b):
    print(i)

# 使用zip调换字典的key和value
demo_dict = {'key01': 'value01', 'key02': 'value02'}
result = list(zip(demo_dict.values(), demo_dict.keys()))
print(result)
