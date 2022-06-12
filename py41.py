def 함수1():
    print('함수를 사용했습니다.')

def 함수2(number):
    print(number,'번 함수 사용')

def 함수3(number,string):
    print(number,'번 함수 사용',string)

def 함수4():
    print('함수4를 사용했습니다.')
    return '함수4' 

def 함수5(number):
    if number < 0:
        print('값은 0보다 작습니다.')
        return -1
    print('값은 0보다 큽니다.')
    return 1 

def star(num):
    print('*' * num)

star(3)
# 입력값 = int(input('숫자를 입력하세요>>>'))
# star(입력값)

def 제곱승(숫자1,숫자2):
    total = 숫자1
    for i in range(숫자2-1):
        total *= 숫자1
    print(total)

제곱승(2,3) 
