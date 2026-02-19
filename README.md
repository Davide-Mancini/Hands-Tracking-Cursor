# Hands-Tracking-Cursor

> Un sistema di controllo del mouse basato su Computer Vision e Hand Tracking che permette di usare la mano come un vero dispositivo di input.
> Il progetto utilizza MediaPipe + OpenCV + Python per tracciare la mano in tempo reale e trasformare i movimenti e i gesti in comandi di sistema (mouse, click, drag, comandi OS).
> Progetto sviluppato solo per curiosità, divertimento e voglia di imparare linguaggio Python.

# Come iniziare

> Per prima cosa per poter utilizzare questo codice è necesario creare un ambiente virtuale ed installare una serie di pacchetti

## Creazione ambiente virtuale

```bash
python -m venv venv
```

## Attivazione

```bash
venv\Scripts\activate
```

## Installazione pacchetti

```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
pip install pygetwindow
```

# Come avviare

> Una volta instalatti i pacchetti sopra citati per far partire il codice basterà

- Apire il terminale

```bash
CTRL + ò
```

- Eseguire il file main.py

```bash
python main.py
```

# Come utilizzare

> A questo punto si aprirà in automatico la finestra con la webcam e il programma iniziera a traciare la mano
> Ora ad ogni movimento della mano corrispondera quello del cursore.

# Gesti

- Indice: Movimento del cursore
- Pollice nel palmo: Click
- Corna: Doppio click
- Pinch (unione pollice e indice): Drag & Drop
- Pugno: Chiusura pagina (Alt+F4)

# Requisiti

- Webcam funzionante
- Python installato
- Sistema operativo Windows
