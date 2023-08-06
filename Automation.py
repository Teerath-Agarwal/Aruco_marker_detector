from dbm import _KeyType
import cv2
import numpy as np
import cv2.aruco as aruco





VideoCap = False
capture = cv2.VideoCapture(0)

def findAruco(img,marker_size = 6, total_markers = 250, draw = True):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')
    
    arucoDict = aruco.Dictionary_get(key)

    arucoParam = aruco.DetectorParameters_create()
    bbox,ids,_ = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    print(ids)
    
while True:
    
    if VideoCap: _,img = capture.read()
    else: 
        img = cv2.imread("sample_image.jpg")
       # img = cv2.resize(img,(0,0),fx = 0.4, fy = 0.4)
        
    findAruco(img)
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

