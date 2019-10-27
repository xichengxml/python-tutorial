from bs4 import BeautifulSoup
import requests
import os
import time
import random
import shutil

# ---------------------------
# @description 爬取一些图片
# @author xichengxml
# @date 2019/10/27 上午 08:27
# ---------------------------

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_topbarnewsshow=1; _ntes_nuid=e260d97b09c0d0a2eefd8148de5a86e0; "
              "mail_psc_fingerprint=fca70241966414031d1d683aec7afc4f; __oc_uuid=ed6d5f30-3130-11e9-bc28-279757043bdf;"
              "utma=187553192.1684249026.1550242210.1550242210.1550288838.2; __"
              "gads=ID=3322dd1b43b7b056:T=1553931701:S=ALNI_Ma5-5sOn404gFueJUB_bKkTwDwXzA; "
              "usertrack=CrGYY11pmHuR5wjoAwQqAg==; _ntes_nnid=e260d97b09c0d0a2eefd8148de5a86e0,1568421670762; "
              "vinfo_n_f_l_n3=ddc8cb6d4f109453.1.12.1553928568543.1568421673782.1568451901141; "
              "P_INFO=xichengxml@163.com|1570953186|0|mail163|00&99|bej&1570891217&mail_"
              "client#bej&null#10#0#0|&0|youdaodict_client|xichengxml@163.com; nts_mail_user=xichengxml@163.com:-1:1; _"
              "nietop_foot=%u9634%u9633%u5E08%7Cyys.163.com; topbarnewsshow=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/78.0.3904.70 Safari/537.36"
}

url = "https://yys.163.com/media/picture.html"

response = requests.get(url, headers=headers)
html_page = BeautifulSoup(response.text, "lxml")
# print(html_page.prettify())


def get_image():
    for image in html_page.find_all("div", class_="cover"):
        # print(image.a)
        # print(image.a.text)
        # 只下载1920 * 1080的图片
        if image.a.text == "1080x1920":
            image_url = image.a.get("href")
            # print(image_url)
            # 获取图片名称，图片名称都一样，自己根据时间戳命名
            # print(os.path.basename(image_url))
            image_name = time.strftime('%Y%m%d%H%M%S') + random.randint(10000, 99999).__str__() + ".jpg"
            # 获取当前路径
            image_dir = os.path.abspath('.') + "\image"
            # print(image_dir)
            # print(image_name)
            file_name = os.path.join(image_dir, image_name)
            print("开始下载: %s" % image_name)
            download(image_url, file_name)


def download(image_url, local_file):
    image_resp = requests.get(image_url, stream=True)
    if image_resp.status_code == 200:
        with open(local_file, "wb") as f:
            image_resp.raw.decode_content=True
            shutil.copyfileobj(image_resp.raw, f)


get_image()

