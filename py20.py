if True:
    print('맞습니다')


age = input('당신의 나이는 몇살입니까?')
if age >= 20:
    print('당신은 성인입니다')
elif age < 20:
    print('당신은 청소년입니다')
elif age >0 and age <= 13:
    print('어린이 입니다')
else:
    print('?')


체온 = float(input('온도를 입력해주세요'))
if 체온 < 35.0:
    print('저체온증!! 얼른 119에 전화하세요')
elif 체온 <= 37.5:
    print('정상 체온입니다') 
elif 체온 < 45.0:
    print('체온이 높습니다')
else:
    print('?') 
