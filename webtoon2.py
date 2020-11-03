import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=602910"
res = requests.get(url)
res.raise_for_status()  # 혹시 문제있으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

"""
cartoons = soup.find_all("td", attrs={"class":"title"})

1. 첫 번째 만화 제목 + 링크 가져오기
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com" + link)

2. 만화 제목 + 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)
"""

total_rates = 0

cartoons = soup.find_all("div", attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)

    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))