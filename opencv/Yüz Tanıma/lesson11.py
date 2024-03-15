import cv2
import pyodbc


db = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=YAGMUR;'
    'Database=yüz_tespit;'
    'Trusted_Connection=yes'

)

imlec = db.cursor()
face_count = 0

# Yüz algılama için Cascade sınıflandırıcını yükle
face_cascade = cv2.CascadeClassifier('opencv_master_data_haarcascades_haarcascade_frontalface_default.xml')

# Kamerayı açın (0, birinci kamera demektir; farklı bir kamera kullanıyorsanız uygun numarayı girin)
cap = cv2.VideoCapture(0)

# Görüş açısından çıkan ve tekrar görüş açısına giren yüzleri saymak için değişkenler
inside_frame = False  # Görüş açısında mıyız?

while True:
    # Kameradan bir görüntü alın
    ret, frame = cap.read()

    # Görüntüyü gri tona dönüştürün (yüz algılama daha hızlıdır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algılayın
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        if not inside_frame:
            face_count += 1
            inside_frame = True
    else:
        inside_frame = False

    # Yüz sayısını ekranda gösterin
    cv2.putText(frame, f'Sayi: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Yüz sayısını SQLite veritabanına kaydedin
    imlec.execute("INSERT INTO tablo (sayi) VALUES (?)", (face_count,))
    cv2.imshow('Yüz Algılama', frame)
    db.commit()
    # Çıkış için "q" tuşuna basılmasını bekleyin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    db.commit()
# Kamera ve pencereyi kapatın
cap.release()
cv2.destroyAllWindows()
