import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('l.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hImg,wImg = img.shape[:2]

block = pytesseract.image_to_boxes(img)
#recognising letters
for i in block.splitlines():
    print(i)
    i = i.split(' ')
    print(i)
    
    x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
    cv2.rectangle(img,(x,hImg-y), (w,hImg-h), (0,0,255),1)
    cv2.putText(img, i[0],(x,hImg-y+20),cv2.FONT_HERSHEY_COMPLEX,1, (100,100,100),1)

cv2.imshow('image',img)
cv2.waitKey(0)

#recognising words
img = cv2.imread('l.jpg')
block = pytesseract.image_to_data(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for count,j in enumerate(block.splitlines()):
    if count!=0:
        print(j)
        j = j.split()
        print(j)
        if len(j)==12:
        
            x,y,w,h = int(j[6]),int(j[7]),int(j[8]),int(j[9])
            cv2.rectangle(img,(x,y), (w+x,h+y), (0,0,255),1)
            cv2.putText(img, j[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1, (100,100,100),1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


