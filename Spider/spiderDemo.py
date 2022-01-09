# coding=utf-8
import urllib.error  # 指点URL 获取网页数据
import urllib.parse
import urllib.request
import bs4  # 网页解析和获取数据
import re  # 正则表达式，进行文字匹配
import xlwt  # 进行excel操作
import sqlite3  # SQLite数据库操作


def main(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}  # header 字典形式
    # 选择代码  ctrl + 鼠标左键 查看变量或者函数或者类的定义
    if "get" in url:
        request = urllib.request.Request(url, headers=headers)  # 发送请求
        # 也可以通过调用Request.add_header()  添加/修改一个特定的  header
        request.add_header("Connection", "keep-alive")  # 一直活着
    elif "post" in url:
        data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
        request = urllib.request.Request(url, headers=headers, data=data)  # 发送请求
    else:
        request = urllib.request.Request(url, headers=headers)  # 发送请求
    response = ""
    try:
        response = urllib.request.urlopen(request, timeout=5)  # 打开请求 超时5s
        print(response.read().decode("utf-8"))  # 读取数据,二进制解码为utf-8
    except urllib.error.URLError:
        print("Time Out!")  # 超时处理
    finally:
        print(response.code)  # 可以查看相应状态码
        print(response.getheaders())


# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# resp = urllib.request.urlopen("http://httpbin.org/post", data=data)
# resp = urllib.request.urlopen(url)


if __name__ == "__main__":  # 当前程序执行调用函数
    url1 = "http://httpbin.org/get"
    url2 = "http://httpbin.org/post"
    url3 = "http://douban.com"
    # main(url1)
    # main(url2)
    main(url3)
    # print(main(url1))  # decode("utf-8")
    # print(main(url2).decode("utf-8"))  # decode("utf-8")  二进制解码为utf-8
