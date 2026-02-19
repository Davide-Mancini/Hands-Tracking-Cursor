import cv2

def init_camera():
    cap = cv2.VideoCapture(0)
    return cap

def get_frame(cap):
    success, frame = cap.read()
    if not success:
        return None
    return frame


def legend (frame):
    x=10
    y=25
    line=25
    cv2.putText(frame, "Hand Tracking - Press ESC to exit", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,200,255), 2)
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