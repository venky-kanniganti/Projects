import cv2 as cv
# import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np
import time
from multiprocessing import Queue, Process

def averageOutBGR(image,degree=20):
    outputMatrix = np.empty(((int)(720/degree), (int)(1280/degree), 3),int)
    # print(len(outputMatrix))
    # print(len(outputMatrix[0]))  tests work
    for x in range(0,(int)(len(image)/degree)):
        for y in range(0,(int)(len(image[0])/degree)):
            (rX, gX, bX) = (0,0,0)
            for d in range(0,degree):
                for b in range(0,degree):
                    (rX, gX, bX) = (rX+image[(degree*x)+d][degree*y+b][0],gX+image[(degree*x)+d][degree*y+b][1],bX+image[(degree*x)+d][degree*y+b][2])
            outputMatrix[x][y][0] = (int)(rX/degree**2)
            outputMatrix[x][y][1] = (int)(gX/degree**2)
            outputMatrix[x][y][2] = (int)(bX/degree**2)
    return outputMatrix
def averageOutBW(img,degree=7,skip=4):
    #1/skip is the ratio of pixels skipped
    image = np.array(img)
    image = image.astype('float32')
    outputMatrix = np.empty(((int)(720/degree), (int)(1280/degree), 1),'float32')
    xRange = (int)(len(image)/degree)
    yRange = (int)(len(image[0])/degree)

    degskip = (int)(degree/skip)
    degsq = degskip**2
    redcoeff = (0.11)/degsq
    grncoeff = (0.59)/degsq
    blucoeff = (0.3)/degsq
    # timetwo = time.process_time() ####

    for x in range(xRange):
        degx = degree*x
        for y in range(yRange):
            yPos = degree*y
            red = 0
            grn = 0
            blu = 0
            for d in range(degskip):
                xPos = degx + skip*d
                for b in range(degskip):
                    yPosi = yPos + skip*b
                    red += image[xPos][yPosi][0]
                    grn += image[xPos][yPosi][1]
                    blu += image[xPos][yPosi][2]
            #source:https://www.baeldung.com/cs/convert-rgb-to-grayscale
            #equation is for RGB --> grayscale [I mislabelled rgb instead of bgr (what openCV uses), hence difference in eqn]
            outputMatrix[x][y] = (redcoeff*red)+(grncoeff*grn)+(blucoeff*blu)
    # print(time.process_time() - timetwo)  ####
    return outputMatrix.astype(int)
def plot(frame):
    plt.imshow(frame, interpolation='nearest')
    plt.show()
    #pull color data from Image
    #map color data to brightness scale
    #map brightness to text brightness
    #print in terminal
def mapping(value,minIn,maxIn,minOut,maxOut):
    ratio = (maxOut - minOut)/(maxIn - minIn)
    return (int)(minOut + ratio*value)
def terminalArrayPrintInteger(frame):
    for row in range(len(frame)):
        bigSize = 2
        print((bigSize*100 - len(frame)*4)*' ')
        for i in range(len(frame[0])):
            x = frame[row][i]
            if x>=100:
                print((str(x).replace('[',' ')).replace(']',''),end = '')
            elif (x >= 10):
                print(' 0',end='')
                print((str(x).replace('[','')).replace(']',''),end = '')
            else:
                print(' 00',end='')
                print((str(x).replace('[','')).replace(']',''),end = '')
def terminalArrayPrint(brightnessScale,frame,rowlimit=1000,darkMode = False):
    if darkMode == True:
        brightnessScale = brightnessScale[::-1]
    for row in range(len(frame)):
        bigSize = 2
        if row==rowlimit:
            break
        print((bigSize*100 - len(frame)*4)*' ')
        for i in range(len(frame[0])):
            x = frame[row][i][0]
            m = mapping(x,0,255,0,len(brightnessScale)-1)
            print(brightnessScale[m],end='')

cap = cv.VideoCapture(0)
time.sleep(0.2)             #delay for camera to register
#source:http://paulbourke.net/dataformats/asciiart/
brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."

while True:
    frame = cap.read()[1]
    frame=averageOutBW(frame)
    terminalArrayPrint(brightness,frame,60)
    # terminalArrayPrintInteger(frame)
# plot(frame)



















# if __name__ == '__main__':
#     q = Queue()
#     frame = cap.read()[1]
#     p = Process(target=averageOutBW, args=(frame,))
#     print("hi")
#     p.start()
#     print("hi")
#     terminalArrayPrint(brightness,q.get(),60,darkMode = True)
#     print("hi")
#     p.join()




#alternate brightness scales
#brightness = [.,^~:;!*<{%&$@#]
#non alphanumeric ascii character set
#print("~`!@#$%^&*()_-+={}[]|\:;<,>.?/")




#----------------------------------------------------------------------
#Source: https://www.pythonfixing.com/2022/05/fixed-python-opencv-multiprocessing.html

#Bruh I dont understand this at all
# import multiprocessing as mp
# import cv2 as cv
# import time
#
# def capture_frames():
#     capture = cv.VideoCapture(0)
#     capture.set(cv.CAP_PROP_BUFFERSIZE, 2)
#
#     #X = desired FPS
#     X = 1000
#     FPS = 1/X
#     FPS_MS = int(FPS * 1000)
#
#     while True:
#         # Ensure camera is connected
#         if capture.isOpened():
#             (status, frame) = capture.read()
#
#             # Ensure valid frame
#             if status:
#                 cv.imshow('frame', frame)
#             else:
#                 break
#             if cv.waitKey(1) & 0xFF == ord('q'):
#                 break
#             time.sleep(FPS)
#
#     capture.release()
#     cv.destroyAllWindows()
#
# if __name__ == '__main__':
#     print('Starting video stream')
#     capture_process = mp.Process(target=capture_frames, args=())
#     capture_process.start()
