import cv2
import os
import face_recognition
import numpy as np
import pandas as pd
from datetime import datetime

path='attendance_images'
images = []
classNames = []
myList = []
myList = os.listdir(path)

# Taking out of extensions(.jpg) from the image names
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

data = pd.read_csv('Attendance.csv', names=['NAME OF THE PERSON', 'STATUS', 'TIME'])
data.drop([i for i in range(0, len(data.index))], axis=0, inplace=True)


for i in range(0,len(classNames)):
    data.loc[len(data.index)] = [classNames[i], 'ABSENT', '00:00:00 XX']


# Encoding the images in the Images file (coverting to RGB)
def findencodings(images):
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Giving Attendance existed in the images file
def markattendance(name, classNames):
    now = datetime.now()
    dstring = now.strftime('%I:%M:%S %p')
    
    index = classNames.index(name)
    data['STATUS'][index] = 'PRESENT'
    data['TIME'][index] = dstring
    data.to_csv('Attendance.csv', index=False)

encodeListKnown = findencodings(images)
print(classNames)
print("Encoding Completed")

wcam , hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
a='hello'

while(True):
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    
    attendees = []
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        face_dist = face_recognition.face_distance(encodeListKnown, encodeFace)
        y1,x2,y2,x1 = faceLoc
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
        matchIndex = np.argmin(face_dist)
        if(matches[matchIndex]):
            name = classNames[matchIndex].upper()
            cv2.putText(img, name.upper(), (x1+10,y1-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0),2)

            if(name not in attendees):
                attendees.append(name)
                markattendance(name, classNames)
        
    cv2.imshow('Attedance Register', img)
    cv2.waitKey(1)