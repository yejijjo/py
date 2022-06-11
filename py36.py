from cv2 import add


def 첫인사():
    print('안녕하세요 저는 인천에 사는 코쿤입니다.')
def 본문():
    print('저는 인천 토박이이며, 인천중학교를 다녔고~~~')
    print('저는 인천 토박이이며, 인천고등학교를 다녔고~~~')
    print('저는 인천 토박이이며, 인천대학교를 다녔고~~~')
    print('저는 인천 토박이이며, 인천캠프를 다녔고~~~')
def 끝인사():
    print('하여 저는 이 곳에 반드시 필요한 인재가 될 것 입니다.')

첫인사()
본문()
끝인사()

def welcome():
    print('Hello Python')
    print('Nice to meet you')

welcome()

def introduce(name,age):
    print('내 이름은 {}이고, 나이는 {}살입니다'.format(name,age))

introduce('james',25)

def address():
    str1 = '우편번호 12345\n'
    str1 += '서울시 영등포구 여의도동'
    return str1
print(address())