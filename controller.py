import pyautogui
import collections
import math
import time
prev_x, prev_y = 0,0
smooth_factor = 0.2

click_treshold_z = -0.05
click_state = False
drag_state = False

x_buffer = collections.deque(maxlen=5)
y_buffer = collections.deque(maxlen=5)
def move_cursor(x,y):
    # global prev_x, prev_y, smooth_factor

    # new_x = prev_x + (x - prev_x) * smooth_factor
    # new_y = prev_y + (y - prev_y) * smooth_factor
    # pyautogui.moveTo(new_x, new_y)
    # prev_x, prev_y = new_x, new_y

    # COLLEZIONA GLU ULTIMI 5 MOVIMENTI E NE CALCOLA LA MEDIA PER MAGGIORE STABILITà DEL CURSORE 
    x_buffer.append(x)
    y_buffer.append(y)
    avg_x = sum(x_buffer) / len(x_buffer)
    avg_y = sum(y_buffer) / len(y_buffer)
    pyautogui.moveTo(avg_x, avg_y)

def check_click_forward(hand, screen_w, screen_h):
    # VECCHIO METODO PER IL CLICK BASATO SULLA PROFONDITA CON SOGLIA SULL'ASSE Z, MA NON MOLTO AFFIDABILE E POCO PRECISO
    # global click_state
    # index = hand[8]
    # thumb = hand[4]
    # palm_center = hand[9]
    # z= index.z
    # if z < click_treshold_z and not click_state:
    #     pyautogui.click()
    #     click_state = True 
    #     print(click_state)
    # elif z >= click_treshold_z and click_state:
    #     click_state = False
    #     print(click_state)
    # NUOVO METODO PER IL CLICK BASATO SULLA DISTANZA TRA POLLICE E PALMO, PIU AFFIDABILE E PRECISO
    global click_state
    thumb = hand[4]
    palm_center = hand[9]
    dist = math.hypot(
        thumb.x - palm_center.x,
        thumb.y - palm_center.y,
    )
    CLICK_TRESHOLD= 0.08
    if dist < CLICK_TRESHOLD and not click_state:
        pyautogui.click()
        click_state = True
    elif dist >= CLICK_TRESHOLD and click_state:
        click_state = False

def check_pinch_drag (hand, screen_w, screen_h):
    global drag_state
    thumb = hand[4]
    index = hand[8]

    thumb_x, thumb_y = int(thumb.x * screen_w), int(thumb.y * screen_h)
    index_x, index_y = int(index.x * screen_w), int(index.y * screen_h)
    dist = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
    pinch_threshold = 40

    if dist < pinch_threshold and not drag_state:
        pyautogui.mouseDown()
        drag_state = True
    elif dist >= pinch_threshold and drag_state:
        pyautogui.mouseUp()
        drag_state = False 


# GESTO PER CHIUDERE LA FINESTRA TRAMITE IL COMANDO ALT+F4, ALLA CHIUSURA DEL PUGNO PER PIù DI 2 SECONDI PER EVITARE CHIUSURE ACCIDENTALI.
fist_start_time = None
# SECONDI CHE IL PUGNO DEVE ESSERE MANTENUTO CHIUSO PER RICONOSCERE IL GESTO DI CHIUSURA FINESTRA
FIST_HOLD_TIME = 2.0
# SOGLIA DI DISTANZA TRA LE DITA E IL PALMO
FIST_TRESHOLD = 0.1
 
#  QUI SI APPLICA IL TEOREMA DI PITAGORA PER CALCOLARE LA DISTANZA TRA DUE PUNTI, IN QUESTO CASO TRA LE DITA E IL PALMO PER RICONOSCERE IL GESTO DI CHIUSURA
def distance(a,b):
    return math.hypot(a.x - b.x, a.y - b.y)

# QUI VERIFICA SE TUTTE LE DITA SONO CHIUSE, PER OGNI DITO DELL'ARRAY VERIFICA SE KA DISTANZA è INFERIORE ALLA SOGLIA, SE LO è AGGIUNGE +1 ALLA VARIABILE DITA CHIUSE FINO A QUANDO ARRIVA A 5
def is_fist(hand):
    palm_center = hand[9]
    fingers= [hand[i] for i in [4,8,12,16,20]]
    close_fingers = 0
    for finger in fingers:
        if distance(finger, palm_center) < FIST_TRESHOLD:
            close_fingers += 1
    return close_fingers == 5

# QUI CONTA IL TEMPO IN CUI IL PUGNO è CHIUSO, SE IL TEMPO SUPERA LA SOGLIA DI 2 SEC IMPOSTATA VIENE RICONOSCIUTO IL GESTO ALTRIMENTI RIPARTE IL CONTEGGIO, IN QUESTO MODO SI EVITANO CHIUSURE ACCIDENTALI DELLA FINESTRA
def detect_close_gesture(hand):
    global fist_start_time
    if is_fist(hand):
        if fist_start_time is None:
            fist_start_time = time.time()
        elif time.time() - fist_start_time > FIST_HOLD_TIME:
           
            fist_start_time = None
            return True
    else:
        fist_start_time = None

    return False

# FUNZIONE PER IL DOPPIO CLICK FACENDO IL SEGNO DELLE CORNA
horn_state = False
HORNS_COOLDOWN = 1.0
last_horn_time = 0
def detect_double_click(hand):
    global horn_state, last_horn_time
    fingers = [hand[i] for i in [8, 12, 16, 20]] 
    thumb = hand[4]
    palm_center = hand[9]
    d_thumb = distance(thumb, palm_center)
    d_index = distance(fingers[0], palm_center)
    d_middle = distance(fingers[1], palm_center)
    d_ring = distance(fingers[2], palm_center)
    d_pinky = distance(fingers[3], palm_center)
    UP= 0.18
    DOWN= 0.10
    horns =(
        d_thumb < DOWN and
        d_index > UP and
        d_middle < DOWN and
        d_ring < DOWN and
        d_pinky > UP
    )
    now= time.time()
    if horns and not horn_state and now - last_horn_time > HORNS_COOLDOWN:
        pyautogui.doubleClick()
        horn_state = True
        last_horn_time = now
    elif not horns:
        horn_state = False



def close_window():
    pyautogui.hotkey('alt', 'f4')