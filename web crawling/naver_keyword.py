#1. 네이버 메인 페이지에서 실시간 급등 검색어를 수집하는 프로그램

# 네이버 접속
import requests
response = requests.get("https://www.naver.com")

if response.status_code != requests.codes.ok:
    print("접속 실패")
    exit()

# 데이터를 파싱
from bs4 import BeautifulSoup

html = BeautifulSoup(response.text, "html.parser")

a_tags = html.select(".ah_list .ah_a")

for a in a_tags:
    link = a.attrs['href']
    rank = a.select_one('.ah_r')
    keyword = a.select_one('.ah_k')
    print(rank.text, keyword.text, link)