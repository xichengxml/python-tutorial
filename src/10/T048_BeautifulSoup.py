from bs4 import BeautifulSoup

# ---------------------------
# @description BeautifulSoup的安装和使用
# pip3 install bs4 -i https://pypi.douban.com/simple
# pip3 install lxml -i https://pypi.douban.com/simple
# @author xichengxml
# @date 2019/10/26 下午 06:03
# ---------------------------


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_page = BeautifulSoup(html_doc, "lxml")
# 美化网页展示
# print(html_page.prettify())

# 获取标题
print(html_page.title)
# 获取标题内容
print(html_page.title.string)

print("------------------------")
# 获取第一个p标签
print(html_page.p)
# 获取第一个p标签的class名称
print(html_page.p['class'])
# 获取所有的p标签
print(html_page.find_all("p"))

print("-------------------------")
# 获取指定id的标签
print(html_page.find(id="link3"))
# 获取所有指定class名称的标签
print(html_page.find_all(class_="story"))

print("-------------------------")
# 找到所有a标签的链接
for link in html_page.find_all("a"):
    print(link.get("href"))



