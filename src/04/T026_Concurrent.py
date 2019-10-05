import threading
from threading import current_thread

# ---------------------------
# @description 并发编程
# @author xichengxml
# @date 2019/10/5 下午 10:02
# ---------------------------


def print_info(a, b):
    print('thread name: %s, a: %s, b: %s' % (current_thread().getName(), a, b))


# 非多线程调用
for i in range(1, 6, 1):
    print_info(i, i * i)

print("-------------------")

# 多线程调用
for i in range(1, 6, 1):
    thread = threading.Thread(target=print_info, args=(i, i * i))
    thread.start()
