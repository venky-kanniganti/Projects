#brightness = [.,^~:;!*<{%&$@#]
brightness = [".",",","^","*","<","/","!","@","#","$","%","&","~",";",":","{"]

#Source: reddit.com/r/Python/comments/cpymni/7_lines_of_python_code_to_show_your_webcam_in_a/

import PySimpleGUIQt as sg
import cv2 as cv
import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy


def frameProcessing(frame):
    plt.imshow(frame, interpolation='nearest')
    plt.show()

# define the window layout
layout = [[sg.Image(filename='', key='_IMAGE_')]]

# create the window and show it without the plot
window = sg.Window("Venky's Camera", layout, location=(0,0))

# ---===--- Event LOOP Read and display frames, operate the GUI --- #
cap = cv.VideoCapture(0)                               # Setup the OpenCV capture device (webcam)

while True:
    event, values = window.Read(timeout=20, timeout_key='timeout')
    if event is None:
        break
    frame = cap.read()[1]                               # Read image from capture device (camera)
    imgbytes=(cv.imencode('.png', frame)[1]).tobytes()     # Convert the buffer to PNG Bytes
    window.find_element('_IMAGE_').Update(data=imgbytes)   # Change the Image Element to show the new image

    frameProcessing(frame)
