import cv2 as cv
img = cv.imread("C:\Users\Otavio\Pictures\Noob Corp\NoobsCorpScreenHoot.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window