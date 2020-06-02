import numpy as np
import cv2 as cv
import os

img=np.zeros((512,512,3),np.uint8)

def ColorWind(b,g=-1,r=-1):
    """
    This function displays color of the pixel in new window
    If an image is grayscale,it will only take one argument
    If an image is BGR, it will take three corresponding BGR channel's value
    """

    #--- If image if in the BGR format ---#
    if g>-1:
        local_img=np.zeros((100,100,3),np.uint8)
        local_img[:]=(b,g,r)
        cv.imshow("Color",local_img)
    #--- If image if in the Grayscale format ---#
    else:
        local_img=np.zeros((100,100,1),np.uint8)
        local_img[:]=b
        cv.imshow("Color",local_img)


def mouseClickCoor(event, x, y, flags, param):
    global img
    if event == cv.EVENT_LBUTTONDBLCLK:
        if len(img.shape)>2:
            print("Coordinates: height={}, width={} - Color: {},{},{}".format(y,x,img[y,x,0],img[y,x,1],img[y,x,2]))
            ColorWind(img[y,x,0],img[y,x,1],img[y,x,2])
        else:
            print("Coordinates: height{}, width{} - Color: {}".format(y,x,img[y,x]))
            ColorWind(img[y,x])

def GetCoordinatesAndColor(imgg):
    """
    This function takes an image composed of numpy array
    and displays the coordinates and color of the pixel
    which is double clicked by mouse
    """
    global img
    if img.size==0:
        print("Image can't be read")
        return False
    img=imgg
    cv.namedWindow("Image")
    cv.setMouseCallback("Image",mouseClickCoor)
    cv.imshow("Image",img)
    k=cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    #--- Image should  be present in the current directory
    imgPath=input("Enter the full name of the image (e.g. Test.png): ")
    if os.path.exists(os.path.join(os.getcwd(),imgPath)):
        image=cv.imread(imgPath,1)
        if(image is None):
            print("File is not an Image")
        else:
            GetCoordinatesAndColor(image)
    else:
        print("Image path not valid")