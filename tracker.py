import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL_PATH = "hand_landmarker.task"

BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

def handle_results (result, output_image, timestamp_ms):
    globals()["latest_result"] = result

options= HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),    
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=handle_results,
    num_hands=1
)

landmarker = HandLandmarker.create_from_options(options)
latest_result = None
def tracks_hands(frame,timestamp_ms):
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    )
    landmarker.detect_async(mp_image, timestamp_ms)
    return latest_result