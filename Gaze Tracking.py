import cv2
from gaze_tracking import GazeTracking
import pyautogui as gui
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    gaze.refresh(frame)

    x = gaze.horizontal_ratio()
    y = gaze.vertical_ratio()

    if gaze.is_blinking():
        time.sleep(0.1)
        if gaze.is_blinking:
            gui.click()
            print ("Blink\n")

    if type(x) == float and type(y) == float:
        if x < 0.4:
            print ("Left", end=" ")
            gui.move(-25, 0)

        elif x > 0.7:
            print ("Right", end=" ")
            gui.move(25, 0)

        else:
            print ("Centre", end=" ")

        if y < 0.45:
            print ("Top", end=" ")
            gui.move(0, -25)

        elif y > 0.65:
            print ("Bottom", end=" ")
            gui.move(0, 25)

        else:
            print ("Centre", end=" ")

        print ("\n")

    else:
        print ("Not Detected\n")

    cv2.imshow("", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()