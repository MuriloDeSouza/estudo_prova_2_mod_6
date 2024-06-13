import cv2

# Caminho para o vídeo
video_path = '../static/mourinho.mp4'

# Carregar o vídeo
cap = cv2.VideoCapture(video_path)

# Verificar se o vídeo foi carregado com sucesso
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

# Carregar o classificador de rostos pretreinado do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ler e exibir frames do vídeo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar suavização para reduzir o ruído
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Mostrar o Número de Rostos Detectados:
        cv2.putText(frame, f'Rostos detectados: {len(faces)}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Exibir o frame com as detecções de rosto
    cv2.imshow('Frame', frame)

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o vídeo e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
