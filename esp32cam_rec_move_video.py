

import os
import cv2
import time
from datetime import datetime

if not os.path.exists('video'):
    os.mkdir('video')

cap = cv2.VideoCapture('http://000.000.000.000:00/stream')

eventVideo = False
countVideo = 0
frameVideo = 500
fps = 30.0
image_size = (320,240)
video_file = 'video/res.avi'

out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size) 

ret, frame1 = cap.read()
ret, frame2 = cap.read()

time.sleep(1)

countMove = 0
countFrame = 0
while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # фильтрация лишних контуров
    a,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # метод для выделения кромки объекта белым цветом
    dilated = cv2.dilate(thresh, None, iterations = 3) #расширяет выделенную на предыдущем этапе область
    сontours,b = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # нахождение массива контурных точек

    for contour in сontours:
        (x, y, w, h) = cv2.boundingRect(contour) # преобразование массива из предыдущего этапа в кортеж из четырех координат

        if cv2.contourArea(contour) < 700: # условие при котором площадь выделенного объекта меньше 700 px
            countMove = 0;
            continue
            
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) # получение прямоугольника из точек кортежа
        cv2.putText(frame1, "Status: {}".format("Dvigenie"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA) #текст
        countMove += 1;

    #print(count)
    cv2.imshow("frame1", frame1)
    frame1 = frame2  
    ret, frame2 = cap.read() 

    if countMove > 1:
        eventVideo = True

    if countFrame > frameVideo:
        video_file = 'video/res'+str(countVideo)+'.avi'
        out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size) 
        countVideo += 1
        countFrame = 0
        eventVideo = False
    
    if eventVideo == True:
        countFrame += 1
        ret, frame = cap.read()
        out.write(frame)
        if countVideo == 0: 
            countFrame = frameVideo + 1

    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()

