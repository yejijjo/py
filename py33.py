변수명1 = 0     #정수
print(변수명1)
변수명2 = 3.14  #실수
print(변수명2)
변수명3 = '33-14' #글자
print(변수명3)
변수명4 = [] #리스트
변수명4 = [1,2,3,4,'1234']
print(변수명4)
변수명5 = () #튜플
변수명5 = (1,2,3,4,'1234') #튜플 #수정불가
print(변수명5)
변수명6 = {1,2,3,4,'1234',1,2,3,4} #세트 #중복불가
print(변수명6)
변수명7 = {1:'첫번째',2:'두번째','word':'단어'}
print(변수명7)

변수명4.append('56')
print(변수명4)

for 임시1 in 변수명4:
    print(임시1)

for 임시2 in 변수명7:
    print(임시2)
    print(변수명7.get(임시2))