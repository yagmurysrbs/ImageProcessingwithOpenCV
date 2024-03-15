import cv2
 # video kareleri yakala degiskenine atandı
yakala = cv2.VideoCapture (0)
while (True):
#Kameradan bir kare yakalanır sonsuz döngüde deger degiskenine atanır
    deger, kare = yakala.read()
# Yakalanan kare ekranda gösterilir
    cv2.imshow("Ben", kare)
# q tuşuna basınca döngü sonlanır
    if cv2.waitKey(1) & 0xFF == ord("q") :
             break
#kamera serbest bırakılır tüm pencereler kapatılır
yakala.release()
cv2.destroyAllWindows()
