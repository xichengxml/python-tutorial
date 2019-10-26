import requests
import re

# ---------------------------
# @description 使用requests和正则表达式获取网页内容
# @author xichengxml
# @date 2019/10/26 下午 04:52
# ---------------------------


content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
# print(content)

# < div class ="grid-item work-thumbnail" >
# < a href="(.*?)".*?title">(.*?)</div>
# < div class ="author" > LynnWei < / div >

# 使用非贪婪模式匹配，re.S用于去除空格
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
# 匹配两个分组，因此结果有两个
results = re.findall(pattern, content)
# print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))