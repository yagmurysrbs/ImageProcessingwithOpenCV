import cv2
resim = cv2.imread("logoopencv.jpeg",0)
# 0 siyah beyaz
cv2.imshow("Logo", resim)
# cv2.imwrite("logogrihali.jpeg",resim)

a = cv2.waitKey(0)
# esc kayıt eder
if a==27:
    cv2.destroyAllWindows()
# s kaydetmeden cıkıs
elif a==ord('s'):
    cv2.imwrite("opencv s tusu.png",resim)

