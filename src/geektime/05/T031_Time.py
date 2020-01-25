import time
import datetime

# ---------------------------
# @description 时间相关库
# https://docs.python.org/3.6/library/datetime.html
# https://docs.python.org/3.6/library/time.html
# @author xichengxml
# @date 2019/10/6 上午 09:48
# ---------------------------

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H-%M-%S'))


print(datetime.datetime.now())
# 获取10分钟后的时间
print(datetime.datetime.now() + datetime.timedelta(minutes=10))
# 获取传入日期10天后的时间
print(datetime.datetime(2008, 8, 8) + datetime.timedelta(days=10))


