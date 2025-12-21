# STEP 2: Download Images from ESP32-CAM

Python script to download 20 images from ESP32-CAM via HTTP.

## File

- `capture_esp32_images.py` - Automatic capture script

## Installation

```bash
pip install requests pillow matplotlib
```

## How to Use

```bash
python capture_esp32_images.py
```

**The program will do the following:**

1. **Opens folder dialog**
   - Select where to save images
   - If you cancel, uses current directory

2. **Connects to ESP32-CAM**
   - URL: `http://192.168.1.110//1024x768.jpg`
   - (Change IP if your ESP32 has a different one)

3. **Captures 20 images**
   - One every 3 seconds
   - Naming: `capture_YYYYMMDD_HHMMSS_ffffff.jpg`
   - Automatic error handling

4. **Shows results**
   - Selects 2 random images
   - Displays in graphical interface

## Configuration

Edit these values in the code:

```python
url = "http://192.168.1.110//1024x768.jpg"  # IP and resolution
num_capturas = 20                             # Number of images
intervalo = 3                                 # Seconds between captures
```

## Functions

| Function | Purpose |
|----------|---------|
| `seleccionar_carpeta()` | Opens dialog to select folder |
| `capturar_imagenes()` | Downloads images from ESP32 |
| `mostrar_imagenes_aleatorias()` | Displays 2 random images |

## Features

✅ Graphical interface to select folder
✅ Unique timestamps in filenames
✅ Automatic error handling
✅ HTTP download with timeout
✅ Sample visualization

## Prerequisites

- ESP32-CAM must be on network and serving images
- Know ESP32 IP (see Serial Monitor from STEP 1)
- Python 3.6+

## Output

```
=== Image Capture Program ===
Please select the folder...

Images will be saved to: /path/folder

Image 1/20 captured: capture_20250621_143022_456789.jpg
Image 2/20 captured: capture_20250621_143025_456789.jpg
...
Image 20/20 captured: capture_20250621_143057_456789.jpg

Selecting 2 random images to display...
[Displays 2 random images]

Program finished.
```

---

**Status:** Active ✅
**Framework:** Requests + PIL + Matplotlib
**Images:** 20 captures at 3 seconds each
