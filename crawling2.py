from unittest import result
import urllib.request
from bs4 import BeautifulSoup
url = urllib.request.urlopen('https://www.instagram.com/')
html = url.read()
문자열 = html.decode()



soup = BeautifulSoup(문자열,'html.parser')
tag = soup.find('title')
result = tag.text.strip()

print(result)