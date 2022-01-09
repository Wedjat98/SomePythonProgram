import urllib.request
import urllib.error  # 指点URL 获取网页数据
import urllib.parse
from bs4 import BeautifulSoup  # 网页解析和获取数据
import sqlite3  # SQLite数据库操作
from datetime import datetime


def getData(baseurl):
    dataList = []
    html = askUrl(baseurl)
    bs = BeautifulSoup(html, "html.parser")

    t_list1 = bs.select("html > body > div > div > main > div > div > div >  div > div > a > div.c-single-text-ellipsis")
    for item in t_list1:
        dataList.append(item.getText())
    return dataList


def saveData2DB(dataList, dbpath):
    dt = datetime.now()
    init_db(dbpath)
    for index in range(len(dataList)):
        dataList[index] = '\"' + dataList[index] + '\"'
        sql = "insert into rankTop_"+datetime_toString(dt)+" (title) values (" + dataList[index] + ")"
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    dt = datetime.now()
    sql = "create table rankTop_%s (id integer primary key autoincrement, title varchar(50) not null ) " % datetime_toString(dt)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def datetime_toString(dt):
    return dt.strftime("%Y%m%d%H%M")


def askUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0(Windows NT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/"
                      "97.0.4692.71Safari/537.36Edg/97.0.1072.55 "
    }

    request = urllib.request.Request(url)
    request.add_header('Referer', 'https://baidu.com/')
    request.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                     "like Gecko) Chrome/97.0.4692.71 Safari/537.36")
    # request.add_header('cookie', "login_sid_t=e81b55d664c5d9b9853a4de850ef6bc2; cross_origin_proto=SSL; _s_tentry=-; "
    #                              "Apache=7651911694974.564.1641718410361; SINAGLOBAL=7651911694974.564.1641718410361; "
    #                              "ULV=1641718410368:1:1:1:7651911694974.564.1641718410361:; "
    #                              "SUB=_2AkMWhi2gf8NxqwJRmP4QzmPqa4twywzEieKg2tx7JRMxHRl"
    #                              "-yT92qlwHtRB6PQYDT6Ze9YWS5Sa8V6N4YKybe42fe0d-; "
    #                              "SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5n3sNiHR.WR.x.ZErwK5Y_")
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def main():
    baseurl = "https://top.baidu.com/board?tab=realtime"
    dbpath = "bdTopRank.db"
    dataList = getData(baseurl)
    saveData2DB(dataList, dbpath)


if __name__ == "__main__":
    main()
    print("Done!")
