import cv2

def principal():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return

    print("Iniciando Rastreador de Rostos... Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rostos = face_cascade.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in rostos:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Rosto Detectado", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            olho_esq_x = int(x + (w * 0.3))
            olho_dir_x = int(x + (w * 0.7))
            olhos_y = int(y + (h * 0.35))
            raio_olho = int(w * 0.1)

            cv2.circle(frame, (olho_esq_x, olhos_y), raio_olho, (0, 0, 255), -1) 
            cv2.circle(frame, (olho_dir_x, olhos_y), raio_olho, (0, 0, 255), -1)

            boca_x1 = int(x + (w * 0.25))
            boca_y1 = int(y + (h * 0.65))
            boca_x2 = int(x + (w * 0.75))
            boca_y2 = int(y + (h * 0.85))
            cv2.rectangle(frame, (boca_x1, boca_y1), (boca_x2, boca_y2), (0, 0, 0), -1)

        cv2.imshow('Detector de Rostos Expert', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    principal()