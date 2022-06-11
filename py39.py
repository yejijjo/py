# def vending_machine(money):
#     개수 = money//700
#     음료수 = 0
#     잔돈 = money - 700*개수
#     for 임시 in range(개수):
#         print('음료수 = {}개, 잔돈 = {}원'.format(개수,잔돈))
#         음료수 += 1
#         잔돈 -= 700

# vending_machine(3000)
##


def 절댓값더하기(숫자1,숫자2):
    결과 = 숫자1 + 숫자2
    if 숫자1 < 0 and 숫자2 > 0:
        return 숫자1*-1 + 숫자2
    elif 숫자2 < 0 and 숫자1 > 0:
        return 숫자2*-1 + 숫자1
    elif 숫자1 < 0 and 숫자2 < 0:
        return 숫자1*-1 + 숫자2*-1
    else:
        return 결과


print(절댓값더하기(3,-1))
print(절댓값더하기(5,2))
print(절댓값더하기(-3,-2))

