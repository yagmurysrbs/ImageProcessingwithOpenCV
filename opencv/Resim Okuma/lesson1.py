
import cv2

# Resim dosyasının yolunu doğru şekilde belirtme !
image_path = 'indir.png'

# Resmi okuyun ve boyutunu kontrol etme
image = cv2.imread(image_path)

if image is not None and image.shape[0] > 0 and image.shape[1] > 0:

    cv2.imshow('Resim', image)

    cv2.waitKey(0)
    # Bir tuşa basana kadar bekle
    cv2.destroyAllWindows()


else:
     print("Resim okunamadı veya geçerli değil.")
