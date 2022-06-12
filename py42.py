# print(2**3)
# print(4**2)

# str(123) #정수 123 -> 문자열 '123'
# int('123') #문자열 '123' -> 정수 123
# float('123.0') #문자열 123.0 -> 실수 123.0

# result = eval('100-50') #정수 50
# print(result)

# 계산식 = input('계산식을 입력하세요>>>')
# result = eval(계산식)
# print(계산식 + '=' + str(result))

# abs() -> 절대값구하기

# from numpy import average


# print(abs(-5))  #절대값 구하기

# lst = [1,2,3,4,5,6,7,8,9,10]
# print(max(lst))  #최대값 구하기
# print(min(lst))  #최소값 구하기

# pi = 3.141592
# print(round(pi,2))  #소수점 둘째자리까지 반올림

# print(sum(lst)) #리스트안에 있는 값을 모두 더함
# print(len(lst)) #리스트 항목의 개수

# print(sum(lst)/len(lst))
# print(average(lst))

# enumerate = 방번호와 값을 분리 (i=방번호, j=값)

# for i, j in enumerate(lst):
#     print(i, ':', j)

일수 = [31,28,31,30,31,30,31,31,30,31,30,31]
for i, j in enumerate(일수):
    print('{}월 = {}일'.format(i+1,j))

색 = ['red','orange','yellow','green','blue','navy','purple']
for i, j in enumerate(색):
    print('무지개의 {}번째 색은 {}입니다.'.format(i+1,j))

점수 =[]

while True:
    입력 = int(input('점수 입력(입력할 점수가 없으면 음수를 아무거나 입력하세요)>>>'))
    if 입력 < 0:
        break
    else:
        점수.append(입력)

print(점수)

평균 = print(round(sum(점수)/len(점수),2))
최대 = print(max(점수))
최소 = print(min(점수))

print('평균 = {}, 최대 = {}, 최소 = {}'.format(평균,최대,최소))