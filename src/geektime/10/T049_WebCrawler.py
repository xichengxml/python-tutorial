from bs4 import  BeautifulSoup
import requests

# ---------------------------
# @description 爬取infoQ新闻
# @author xichengxml
# @date 2019/10/26 下午 08:01
# ---------------------------


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'http://ifeve.com/'


def crawler():
    response = requests.get(url, headers=headers)
    html_page = BeautifulSoup(response.text, "lxml")
    # print(html_page)
    all_summary = html_page.find_all("div", class_="post")
    # print(all_summary)
    for summary in all_summary:
        # print(summary)
        print(summary.h3.a.text)


crawler()

