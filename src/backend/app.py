import cv2  
 
# caminho para o arquivo do vídeo
video_mourinho = '../static/mourinho.mp4'

#carregar o vídeo
cap = cv2.VideoCapture(video_mourinho)

#verificação báscia se o vídeo foi carregado
if not cap.isOpened():
    print("O vídeo não conseguiu abrir")
    exit()

#ler e exibir os frames
frame_number = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

# Exibir o frame
    cv2.imshow('Frame', frame)
    
    # Salvar o frame (opcional)
    cv2.imwrite(f'frame_{frame_number}.jpg', frame)
    frame_number += 1

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o vídeo e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()