import urllib.request
import urllib.error  # 指点URL 获取网页数据
import urllib.parse
from bs4 import BeautifulSoup  # 网页解析和获取数据
import sqlite3  # SQLite数据库操作
from datetime import datetime


def getData(baseurl):
    html = askUrl(baseurl)
    bs = BeautifulSoup(html, "html.parser")
    t_list1 = bs.select("# application_root > div > div > div.partnereventdisplay_EventBodyCtn_3o4SV > div.partnereventdisplay_EventBodyPosition_3lIxP > div.partnereventdisplay_EventBody_3aht- > div.partnereventdisplay_EventColumns_1PEIf.EventDetail > div.partnereventdisplay_EventDetailsDescription_2orfV > div")

    return t_list1


def datetime_toString(dt):
    return dt.strftime("%Y%m%d%H%M")


def askUrl(url):
    request = urllib.request.Request(url)
    request.add_header('Referer', 'https://steam.com/')
    request.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                     "like Gecko) Chrome/97.0.4692.71 Safari/537.36")
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def main():
    baseurl = "https://store.steampowered.com/news/app/1660280/view/5293421584000418585"
    dataList = getData(baseurl)
    print(dataList)


if __name__ == "__main__":
    main()
    print("Done!")
