import pyautogui

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

def map_to_screen(x, y):
    x= 1-x

    screen_x = int(x * SCREEN_WIDTH)
    screen_y = int(y * SCREEN_HEIGHT)
    return int(screen_x), int(screen_y)