import re

# ---------------------------
# @description 正则表示式
# https://docs.python.org/3.6/library/re.html
# @author xichengxml
# @date 2019/10/6 上午 08:54
# ---------------------------


# 学习r的作用
print('\n x \n')
print(r'\n x \n')


# 使用分组提取日期中的年月日
pattern = re.compile(r'(\d+)-(\d+)-(\d+)')
year, month, date = pattern.match('2019-10-06').groups()
print('year: %s, month: %s, date: %s' % (year, month, date))
# 使用search不需要完全匹配，经常用于搜索
print(pattern.search('aaa2019-10-06ffff').group())


# sub可用于替换字符
print(re.sub('a', '*', 'caaata'))
