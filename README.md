# Digit Classification System with Neural Networks

![Graphical abstract](/ProjectImages/GraphicalAbstract.PNG)

Complete project to capture images with ESP32-CAM, process them, and train a neural network to classify digits (0-9) with 98.2% accuracy.

## Project Structure

```
├── 1_ESP32_Arduino
│   ├── README.md
│   ├── WifiCam.hpp
│   ├── WifiCam.ino
│   └── handlers.cpp
├── 2_Image_Capture
│   ├── README.md
│   └── capture_esp32_images.py
├── 3_Image_Processing
│   ├── 03_Preprocessing.ipynb
│   └── README.md
├── 4_Neural_Network_Training
│   ├── 04_Neural_Network_Training_and_Prediction.ipynb
│   └── README.md
├── README.md
├── LICENSE
└── .gitignore
```

## How to Replicate the Project

### Step 1: Configure ESP32-CAM

1. Open `1_ESP32_Arduino/WifiCam.ino` in Arduino IDE
2. Configure WiFi in the code
3. Upload firmware to your ESP32-CAM
4. Get the ESP32 IP from Serial Monitor

Required files:
- `WifiCam.hpp` - Definitions
- `handlers.cpp` - Handlers

### Step 2: Download Images

```bash
cd 2_Image_Capture
python capture_esp32_images.py
```

Configure in the script:
- `url = "http://[YOUR_IP]/1024x768.jpg"`
- `num_capturas = 20`
- `intervalo = 3` (seconds)

Output: 20 JPG images in selected folder

See: `2_Image_Capture/README.md`

### Step 3: Process Images

```bash
cd 3_Image_Processing
jupyter notebook 03_Preprocessing.ipynb
```

Process:
1. Load ZIP with images
2. Binarize with OTSU threshold
3. Extract 6 blobs per image
4. Resize to 28×28 pixels
5. Export ZIP with blobs

Output: 120+ processed images (6 per original photo)

See: `3_Image_Processing/README.md`

### Step 4: Train Neural Network

```bash
cd 4_Neural_Network_Training
jupyter notebook 04_Neural_Network_Training_and_Prediction.ipynb
```

Processes:
1. Load MNIST dataset (60k train, 5k test, 5k val)
2. Normalize images [0-1]
3. Search optimal hyperparameters
4. Train neural network
5. Make predictions

Final Architecture:
```
Input (784) → Dense(448, ReLU) → Dense(224, ReLU) → Output(10, Softmax)
```

Results:
- Training Accuracy: ~99%
- Validation Accuracy: ~98%
- Test Accuracy: ~98.2%

See: `4_Neural_Network_Training/README.md`

## Quick Installation

### Requirements

```bash
pip install tensorflow keras keras-tuner scikit-learn matplotlib numpy pandas opencv-python requests pillow
```

Or install all:

```bash
pip install -r requirements.txt
```

### Hardware

- ESP32-CAM with WiFi module
- Computer with Python 3.8+
- GPU recommended (optional)

## Complete Flow in 5 Minutes

```
┌─────────────────────────────────┐
│ 1. CAPTURE (ESP32-CAM)          │
│    ↓ 20 images                  │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│ 2. DOWNLOAD (Python Script)     │
│    ↓ Stores JPG                 │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│ 3. PROCESS (Jupyter)            │
│    ↓ Extract 6 blobs/image      │
│    ↓ Binarize and resize        │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│ 4. TRAIN (Jupyter)              │
│    ↓ MNIST neural network       │
│    ↓ Accuracy: 98.2%            │
│    ↓ Predictions                │
└─────────────────────────────────┘
```

## Important Files

| File | Description |
|------|-------------|
| `1_ESP32_Arduino/WifiCam.ino` | ESP32-CAM firmware |
| `2_Image_Capture/capture_esp32_images.py` | Download images |
| `3_Image_Processing/03_Preprocessing.ipynb` | Process images |
| `4_Neural_Network_Training/04_Neural_Network_Training_and_Prediction.ipynb` | Train and predict |

## Required Configuration

Edit these values according to your setup:

**ESP32:**
```cpp
const char* ssid = "your_wifi";
const char* password = "your_password";
int camera_resolution = FRAMESIZE_XGA; // 1024x768
```

**Python (capture):**
```python
url = "http://192.168.1.110/1024x768.jpg"  # Your ESP32 IP
num_capturas = 20
intervalo = 3  # seconds
```

**Processing:**
```python
roi1 = bin_img[130:250, 220:700]     # Main region
roi2 = bin_img[160:240, 725:770]     # Secondary region
tamaño_salida = 28                   # Blob size
```

**Training:**
```python
epochs = 108                    # Number of epochs
batch_size = 540               # Batch size
learning_rate = 0.001          # Learning rate
units_capa1 = 448              # Layer 1 neurons
units_capa2 = 224              # Layer 2 neurons
```

## Features

✅ Automatic image capture with ESP32-CAM
✅ HTTP download without SD card
✅ Automatic image processing
✅ OTSU threshold binarization
✅ Intelligent blob extraction
✅ Trained neural network (98.2% accuracy)
✅ Real-time predictions
✅ Modular and reusable code

## Troubleshooting

**"Cannot connect to ESP32"**
- Verify IP in Serial Monitor
- Make sure WiFi is configured
- Try ping to the IP

**"Error in image processing"**
- Verify resolution is 1024x768
- Adjust ROI according to your image
- Check absolute/relative paths

**"Low accuracy in predictions"**
- Increase epochs to 150+
- Try batch_size = 256
- Normalize images properly

## Detailed Documentation

For specific information on each step, see:
- `1_ESP32_Arduino/README.md`
- `2_Image_Capture/README.md`
- `3_Image_Processing/README.md`
- `4_Neural_Network_Training/README.md`

## Expected Results

### Capture
- 20 images with clear extension
- Resolution 1024×768

### Processing
- 120+ extracted blobs
- Binarized and clean images
- Uniform 28×28 size

### Training
- Training accuracy: ~99%
- Validation accuracy: ~98%
- Test accuracy: ~98.2%
- Final loss: < 0.08

### Prediction
- Predicts digits 0-9
- Confidence: 85-95%
- Time: <100ms per image

## License

This project is under MIT license. See `LICENSE` file.

## Author

Digit classification project with deep learning.
Last update: December 2025

---

**Status:** Active ✅
**Version:** 1.0
**Framework:** TensorFlow + Keras + OpenCV
**Accuracy:** 98.2%
