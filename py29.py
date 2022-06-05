# list = []
# list.append(2)
# list.append(3.14)
# list.append('안녕하세요')

# 삽입하기 : .insert(번호, 번호앞에 추가할 것)
# 제거하기 : .pop(해당하는 번호) → -1은 뒤에서부터
# 수정하기 : [번호] = 문구

lst = []

개수 = int(input('몇 개의 과일을 보관할까요? >>>'))
for a in range(개수):
    과일 = input('{}번째 과일을 입력하세요'.format(a+1))
    lst.append(과일)
print('입력받은 과일들은 {}입니다'.format(lst))


