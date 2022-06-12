from unittest import result

from bitarray import bitarray


string  = 'Hello Python'

# find = 문자 시작위치 찾기
idx = string.find('Python') 
print(idx)

# replace = 글자 바꾸기
result = string.replace('Python','World')
print(result)


s = 'Life is too short'
print(s.replace('short','long'))

s = '010-2345-6789'
print(s.replace('-',' '))

while True:
    p = input('하이픈을 포함하여 주민등록번호 전체를 입력하세요>>>')
    if p.find('-') != 6:
        print('하이픈의 위치가 잘못되었습니다.')
        continue
    생일 = p.split('-')[0]
    print('생년월일은 {}입니다.'.format(생일))
    break