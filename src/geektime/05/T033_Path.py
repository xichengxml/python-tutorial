import os
from pathlib import Path

# ---------------------------
# @description 文件和路径
# https://docs.python.org/3.6/library/os.path.html
# https://docs.python.org/3.6/library/pathlib.html
# @author xichengxml
# @date 2019/10/6 上午 10:38
# ---------------------------

# 当前路径的绝对路径
print(os.path.abspath('.'))
# 上一级路径的绝对路径
print(os.path.abspath('..'))
print(os.path.isdir('/users'))
print(os.path.join('/a/b', '/c/d'))

path = Path('.')
print(path.resolve())
q = Path('/tmp/a/b')
Path.mkdir(q, parents=True)

