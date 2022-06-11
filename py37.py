import cv2

def 이미지띄우기():
    img = cv2.imread('ing1.jpg')
    cv2.imshow('tittle', img)
    cv2.waitKey(0)

def 이미지띄우기2(이미지이름):
    img = cv2.imread(이미지이름)
    cv2.imshow('tittle', img)
    cv2.waitKey(0)

def 회색이미지(이미지이름):
    img = cv2.imread(이미지이름)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('tittle', gray)
    cv2.waitKey(0)
    

# 이미지띄우기()
# 이미지띄우기2('ing1.jpg')
# 이미지띄우기2('ing2.jpg')
# 회색이미지('ing2.jpg')