# ---------------------------
# @description 上下文管理器 with
# @author xichegnxml
# @date 2019/10/5 下午 08:17
# ---------------------------


file = open('../resources/file_op/name1.txt', encoding='utf-8')
try:
    for line in file:
        print(line.strip())
except Exception as e:
    print(e)
finally:
    file.close()

# 以下写法等价于上面写法
with open('../resources/file_op/name1.txt', encoding='utf-8') as fd:
    for line in fd:
        print(line.strip())


