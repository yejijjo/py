import cv2

#이미지 불러오기
img = cv2.imread('ing1.jpg')

#크기변경
크기변경 = cv2.resize(img, (600, 600))

#글자넣기
cv2.putText(크기변경, 'YE JI', (20,20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 228, 255), 2)

#이미지 보여주기(제목,이미지명)
cv2.imshow('flower', 크기변경)

#이미지 띄워놓고 대기
cv2.waitKey(0)