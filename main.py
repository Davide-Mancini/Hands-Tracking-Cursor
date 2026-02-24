import cv2
from tracker import tracks_hands
from camera import init_camera, get_frame,legend
from mapper import map_to_screen
import draw_hand_landmarks as dh
from controller import move_cursor, check_click_forward, check_pinch_drag,detect_close_gesture,close_window,detect_double_click
import pyautogui


cap = init_camera()
timestamp = 0
screen_w, screen_h = pyautogui.size()
while True:
    # Legge un frame dalla webcam, se fallisce esce dal ciclo, altrimenti continua con il frame ottenuto
    frame = get_frame(cap)
    if frame is None:
        break
        # Mosta il frame passato alla funzione della legenda per le istruzioni a video
    legend(frame)
    results = tracks_hands(frame, timestamp)
    timestamp += 1

    if results and results.hand_landmarks:
        for hand in results.hand_landmarks:
           
            dh.draw_hand_landmarks(frame, hand)
            # Definisco l'indice come puntatore
            index_finger = hand[8]
            x_norm = index_finger.x
            y_norm = index_finger.y
            # Trasformo le coordinate normalizzate in coordinate dello schermo e muovo il cursore, poi controllo i gesti per click, drag, doppio click e chiusura finestra
            x_screen, y_screen = map_to_screen(x_norm, y_norm)
            move_cursor(x_screen, y_screen)
            detect_double_click(hand)
            check_click_forward(hand, screen_w, screen_h)
            check_pinch_drag(hand, screen_w, screen_h)
            if detect_close_gesture(hand):
                close_window()
            # print(f"Screen coordinates: ({x_screen}, {y_screen})")

    cv2.imshow("Hand Tracking", frame)

    # Con ESC chiude la finestra, altrimenti continua a mostrare il video 
    if cv2.waitKey(1) & 0xFF == 27:
        break
#  Rilascia la webcam e chiude tutte le finestre di OpenCV quando esce dal ciclo
cap.release()
cv2.destroyAllWindows()