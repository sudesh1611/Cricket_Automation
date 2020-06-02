import cv2 as cv
import pyautogui
import numpy as np

#--- For capturing screenshots and make video from it ---#
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 10.0, (1366,768))

while(True):

    #--- Capture screenshot as PIL image ---#
    img = pyautogui.screenshot()
    frame = np.array(img,dtype=np.uint8)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    #--- Makes a retangle on the sreenshot for showing in video
    #--- (x,y), where x is width and y is height of pixel.
    #--- These values are according to my screen resolution, you can use
    #--- GetCoordinatesAndColor.py to get coordinates according to your sreen resolution ---#   
    cv.rectangle(frame,(640,380),(730,421),(0,0,255))

    #--- Crop the highlighted rectangle part of the screenshot by slicing numpy array
    #--- Syntax is [x1:x2,y1:y2], where
    #--- x1 is height of top-left pixel of rectangle,
    #--- x2 is height of bottom-right pixel of rectangle,
    #--- y1 is width of top-left pixel of rectangle,
    #--- y2 is width of bottom-right pixel of rectangle,
    frame2 = frame[380:421,640:730]
    frame2 = cv.cvtColor(frame2,cv.COLOR_RGB2GRAY)

    #--- Change the cropped image to binary colors black and white
    #--- All pixels having value less than 150 will turn black
    #--- All piels having values greater than or equal to 150 will turn white
    #--- This threshold value might vary, use trial and error to get correct value
    
    _,thresh = cv.threshold(frame2,150,255,cv.THRESH_BINARY_INV)
    cv.waitKey(1)
    
    #--- Check number of white pixels in the rectangle, our ball will appear as white pixel
    #--- If number of white pixels is greter than 160, enter will be pressed
    #--- Number of white pixels might vary, uncomment next line to get values in output video ---#
    #--- cv.putText(frame,str(np.count_nonzero(thresh.ravel() == 255)),(500,600),cv.FONT_HERSHEY_PLAIN,3,(0,0,255),2) ---#
    if np.count_nonzero(thresh.ravel() == 255) > 160:
        x=5
        while(x>0):
            pyautogui.press('enter')
            x=x-1
    out.write(frame)
cv.destroyAllWindows()