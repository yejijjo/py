# num = 0
# while True:
#     num += 1
#     if(num > 5):
#         break
#     print(num)

# for num in range(10):
#     if (num % 2) == 1:
#         continue
#     print(num)


from itertools import count


while True:
    city = input('대한민국의 수도는 어디인가요? >>>')
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다')
        break
    else:
        print('오답입니다. 다시 시도하세요')


hobbies = []
while True:
    hobby = input('취미를 입력하세요(종료는 그냥 엔터 >>>')
    if hobby == '':
        break
    else:
        hobbies.append(hobby) 
print(hobbies)


fruits = ['사과','감귤']
count = 3
while count > 0:
    fruit = input('과일을 입력하세요>>>')
    if fruit == '사과' or fruit == '감귤':
        print('동일한 과일이 있습니다')
        continue
    fruits.append(fruit)
    count -= 1
    print('입력이 {}번 남았습니다'.format(count))
print('입력된 과일은 {}입니다'.format(fruits))

