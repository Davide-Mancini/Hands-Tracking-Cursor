import pyautogui

# Legge coordinate reali dello schermo
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
# Riceve coordinate normalizzate (0-1) e le trasforma in coordinate reali dello schermo
def map_to_screen(x, y):
    # Rimuovo specchiatura webcam invertendo l'asse x
    x= 1-x

    screen_x = int(x * SCREEN_WIDTH)
    screen_y = int(y * SCREEN_HEIGHT)
    # Restituisce le coordinate in pixel dello schermo, che possono essere usate per muovere il cursore o eseguire altre azioni basate sulla posizione della mano rilevata dalla webcam.
    return int(screen_x), int(screen_y)