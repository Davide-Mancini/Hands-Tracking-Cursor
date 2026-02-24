import cv2

HAND_CONNECTIONS=[
    (0,1),(1,2),(2,3),(3,4),      # pollice
    (0,5),(5,6),(6,7),(7,8),      # indice
    (0,9),(9,10),(10,11),(11,12), # medio
    (0,13),(13,14),(14,15),(15,16), # anulare
    (0,17),(17,18),(18,19),(19,20)  # mignolo
]

# Funzione che disegna i punti di riferimento delle mani e le connessioni tra di essi sul frame video, prende in input il frame e i punti di riferimento della mano, 
# calcola le coordinate in pixel dei punti di riferimento e disegna cerchi per ogni punto e linee per ogni connessione definita nell'array HAND_CONNECTIONS.
#  Le coordinate dei punti di riferimento sono normalizzate tra 0 e 1, quindi vengono moltiplicate per la larghezza e l'altezza del frame per ottenere le coordinate in pixel.
#  I cerchi vengono disegnati in verde e le linee in blu.
def draw_hand_landmarks(frame, hand_landmarks):
    h, w, _ = frame.shape
    for lm in hand_landmarks:
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(frame, (cx, cy), 5, (0, 255,0), -1)
    for connection in HAND_CONNECTIONS:
        start_idx, end_idx = connection
        start_lm = hand_landmarks[start_idx]
        end_lm = hand_landmarks[end_idx]
        cv2.line(frame, (int(start_lm.x * w), int(start_lm.y * h)), (int(end_lm.x * w), int(end_lm.y * h)), (255,0,0), 2)