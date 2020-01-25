from urllib import request, parse

# ---------------------------
# @description 自定义请求头
# @author xichengxml
# @date 2019/10/13 下午 10:51
# ---------------------------

url = "http://www.httpbin.org/post"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie":
        "gauges_unique_hour=1; _gauges_unique_day=1; gauges_unique_month=1; gauges_unique_year=1; gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
        "like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
}
value = {
    'name': 'value'
}

data = bytes(parse.urlencode(value), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf8'))




