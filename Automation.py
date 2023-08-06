import cv2
import numpy as np
import cv2.aruco as aruco





VideoCap = False
capture = cv2.VideoCapture(0)


dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

def findAruco(img,detector):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(gray)
    for i in range(6):
        pt1 = tuple(markerCorners[i][0][0].astype(int))
        pt2 = tuple(markerCorners[i][0][2].astype(int))
        cv2.rectangle(img, pt1, pt2, (0,255,0), thickness=2)
        text_position = (pt1[0], pt1[1])  
        cv2.putText(img, str(markerIds[i]), text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    
while True:
    
    if VideoCap: _,img = capture.read()
    else: 
        img = cv2.imread("sample_image.jpg")
        img = cv2.resize(img,(0,0),fx = 0.4, fy = 0.4)
        
    findAruco(img,detector)
    if cv2.waitKey(1) == 113: 
        break
    cv2.imshow("img",img)