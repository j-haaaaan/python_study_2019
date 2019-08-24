# 네이버 뉴스 기사를 찾아서 화면에 출력한다.
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%A7%A8%EC%B2%B4%EC%8A%A4%ED%84%B0+%EC%9C%A0%EB%82%98%EC%9D%B4%ED%8B%B0%EB%93%9C"

import requests
data = requests.get(url)

if data.status_code != requests.codes.ok:
    print("접속 실패")
    exit()

from bs4 import BeautifulSoup
html = BeautifulSoup(data.text, "html.parser")

news_data = html.select(".type01 > li")
for news in news_data:
    title = news.select_one('._sp_each_title)')
    print(title.text)
