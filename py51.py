

class 자동차:
    # 클래스 멤버 변수 (=self)
    차종 = ''
    차주인 = ''
    차색상 = ''

    def __init__(self):
        pass
    def 차정보입력(self, name, owner, color):
        self.차종 = name
        self.차주인 = owner
        self.차색상 = color
    def 차정보(self):
        print('차는', self.차종, '차주인은', self.차주인, '차색상은', self.차색상)


#클래스 사용법 (객체화)
내차 = 자동차()     # 클래스를 변수에 담는다 (=객체화한다)
내차.차정보입력('모닝', '홍길동', '빨간색')

'''

class 슈퍼카:
    # 클래스 멤버 변수 (=self)
    차종 = ''
    차주인 = ''
    차색상 = ''
    부스터 = 0

    def __init__(self):
        pass
    def 차정보입력(self, name, owner, color, buster):
        self.차종 = name
        self.차주인 = owner
        self.차색상 = color
        self.부스터 = buster
    def 차정보(self):
        print('차는', self.차종, '차주인은', self.차주인, '차색상은', self.차색상, '부스터용량', self.부스터)

누구차 = 슈퍼카()
누구차.차정보입력('슈퍼카','아무개','빨간색',80)
누구차.차정보()

'''


# 상속: 클래스 복사붙여놓기 (사람이 아닌 컴퓨터가)
class 슈퍼카(자동차):
    부스터 = '부스터 사용 가능'
    def 차정보(self):  # 부모 클래스가 중복되는게 아니라 수정된 함수가 우선으로 사용됨
        print('차는', self.차종, '차주인은', self.차주인, '차색상은', self.차색상, self.부스터)

누구차 = 슈퍼카()
누구차.차정보입력('슈퍼카','아무개','빨간색')
누구차.차정보()

class Coffee:

    def __init__(self, bean):
        self.bean = bean
    
    def coffee_info(self):
        print('원두: {}'.format(self.bean))

class Espresso(Coffee):

    def __init__(self, bean, water):
        super().__init__(bean)  # super():부모
        self.water = water
    
    def espresso_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))

coffee = Espresso('콜롬비아',30)
coffee.espresso_info()
