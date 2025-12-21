# PASO 1: ESP32-CAM Arduino Code

Resources and documentation for Arduino code implementing a WiFi-based image capture and streaming system using ESP32-CAM microcontroller. The code is organized in a modular architecture with separate files for main logic, declarations, and HTTP handlers. This system allows real-time image streaming and capture through a web browser interface.

## Descripción

Código Arduino IDE para subir imágenes capturadas por ESP32-CAM a un servidor web.
Las imágenes se visualizan por IP desde cualquier navegador.

## Project Structure

The project hierarchy and files description is as follows:

1. **1_ESP32_Arduino**: Arduino IDE sketch folder
   1. `WifiCam.ino` - Archivo principal (abre ESTE en Arduino IDE). Contains setup() and loop() functions for WiFi initialization and HTTP server management.
   2. `WifiCam.hpp` - Header file (declaraciones). Contains all function declarations, variable definitions and preprocessor directives with `#ifndef` guards.
   3. `handlers.cpp` - Manejadores HTTP (funciones). Contains implementation of HTTP request handlers:
      1. `handleRoot()` - Serves main HTML interface page
      2. `handleCapture()` - Captures single image
      3. `handleStream()` - Continuous MJPEG video stream
      4. `handleJpg()` - Returns current JPEG frame

## Especificaciones

- **Resolución:** 1024×768 JPG
- **Servidor:** Puerto 80 y 81
- **Interfaz:** Web browser por IP
- **WiFi:** Configurable (SSID + Password)
- **Arquitectura:** 3 archivos modulares (.ino + .hpp + .cpp)

## Características

✅ Transmisión WiFi en tiempo real
✅ Resolución 1024×768
✅ Consumo bajo en espera
✅ Compatible con deep sleep mode
✅ Arquitectura modular escalable
✅ Interfaz web intuitiva

## Dependencias

- Arduino IDE 1.8.13+
- ESP32 Board Support 2.0+
- ESP32-Camera library

---

## Cómo usar

1. Abre Arduino IDE
2. Instala librería: `esp32-camera` (Espressif)
3. Descarga los **3 archivos juntos**
4. Coloca en la **MISMA carpeta**
5. Abre **SOLO** `WifiCam.ino`
6. Configura SSID y Password de tu WiFi
7. Selecciona Board: **"AI Thinker ESP32-CAM"**
8. Sube el código (Ctrl+U)
9. Abre Serial Monitor (115200 baud)
10. Copia la IP que aparece en consola
11. Abre navegador: `http://192.168.x.x` (tu IP)

---

## 🔧 INSTALACIÓN PASO A PASO EN ARDUINO IDE

### 1️⃣ Abre Arduino IDE

Inicia el programa Arduino IDE en tu computadora.

### 2️⃣ Abre el archivo WifiCam.ino

Arduino IDE cargará automáticamente los otros 2 archivos.

### 3️⃣ Verifica que las 3 pestañas están presentes

En la parte **INFERIOR** del editor, deberías ver **3 pestañas**:

Si ves las 3 pestañas, ¡todo está bien! ✅

### 4️⃣ Configura tu WiFi

En la pestaña **WifiCam.ino**, busca estas líneas:


Reemplaza con tus credenciales:

const char* WIFI_SSID = "Mi_Red_WiFi"; // Tu SSID
const char* WIFI_PASS = "Mi_Contraseña"; // Tu contraseña

### 5️⃣ Selecciona el Board correcto

Menú: Herramientas → Placa
Busca: "AI Thinker ESP32-CAM"
Selecciona

text

### 6️⃣ Selecciona el Puerto COM

Menú: Herramientas → Puerto
Selecciona el puerto donde está conectado tu ESP32
Ej: COM3, COM4, /dev/ttyUSB0, etc.

text

### 7️⃣ Sube el código

Sketch → Subir
O presiona: Ctrl+U

text

Espera a que termine. Verás un mensaje de éxito:

Subiendo...
Escribiendo a 0x00010000... (100%)
¡Listo! La carga se ha completado.

text

### 8️⃣ Abre Serial Monitor

Herramientas → Serial Monitor
O presiona: Ctrl+Shift+M

Importante: Velocidad = 115200 baud

text

### 9️⃣ Obtén la IP de tu ESP32

En el Serial Monitor verás:

Conectando a WiFi...
...
✅ Conectado a WiFi
IP: 192.168.1.110 ← COPIA ESTA IP
Servidor iniciado en puerto 80

text

### 🔟 Abre en tu navegador

Escribe en la barra de direcciones:

http://192.168.1.110

text

O reemplaza con la IP que viste en Serial Monitor.

¡Deberías ver la interfaz web! 🎉

---

## ⚠️ Errores Comunes

| Error | Solución |
|-------|----------|
| "WifiCam.hpp: No such file" | Los 3 archivos deben estar juntos en la misma carpeta |
| "handlers.cpp: No such file" | Verifica que WifiCam.hpp tenga `#include "handlers.cpp"` |
| "Arduino.h not found" | Instala ESP32 Board Support desde Board Manager |
| "No conecta WiFi" | Verifica SSID/Password, WiFi 2.4GHz, Serial Monitor 115200 |
| "Connection refused" | Presiona RESET en ESP32, espera 2s, refresca navegador |

---
