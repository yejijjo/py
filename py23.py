# from time import sleep

# import time

# 기준점 = 2
# while 기준점<12:
#     time.sleep(1)
#     print('안녕하세요')
#     기준점 += 1
# print('프로그램 종료')

# num = 1
# while num < 11:
#     print(num,'번 했습니다')
#     num += 1

# n = 10
# while n >= 1:
#     print(n)
#     n -= 1

# 정수 = int(input('정수를 입력하세요>>>'))
# if 정수 <=0:
#     print('잘못된 입력입니다')
# for 정수 in range(정수):
#     print(정수+1,'번째 Hello')

n = 1
while n <= 14:
    print(n*7)
    n += 1

for n in range(100):
    if n % 7 == 0:
        print(n+1)


dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print('{}x{}={}'.format(dan,n,dan*n))
        n += 1
    dan += 1
    