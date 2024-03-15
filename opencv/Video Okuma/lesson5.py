import cv2
yakala = cv2. VideoCapture("video.mp4")

while (yakala.isOpened()):
       deger, kare = yakala.read()
       gray = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
       # cv2.imshow("Kaza", kare)
       cv2.imshow("Kaza", gray)

       if cv2.waitKey(1) & 0xFF == ord("q"):
            break
yakala.release()
cv2.destroyAllWindows()
