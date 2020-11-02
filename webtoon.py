import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()     # 혹시 문제있으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

"""
*** 웹 페이지에 대해서 잘 알 때 사용 ***

print(soup.title)
  # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
  
print(soup.title.get_text())
  # 네이버 만화 > 요일별  웹툰 > 전체웹툰
  
print(soup.a)           # soup 객체에서 처음 발견되는 a element 출력
  # <a href="#menu" onclick="document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"><span>메인 메뉴로 바로가기</span></a>

print(soup.a.attrs)     # a element 의 속성 정보를 출력
  # {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}

print(soup.a["href"])     # a element 의 href 속성 '값' 정보를 출력
  # #menu
"""

"""
print(soup.find("a", attrs={"class":"Nbtn_upload"}))     # class = "Nbtn_upload" 인 a element 를 찾아줘
  # <a class="Nbtn_upload" href="/mypage/myActivity.nhn" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
print(soup.find(attrs={"class":"Nbtn_upload"}))          # class = "Nbtn_upload" 인 어떤 element 를 찾아줘
  # 위와 결과 동일
"""

"""
# print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})

(1)
print(rank1.a)
print(rank1.a.get_text())
print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling)

rank2 = rank1.next_sibling.next_sibling
print(rank2.a.get_text())
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)

(2)
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

(3)
print(rank1.find_next_siblings("li"))
"""

"""
webtoon = soup.find("a", text="바른연애 길잡이-123")
print(webtoon)
"""

# 네이버 웹튼 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})

# class 속성이 title 인 a element 인 모든 element 를 반환
for cartoon in cartoons:
    print(cartoon.get_text())
