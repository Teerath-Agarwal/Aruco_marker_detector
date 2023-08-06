
import cv2
import numpy as np
# import cv2.aruco as aruco





VideoCap = False
capture = cv2.VideoCapture(0)


dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

def findAruco(img,detector):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(gray)
    print(markerIds)
    print(markerCorners)
    
while True:
    
    if VideoCap: _,img = capture.read()
    else: 
        img = cv2.imread("sample_image.jpg")
        img = cv2.resize(img,(0,0),fx = 0.4, fy = 0.4)
        
    findAruco(img,detector)
    if cv2.waitKey(1) == 113: #milliseconds
        break
    cv2.imshow("img",img)


 #___________________________________________________
 
#  import cv2 as cv

# arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
# parameters =  cv2.aruco.DetectorParameters()
# detector = cv.aruco.ArucoDetector(dictionary, parameters)

# frame = cv.imread(...)

# markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)



#__________________________________________________________
 
# cv2.destroyAllWindows()
# #-----------Start by loading an image
# imLoad = cv2.imread("sample_image.jpg")
# print(imLoad)
# imLoad.shape
# cv2.imshow('ArUco Marker',imLoad)
# cv2.waitKey(10000) #milliseconds
# cv2.destroyAllWindows()

# cv2.imwrite('ArUco Marker.jpg',imLoad)

# arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
# arucoParams = cv2.aruco.DetectorParameters_create()
# (corners, ids, rejected) = cv2.aruco.detectMarkers(imLoad, arucoDict,
# 	parameters=arucoParams)



# #cv2.imshow ("Window Name", imLoad)
# #cv2.waitKey(0)
# #cv2.destroyAllWindows()
# # image = np.zeros((512, 512, 3), np.uint8)

# # cv2.line(image, (0,0), (511, 511), (0,255,0), 5)

# # cv2.rectangle(image, (384,0), (510,128), (0,0,255), 3)

# # cv2.circle(image, (447, 63), 63, (255, 0, 0), -1)

# # cv2.imshow('Image', image)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

