import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL_PATH = "hand_landmarker.task"

BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

# Funzione di callback che viene chiamata ogni volta che il modello rileva una mano nel video, aggiorna la variabile globale latest_result con i risultati del rilevamento
def handle_results (result, output_image, timestamp_ms):
    globals()["latest_result"] = result

options= HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH), 
    # Processa frame in tempo reale   
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=handle_results,
    # Rileva una sola mano cosi evita confusione e migliora la stabilità
    num_hands=1
)

landmarker = HandLandmarker.create_from_options(options)
latest_result = None
def tracks_hands(frame,timestamp_ms):
    mp_image = mp.Image(
        # Qui viene convertita l'immagine perchè Mediapipe usa RGB mentre openCV usa BGR
        image_format=mp.ImageFormat.SRGB,
        data= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    )
    landmarker.detect_async(mp_image, timestamp_ms)
    return latest_result