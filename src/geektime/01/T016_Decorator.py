import time

# ---------------------------
# @description 装饰器，类似于java中的aop
# @author xichengxml
# @date 2019/10/5 下午 02:24
# ---------------------------


def decorator_timer(func):
    def decorator_timer_closure():
        start_time = time.time()
        func()
        print("function run time: %s" % (time.time() - start_time))

    return decorator_timer_closure


@decorator_timer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()
