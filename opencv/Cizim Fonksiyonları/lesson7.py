import cv2
img = cv2.imread("kopek.jpeg")
en = img.shape[1]
boy = img.shape[0]
print(f"Genişlik: {en} piksel")
print(f"Yükseklik: {boy} piksel")
img2 = cv2.rectangle(img.copy(), (15, 15), (215, 190), (0, 255, 0), 5)
img3 = cv2.circle(img2, (113, 100), 100, (0, 0, 255), 1)
cv2.imshow("köpek3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# img: Çizimin yapılacağı görüntü.
# (15, 15): Dikdörtgenin sol üst köşesinin koordinatları (x, y).
# (215, 190): Dikdörtgenin sağ alt köşesinin koordinatları (x, y).
# (0, 255, 0): Dikdörtgenin kenar çizgisinin rengi (BGR renk formatı kullanılıyor).
# Burada (0, 255, 0) yeşil bir kenar çizgisi belirtir.
# 5: Dikdörtgenin kenar kalınlığı.

# img2: Çizimin yapılacağı görüntü. Bu, önceki cv2.rectangle() işlevinin çıktısı olabilir.
# (113, 100): Dairenin merkez koordinatları (x, y).
# 100: Dairenin yarıçapı.
# (0, 0, 255): Dairenin iç rengi (BGR renk formatı kullanılıyor). Burada (0, 0, 255) kırmızı bir iç renk belirtir.
# -1: Daireyi içiyle doldurur, yani içi tamamen kapatır.
# 1: Dairenin içi boş,çember çizer
