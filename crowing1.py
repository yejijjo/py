import urllib.request
url = urllib.request.urlopen('https://www.naver.com/')
html = url.read()
문자열 = html.decode()

print(문자열)
