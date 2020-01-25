from threading import Thread, current_thread
import time
import random
from queue import Queue

# ---------------------------
# @description 生产者消费者问题
# @author xichengxml
# @date 2019/10/5 下午 10:40
# ---------------------------


# 定义队列长度为5
queue = Queue(5)


# 生产者线程
class ProducerThread(Thread):
    def run(self):
        num_list = range(100)
        # 从列表中选择一个数字入队
        while True:
            enqueue = random.choice(num_list)
            # global queue
            queue.put(enqueue)
            print('thread name: %s, enqueue: %s' % (current_thread().getName(), enqueue))
            # 随机睡眠1~3秒
            time.sleep(random.randint(1, 3))

            # 获取队列长度，判断队列满
            qsize = queue.qsize()
            if qsize >= 5:
                print("queue full, size: %s" % qsize)


class ConsumerThread(Thread):
    def run(self):
        # global queue
        while True:
            dequeue = queue.get()
            queue.task_done()
            print("thread name: %s, dequeue: %s" % (current_thread().getName(), dequeue))
            # 随机睡眠1~5秒
            time.sleep(random.randint(1, 5))

            # 获取队列长度，判断队列空
            qsize = queue.qsize()
            if qsize <= 0:
                print("queue empty, size: %s" % qsize)


# 多生产者，模拟队列满的情况
ProducerThread(name='p1').start()
ProducerThread(name='p2').start()
ProducerThread(name='p3').start()

ConsumerThread(name='c1').start()


