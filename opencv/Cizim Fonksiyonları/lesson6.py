import cv2
import numpy as np
img = np.zeros((512, 512,3) ,np.uint8)
cv2.imshow("Pencere", img)
img2 = cv2.line(img ,(0,0), (512, 512) ,(255,0,0), (6))
cv2.imshow("Cizgili", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
