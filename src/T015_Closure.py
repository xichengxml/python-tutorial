# ---------------------------
# @description 闭包的使用
# @author xichegnxml
# @date 2019/10/5 下午 02:16
# ---------------------------


# y = a * x + b 直线生成器
def line_gen(a, b):
    def line_gen_closure(x):
        return a * x + b

    return line_gen_closure
    # 可以简写为
    # return lambda x: a * x + b


line_gen_01 = line_gen(5, 10)
print(line_gen_01(10))
print(line_gen_01(20))
