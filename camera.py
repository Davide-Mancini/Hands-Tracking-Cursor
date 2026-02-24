# Importo la libreria OpenCV per gestire la webcam e le operazioni sui video
import cv2

def init_camera():
    # Apre la prima webcam dispnibile indice 0, se ci sono più webcam, è possibile cambiare l'indice per decidere quale utilizzare
    cap = cv2.VideoCapture(0)
    #  cap è l'oggetto che rappresenta il flusso video dalla webcam, e viene restituito per essere utilizzato nelle altre funzioni
    return cap
#  Funzione che prende in input l'oggetto cap e legge un frame dal flusso video, restituendo il frame se la lettura è avvenuta con successo, altrimenti restituisce None
def get_frame(cap):
    success, frame = cap.read()
    if not success:
        return None
    return frame


# Inserisco le informazioni direttamente sul video della webcam
def legend (frame):
    # Queste sono le coordinate di partenza per il testo, e la distanza tra le righe
    x=10
    y=25
    line=25
    cv2.putText(frame, "Hand Tracking - Press ESC to exit", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,200,255), 2)
    # Per evitare sovrapposizioni, aumento la coordinata y ad ogni riga
    y += line*2
    cv2.putText(frame, "Move cursor: Move index finger", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,200,255), 1)
    y += line
    cv2.putText(frame, "Click: Thumb in palm", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,200,255), 1)
    y += line
    cv2.putText(frame, "Drag: Pinch thumb and index", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,200,255), 1)
    y += line
    cv2.putText(frame, "Close window: Fist for 2 seconds", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,200,255), 1)
    y += line
    cv2.putText(frame, "Double Click: Horns", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,200,255), 1)