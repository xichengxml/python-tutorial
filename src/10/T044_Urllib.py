from urllib import request, parse, error
import socket

# ---------------------------
# @description 使用urllib发送post和get请求
# @author xichengxml
# @date 2019/10/13 下午 10:32
# ---------------------------

# get请求
print("---------------get请求----------------")
response = request.urlopen("http://www.httpbin.org/get?a=1&b=2")
print(response.read().decode('utf-8'))


# post请求
print("---------------post请求---------------")
data = bytes(parse.urlencode({"key": "value"}), encoding='utf-8')
response2 = request.urlopen("http://www.httpbin.org/post", data=data, timeout=1)
print(response2.read())

# http请求的超时处理, 为什么www.baidu.com不行?
print('----------超时处理------------')
try:
    response3 = request.urlopen("http://httpbin.org/get", timeout=0.001)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("超时错误")


