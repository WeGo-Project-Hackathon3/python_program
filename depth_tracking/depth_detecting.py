import cv2
import pyrealsense2
from realsense_depth import *
 
point = (400,300)
 
def show_distance(event, x, y, args, params):
 global point
 point = (x,y)
 
 
#create mouse event
cv2.namedWindow("Color_Frame")
cv2.setMouseCallback("Color_Frame", show_distance)
 
while True:
 dc = DepthCamera()
 
 ret, depth_frame, color_frame = dc.get_frame()
  #show distance for specific point
 cv2.circle(color_frame, point, 4, (0,0,255))
 
 # using cv, we convert (x,y) to (y, x)
 distance = depth_frame[point[1], point[0]]
 
 #cv2.putText(color_frame, "{}".format(distance), (((point[0]+300)/2), ((point[1]+400)/2)), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0),2)
 cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

 cv2.imshow("color_frame", color_frame)
 cv2.imshow("depth_frame", depth_frame)
 key = cv2.waitKey(1)
 
 if key == 27 or key == 0xFF :
	dc.release()
	cv2.destroyAllWindows()
   break

