import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://comic.naver.com/webtoon/weekday')
html = url.read()
문자열 = html.decode()


리스트 =[]
soup = BeautifulSoup(문자열,'html.parser')
tag = soup.find_all('a', class_='title')

for i in tag:
    print(i)
    result = i.text.strip()
    리스트.append(result)

print(리스트)

for j in 리스트:
    print(j)
