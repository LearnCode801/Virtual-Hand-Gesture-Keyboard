import cv2
import numpy
import time
from pynput.keyboard import Controller
import cvzone
import mediapipe
from cvzone.HandTrackingModule import HandDetector

url='http://192.168.10.2:8080/video'
cap=cv2.VideoCapture(url)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8,maxHands=10)
keys=[
     ['Q','W','E','R','T','Y','U','I','O','P'],
     ['A','S','D','F','G','H','J','K','L',';'],
     ['Z','X','C','V','B','N','M',',','.','<-']]

clickedText=""
keyboard=Controller()
def drawALL(img,buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

    return img

class Button():
    def __init__(self, pos, text, size=[80, 80]):
        self.pos = pos
        self.text = text
        self.size = size

buttonList=[]
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 200], key))


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    if success is not None:
        cv2.rectangle(img, (55, 55), (1040, 120), (0, 150, 0), cv2.FILLED)
        cv2.putText(img, clickedText, (60, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
        # cv2.rectangle(img, (46, 160), (1040, 520), (50, 50, 50), cv2.FILLED)
        lmlist, bboxInfo = detector.findPosition(img)
        drawALL(img, buttonList)
        cv2.rectangle(img, (150, 530), (850,600), (0, 0,0), cv2.FILLED)
        cv2.putText(img," Space ", (400, 580), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

        cv2.imshow('LIVE VIDEO', img)

        # print(lmlist)
        # print(bboxInfo)

        if lmlist:
            l, _, _ = detector.findDistance(8, 4, img)
            for button in buttonList:
                x,y=button.pos
                w,h=button.size
                # print(button)
                # print('x : ',x)
                # print('y : ',y)
                # print('width : ',w)
                # print('hight : ',h)
                if x<lmlist[8][0]<x+w and y<lmlist[8][1]< y+h:
                    cv2.rectangle(img, button.pos,(x + w, y + h),(255,0,0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                    # l,_,_=detector.findDistance(8,4,img)
                    print(l)
                    if l < 25 :
                        # keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255),2)
                        print("\t ----> ")
                        if button.text=='<-':
                            b = clickedText[:-1]
                            clickedText = b
                        else:
                            clickedText=clickedText+button.text
                            time.sleep(0.2)

            if l<25:
                if 150 < lmlist[8][0] < 850  and   530 < lmlist[8][1] < 600:
                    cv2.rectangle(img, (150, 530), (850, 600), (255, 255, 255), cv2.FILLED)
                    cv2.putText(img, " Space ", (400, 580), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
                    clickedText = clickedText + " "

        print(clickedText)




    q=cv2.waitKey(1)
    if q=='q':
        break
cv2.destroyAllWindow()






