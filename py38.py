def 커피머신(money,pick):
    print('{}원에 {}를 선택하셨습니다'.format(money,pick))
    메뉴 = {'아메리카노':1000,'카페라떼':1500,'카푸치노':2000}
    if pick not in 메뉴:
        print('{}는 판매하지 않습니다'.format(pick))
        return money, '없는 메뉴'
    elif 메뉴[pick] > money:
        print('{}는 {}원입니다'.format(pick,메뉴[pick]))
        return money, '금액 부족'
    else:
        return money - 메뉴[pick],pick

order = input('커피를 선택하세요.(아메리카노, 카페라떼, 카푸치노)>>>')
pay = int(input('얼마를 내시나요?>>>'))

change,coffe = 커피머신(pay,order)
print('잔돈 {}원, 커피 {}'.format(change,coffe))

