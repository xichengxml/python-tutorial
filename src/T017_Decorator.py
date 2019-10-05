# ---------------------------
# @description 装饰器的使用
# @author xichegnxml
# @date 2019/10/5 下午 02:59
# ---------------------------


# 装饰器参数通过最外层传递
def tips(decorator_args):
    def tips_outer(func):
        # 函数参数通过最内层传递
        def tips_closure(func_arg_a, func_arg_b):
            print(decorator_args + "--" + func.__name__)
            func(func_arg_a, func_arg_b)

        return tips_closure

    return tips_outer


@tips("add_module")
def add(a, b):
    print(a + b)


@tips("sub_module")
def sub(a, b):
    print(a - b)


print(add(1, 3))
print(sub(1, 3))
