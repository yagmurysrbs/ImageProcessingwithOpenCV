import cv2
yakala = cv2.VideoCapture("atatürk.mp4")
print(yakala.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(yakala.get(cv2.CAP_PROP_FRAME_WIDTH))
while(  yakala.isOpened()):
    ret, frame = yakala.read()
    frame = cv2.rectangle(frame, (500, 300), (150,100), (0, 255, 0),5)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
               break
yakala.release()
cv2.destroyAllWindows()
