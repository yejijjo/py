# 리스트 = []
# 세트 = set({})

# 세트.add(1)
# 세트.add(2)
# 세트.add(2)
# 세트.discard(2)
# print(세트)

세트 = set({})

for i in range(3):
    a = input('희망하는 수학여행지를 입력하세요>>>')
    세트.add(a)
print('조사된 수학여행지는 {}입니다.'.format(세트))
