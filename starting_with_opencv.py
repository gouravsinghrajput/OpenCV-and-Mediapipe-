# loading an image and displaying it using OpenCV

# import cv2
# import sys

# image = cv2.imread(cv2.samples.findFile("Lh44.jpg"))

# if image is None:
#     sys.exit("could not read the image")

# cv2.imshow("display window", image)
# k = cv2.waitKey(0)

# if k == ord("q"):
#     cv2.imwrite("Lh44.jpg", image)



# basic webcam feed display using OpenCV (grayscale)

# import cv2 as cv
# import numpy as num

# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("cannot open the camera")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("cannot collect the frame, exiting the program")
#         break

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)

#     k = cv.waitKey(1)
#     if k == ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()




#playing a video file using OpenCV
'''everything will be same, except we will use, the name of the file insted of the our initial video capture zero,
   and in the place of the waitkey index, we will be using the numbers depending on what speed do we need in our video, 
   higher the waitkey index, slower the video will play...
'''


# import cv2 as cv
# import numpy as num

# cap = cv.VideoCapture('WIN_20251219_22_29_59_Pro.mp4')
# # if not cap.isOpened():
# #     print("cannot open the camera")
# #     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("cannot collect the frame, exiting the program")
#         break

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', (gray))

#     k = cv.waitKey(60)   #the longer the waitkey, the slower the video will play..
#     if k == ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()






# import cv2 as cv
# import numpy as num
# # import sys

# img = cv.imread("Lh44.jpg")

# # if img is None:
# #    sys.exit('could not read the image')

# cv.imshow('Lewis Hamilton', img)

# cv.waitKey(0)
# # == ord('q'):
#    # cv.imwrite("Lh44.jpg", img)



# capturing video from webcam and saving it to a file using OpenCV
'''to save videos we need fourcc code, which is a 4 byte code used to specify the video codec.
   use this when required, not that imoportant for basic understanding.
'''


''' simply opening the webcam and displaying the video feed using OpenCV and Mediapipe'''


# import cv2 as cv
# import numpy as num 

# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("cannot open the camera")
#     exit()

# while True:
#       ret, frame = cap.read()
#       if not ret:
#           print("cannot collect the frame, exiting the program")
#           break
      
#       frame = cv.flip(frame, 1)
#       # frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) imshow wxpects BGR format and we changed it to RBG, so that is why it was giving weird colors.
#       cv.imshow('frame', frame)

#       k = cv.waitKey(1)
#       if k == ord('q'):
#          break

# cap.release()
# cv.destroyAllWindows()





'''np is numpy.
the np.zero function is used to ccreate a image itself
np.zero cretaes a empty array with the initial and all values as zero.
now we initialize thsome value in that empty array.
it takes three arguements, first is the height of the image, second is the width of the image.
now the third arguement is the number of channels, we use 3 channels as opencv uses BGR format, and we use 1 channel for grayscale images.
so this creates a black image of the given size.

and now, the np.uint8 is unsigned 8 bit integer, which means the values can range from 0 to 255, and this is what opencv uses to represent the pixel values.

now the second line:
cv.line(img,(0,0),(511,511),(231,126,153 ),5)

cv.line is used to draw a line.
it takes 5 arguements:
the first arguement is the image (name of the variable in which the np.zero is stored).
the second and third arguements are the cordinates of the stsrting and ending points of the line, 
(0,0) is considered as the top left corner.
the next arguement is the color of the line in the BGR format.
and the last arguement is the thickness of the line in pixels.
'''
# import numpy as np
# import cv2 as cv

# # Create a black image
# img = np.zeros((512,512,3), np.uint8)

# # Draw a diagonal blue line with thickness of 5 px
# cv.line(img,(0,0),(511,511),(231,126,153 ),5)
# '''we used 511 and not 512 because indexing starts from 0, so the last pixel will be at 511.'''
# cv.imshow('image', img)

# k = cv.waitKey(0)
# if k == ord('q'):
#     cv.destroyAllWindows() 

'''simiraly we can draw rectangles, circles, ellipses, polygons and put text on images using opencv functions.

for rectangles, we use cv.rectangle in which the arguements are same but instead of starting and end points of line,
the top left and the bottom right corners of the rectangle are given.

for circles, we use cv.circle, the arguements consists of the image, centre coordinates, radius, color and the thickness
if we want to fill the circle, we use -1 in place of thickness.

For ellipses, we use cv.ellipse; the arguments consist of the image, centre coordinates, axes (half-width and half-height),
rotation angle, start angle, end angle, color, and thickness.
If we want to fill the ellipse, we use -1 in place of thickness.

and for other polygons, we use three things, first the coordinates of the vertices of the polygon, we keep the points in a list,
pts = np.array([points in [] ], np.int32), forces the points to be in the 32 integer format.
pts = pts.reshape((-1,1,2)) reshapes the points according to our need.
now the reshape format is as (number of points, 1, 2(coordinates)), like 2 for x,y
number of points = -1, opencv automatically calculates the number of points.
the next 1 is for the contour format.
cv.polylines(img,[pts],True,(color format), thickness)
if we use False, the plogon will remain open and won't close, that is it will be open polygon.

and the information for filling the polygon is given in the below code
'''

# import cv2 as cv
# import numpy as np

# img = np.zeros((512,512,3), np.uint8)
# cv.rectangle(img, (0,0), (511,511), (132,234,145), -1)
# pts = np.array([[12,34], [45,67], [78,90], [123,456]], np.int32)t
# pts = pts.reshape((-1,1,2))
# cv.polylines(img, [pts], True, (255,0,0), 8)
# cv.fillPoly(img,[pts],(0,0,255), lineType=None, shift=None)
# cv.imshow('image', img)

# k = cv.waitKey(0)
# if k == ord('q'):
#    cv.destroyAllWindows()




'''to add fonts to our image we use the cv.putText keyword
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

the first line select's the font style, and secondline puts it in the image.
the arguemnets are: For writing text on an image, we use cv.putText; the arguments consist of the image, the text string to be written,
the bottom-left starting coordinates of the text, the font type, the font scale (size), the color in BGR format, the thickness, and optionally the line type.
If we want smoother text, we use cv.LINE_AA as the line type, which applies anti-aliasing and makes the text look cleaner.
'''

# import cv2 as cv
# import numpy as np

# img = np.zeros((512,512,3), np.uint8)
# cv.rectangle(img, (0,0), (511,511), (132,234,145), -1)
# pts = np.array([[12,34], [45,67], [78,90], [123,456]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv.polylines(img, [pts], True, (255,0,0), 8)
# cv.fillPoly(img,[pts],(0,0,255), lineType=None, shift=None)
# cv.putText(img, 'hii, this is gourav', (5,250), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2, cv.LINE_AA)
# cv.imshow('image', img)

# k = cv.waitKey(0)
# if k == ord('q'):
#    cv.destroyAllWindows()

''''''
