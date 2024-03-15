import cv2
img = cv2.imread("images.png", 0)
img2 = cv2.rectangle(img, (15, 15), (880, 275), (0, 255, 0), 5)
img3 = cv2.circle(img2, (450, 150), 40, (59, 150, 255), -1)
cv2.imshow("images", img3)
font = cv2.FONT_HERSHEY_COMPLEX
img4 = cv2.putText(img3, "Logo", (45, 110), font, 2, 15, 2, cv2.LINE_AA)
cv2.imshow("image4", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
