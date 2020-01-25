# ---------------------------
# @description 自定义with
# @author xichengxml
# @date 2019/10/5 下午 09:55
# ---------------------------


class WithDemo:
    def __enter__(self):
        print("enter....")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("exit...")
            print("--------------------")
        else:
            print("error: %s" % exc_tb)


# 无异常情况
with WithDemo():
    print("with demo is running")

# 有异常情况
with WithDemo():
    print("with demo is running")
    raise NameError("my name error")
