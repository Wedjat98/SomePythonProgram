from bs4 import BeautifulSoup

file = open("./demo.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

t_list = bs.select("html > body > div > div > div > div > div > table > tbody > tr > td > a")
t_list2 = bs.select("html > body > div > div > div > div > div > table > tbody > tr > td.td-01.ranktop ")

for item in t_list2:
    # print(item)
    print(item.getText())

#
# def name_is_exists(tag):
#     return tag.has_attr("target")
