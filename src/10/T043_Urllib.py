from urllib import request

# ---------------------------
# @description 
# @author xichengxml
# @date 2019/10/9 下午 11:04
# ---------------------------


url = "http://www.baidu.com"
response = request.urlopen(url, timeout=1)
print(response.read().decode('utf-8'))
