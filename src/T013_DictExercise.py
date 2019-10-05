import re

file_path = '../resources/file_op/'
name_dict = {}
weapon_dict = {}


# 定义在文件中查找特定字符串的方法
def find_string_in_file(string):
    with open(file_path + 'sanguo.txt', encoding='utf-8') as three_kingdoms:
        data = three_kingdoms.read().replace('\n', '')
        string_cnt = re.findall(string, data)
    return string, len(string_cnt)


# 统计人物出现的次数
with open(file_path + 'name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            character_name, character_cnt = find_string_in_file(n)
            name_dict[character_name] = character_cnt


# 统计武器出现的次数
with open(file_path + 'weapon.txt', encoding='utf-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            weapon_name, weapon_cnt = find_string_in_file(line.strip())
            weapon_dict[weapon_name] = weapon_cnt
        i += 1


# 排序
character_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(character_sorted[0:10])

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
print(weapon_sorted[0:10])

