import requests

# ---------------------------
# @description requests库学习
# pip3 install requests -i https://pypi.douban.com/simple
# @author xichengxml
# @date 2019/10/26 下午 02:24
# ---------------------------


data = {"user": "admin", "password": "123456"}

# get请求
url = "http://httpbin.org/get"
response = requests.get(url, data)
print(response.text)


# post请求
url = "http://httpbin.org/post"
response = requests.post(url, data)
print(response.text)




