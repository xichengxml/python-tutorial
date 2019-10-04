# 以utf-8形式写入
fileName1 = "../resources/file_op/name1.txt"
file1 = open(fileName1, "w", encoding="utf-8")
file1.write("诸葛亮")
file1.close()

# 以utf-8形式读出
file2 = open(fileName1, 'r', encoding="utf-8")
print(file2.read())
file2.close()

# 以追加的方式写入
file3 = open(fileName1, 'a', encoding="utf-8")
file3.write("刘备")
file3.close()

file4 = open(fileName1, 'r', encoding='utf-8')
print(file4.readline())
file4.close()

# 读取所有内容
threeKingdoms = "../resources/file_op/sanguo.txt"
file5 = open(threeKingdoms, encoding="utf-8")
lines = file5.readlines()
for line in lines:
    print(line)


