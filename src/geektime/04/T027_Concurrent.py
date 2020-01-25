import threading
from threading import current_thread
import time

# ---------------------------
# @description 线程
# @author xichengxml
# @date 2019/10/5 下午 10:29
# ---------------------------


class MyTask(threading.Thread):

    def __init__(self, run_time):
        threading.Thread.__init__(self)
        self.run_time = run_time

    def run(self):
        print(current_thread().getName() + " start")
        time.sleep(self.run_time)
        print(current_thread().getName() + " stop")


task01 = MyTask(1)
task02 = MyTask(2)
task01.start()
task02.start()
# 主线程等待子线程执行完毕后再退出，对比task01和task02的打印顺序
task01.join()

print(current_thread().getName() + " end")
