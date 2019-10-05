# ---------------------------
# @description 闭包
# @author xichengxml
# @date 2019/10/5 下午 02:01
# ---------------------------


# 对比普通函数定义和闭包
def function01(a, b):
    return a + b


def function02(a):
    def add(b):
        return a + b

    return add


print(function01(1, 1))
print(function02(1)(1))
print("--")


# 使用闭包实现一个计数器
def counter(init_value=0):
    cnt = [init_value]

    def add():
        cnt[0] += 1
        return cnt[0]

    return add


counter5 = counter(5)
counter10 = counter(10)

print(counter5())
print(counter5())
print(counter5())
print("--")
print(counter10())
print(counter10())
