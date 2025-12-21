# STEP 1: ESP32-CAM Arduino Code

Resources and documentation for Arduino code implementing a WiFi-based image capture and streaming system using ESP32-CAM microcontroller. The code is organized in a modular architecture with separate files for main logic, declarations, and HTTP handlers. This system allows real-time image streaming and capture through a web browser interface.

## Description

Arduino IDE code to upload images captured by ESP32-CAM to a web server. Images are displayed by IP from any web browser.

## Project Structure

The project hierarchy and files description is as follows:

1. **1_ESP32_Arduino**: Arduino IDE sketch folder
   1. `WifiCam.ino` - Main file (open THIS in Arduino IDE). Contains setup() and loop() functions for WiFi initialization and HTTP server management.
   2. `WifiCam.hpp` - Header file (declarations). Contains all function declarations, variable definitions and preprocessor directives with `#ifndef` guards.
   3. `handlers.cpp` - HTTP handlers (functions). Contains implementation of HTTP request handlers:
      1. `handleRoot()` - Serves main HTML interface page
      2. `handleCapture()` - Captures single image
      3. `handleStream()` - Continuous MJPEG video stream
      4. `handleJpg()` - Returns current JPEG frame

## Specifications

- **Resolution:** 1024×768 JPG
- **Server:** Port 80 and 81
- **Interface:** Web browser via IP
- **WiFi:** Configurable (SSID + Password)
- **Architecture:** 3 modular files (.ino + .hpp + .cpp)

## Features

✅ Real-time WiFi transmission
✅ 1024×768 resolution
✅ Low standby power consumption
✅ Compatible with deep sleep mode
✅ Scalable modular architecture
✅ Intuitive web interface

## Dependencies

- Arduino IDE 1.8.13+
- ESP32 Board Support 2.0+
- ESP32-Camera library

---

## How to Use

1. Open Arduino IDE
2. Install library: `esp32-camera` (Espressif)
3. Download the **3 files together**
4. Place in the **SAME folder**
5. Open **ONLY** `WifiCam.ino`
6. Configure your WiFi SSID and Password
7. Select Board: **"AI Thinker ESP32-CAM"**
8. Upload the code (Ctrl+U)
9. Open Serial Monitor (115200 baud)
10. Copy the IP that appears in the console
11. Open browser: `http://192.168.x.x` (your IP)

---

## 🔧 STEP-BY-STEP INSTALLATION IN ARDUINO IDE

### 1️⃣ Open Arduino IDE

Launch the Arduino IDE program on your computer.

### 2️⃣ Open the WifiCam.ino file

Arduino IDE will automatically load the other 2 files.

### 3️⃣ Verify that the 3 tabs are present

At the **BOTTOM** of the editor, you should see **3 tabs**:

If you see the 3 tabs, everything is good! ✅

### 4️⃣ Configure your WiFi

In the **WifiCam.ino** tab, find these lines:

```cpp
const char* WIFI_SSID = "Mi_Red_WiFi"; // Your SSID
const char* WIFI_PASS = "Mi_Contraseña"; // Your password
```

Replace with your credentials.

### 5️⃣ Select the correct Board

Menu: Tools → Board
Search: "AI Thinker ESP32-CAM"
Select it

### 6️⃣ Select the COM Port

Menu: Tools → Port
Select the port where your ESP32 is connected
Example: COM3, COM4, /dev/ttyUSB0, etc.

### 7️⃣ Upload the code

Sketch → Upload
Or press: Ctrl+U

Wait for it to finish. You will see a success message:

```
Uploading...
Writing at 0x00010000... (100%)
Done! Upload complete.
```

### 8️⃣ Open Serial Monitor

Tools → Serial Monitor
Or press: Ctrl+Shift+M

Important: Speed = 115200 baud

### 9️⃣ Get your ESP32 IP

In the Serial Monitor you will see:

```
Connecting to WiFi...
...
✅ Connected to WiFi
IP: 192.168.1.110 ← COPY THIS IP
Server started on port 80
```

### 🔟 Open in your browser

Type in the address bar:

`http://192.168.1.110`

Or replace with the IP you saw in Serial Monitor.

You should see the web interface! 🎉

---

## ⚠️ Common Errors

| Error | Solution |
|-------|----------|
| "WifiCam.hpp: No such file" | The 3 files must be together in the same folder |
| "handlers.cpp: No such file" | Verify that WifiCam.hpp has `#include "handlers.cpp"` |
| "Arduino.h not found" | Install ESP32 Board Support from Board Manager |
| "Won't connect to WiFi" | Verify SSID/Password, WiFi 2.4GHz, Serial Monitor 115200 |
| "Connection refused" | Press RESET on ESP32, wait 2s, refresh browser |
