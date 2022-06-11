사전 = {'sun':'태양','moon':'달','star':'별','space':'우주'}

print(사전)

for 변수 in 사전:
    print('{}의 뜻: {}'.format(변수,사전.get(변수)))