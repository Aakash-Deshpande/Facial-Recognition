import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "XML_Files/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('face_recognition.avi', fourcc, 20.0, (640,480))

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
'''================FONTS=================
    FONT_HERSHEY_SIMPLEX = 0,
    FONT_HERSHEY_PLAIN = 1,
    FONT_HERSHEY_DUPLEX = 2,
    FONT_HERSHEY_COMPLEX = 3,
    FONT_HERSHEY_TRIPLEX = 4,
    FONT_HERSHEY_COMPLEX_SMALL = 5,
    FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
    FONT_HERSHEY_SCRIPT_COMPLEX = 7,
    FONT_ITALIC = 16
======================================'''

while(1):
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x,y), (x+w,y+h), (225,0,0), 2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf < 50):
            if(Id == 1):
                Id = "Adam"
            elif(Id == 2):
                Id = "Aakash"
        else:
            Id = "Unknown"
        
        cv2.putText(im, Id, (x,y+h), font, 2, (0,0,255), 2, cv2.LINE_AA)
    
    #out.write(im) # write the image in the file
    cv2.imshow('im',im) 
    
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()