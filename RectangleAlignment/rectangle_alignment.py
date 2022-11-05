import cv2
import numpy as np

def rotateImage(image, angel):#parameter angel in degrees
    height = image.shape[0]
    width = image.shape[1]
    height_big = height * 2
    width_big = width * 2
    image_big = cv2.resize(image, (width_big, height_big))
    image_center = (width_big/2, height_big/2)#rotation center
    rot_mat = cv2.getRotationMatrix2D(image_center,angel, 0.5)
    result = cv2.warpAffine(image_big, rot_mat, (width_big, height_big), flags=cv2.INTER_LINEAR)
    return result

if __name__=="__main__":

    Image = cv2.imread("img.jpg")
    Image = cv2.resize(Image, (1000,1000))
    r = cv2.selectROI("select the area", Image)
    num = int(input("Input the rectangle number 1/2/3/4 that you've selected \n"))

    if(num==1):
        angle = -75
    elif num == 2:
        angle = 74
    elif num == 3:
        angle = 60
    else:
        angle= -60


        # select the rectangle region that you'd like to rotate
  
    cropped_image = Image[int(r[1]):int(r[1]+r[3]),
                              int(r[0]):int(r[0]+r[2])]
    imageOriginal = cv2.resize(cropped_image, (200,200))
    imageRotated= rotateImage(imageOriginal, angle)
        # cv2.imshow("Rotated", imageRotated)
        # select the region to save image 
    r = cv2.selectROI("Image has been rotated . Please select the region to save the cropped image", imageRotated)
    cropped = imageRotated[int(r[1]):int(r[1]+r[3]),
                              int(r[0]):int(r[0]+r[2])]
    cv2.imwrite('rectangle_output_'+str(num)+'.jpg', cropped)
    print("Press C to exit and then try for other rectangles")
    output = cv2.imread('rectangle_output_'+str(num)+'.jpg')
    cv2.imshow("Output. Please press enter to save the output",output)
    cv2.waitKey(0)




