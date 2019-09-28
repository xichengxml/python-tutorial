# 以utf-8形式写入
fileName1 = "../resources/name1.txt"
file1 = open(fileName1, "w", 100, "utf-8")
file1.write("诸葛亮")
file1.close()

# 以utf-8形式读出
file2 = open(fileName1, 'r', 100, "utf-8")
print(file2.read())
file2.close()

# 以追加的方式写入
file3 = open(fileName1, 'a')
file3.write("刘备")
file3.close()

file4 = open(fileName1, 'r', 100, 'utf-8')
print(file4.readline())
file4.close()




