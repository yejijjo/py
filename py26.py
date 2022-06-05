from time import sleep

i = 0
while True:
    # sleep(1)
    print('무한반복')
    i += 1
    if i > 5:
        break           #반복문 종료


for i in range(1, 11):
    if i % 2 == 0:
        continue        #반복문 처음으로 돌아감
    print(i)
