# importing the module
import cv2
import math
import numpy as np
import random

# function to display the coordinates of
# of the points clickeimport numpy as np

def click_event(event, x, y, flags, params):

   # checking for left mouse clicks
   if event == cv2.EVENT_LBUTTONDOWN:
      global counter, list,i
  
      # displaying the coordinates
      # on the Shell
      print(x, ' ', y)
      list.append(x)
      list.append(y)
      counter=counter+1

      # displaying the coordinates
      # on the image window
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(img, str(x) + ',' +
               str(y), (x,y), font,
               0.5, (255, 0, 0), 2)

      cv2.imshow('image', img)
      # the below code calculates the length of the line and stores in a list

      if (counter==2):
         print(list)
         i=i+1
         length = math.dist([list[0], list[1]], [list[2], list[3]])
         print(length)
         cv2.putText(img, "Length :"+' '+ str(int(length)), (list[0],list[1]-100), font,
               1, (0, 255, 0), 2)

         cv2.imshow('image', img)
         coordinates[i]= (list[0],list[1])
         result.append(int(length))
         res_d[i] = int(length)
         #reinitialize the counter and list 
         counter=0
         list=[]
         print(result)
         print("res_d",res_d)
         print("coordinates",coordinates)   

      # after all the calculations of the lines are done, we sort the values from low to high and display them below each figure


   if(i==4):
      a = sorted(res_d.items(), key=lambda x: x[1])    
      print(a)
      for j in range(0,4):
         c = a[j][0]
         d = a[j][1]
         x_coord = coordinates[c][0] 
         y_coord= coordinates[c][1] + 100
         cv2.putText(img, str(a.index((c,d))+1), (x_coord,y_coord), font, 1, (0, 0, 255),4)
         cv2.imshow('image', img)

      cv2.waitKey(0)



# driver function
if __name__=="__main__":

   counter = 0
   list = []
   result =[]
   res_d = {}
   coordinates={}
   i=0

   img = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
   img = cv2.resize(img, (1000,1000))

   edges = cv2.Canny(img, 0, 100)
   lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=2)

   for line in lines:
      x1, y1, x2, y2 = line[0]
      cv2.line(img,(x1,y1),(x2,y2),(0, 255, 255),2)

   # displaying the image
   cv2.imshow('image', img)

   # setting mouse handler for the image
   # and calling the click_event() function
   cv2.setMouseCallback('image', click_event)
 

   # wait for a key to be pressed to exit
   cv2.waitKey(0)

   # close the window
   cv2.destroyAllWindows()
