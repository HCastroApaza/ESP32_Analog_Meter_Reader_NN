# PASO 1: ESP32-CAM Arduino Code

## Descripción

Código Arduino IDE para subir imágenes capturadas por ESP32-CAM a un servidor web.
Las imágenes se visualizan por IP desde cualquier navegador.

## Archivo

- `wifi_stream_capture.ino` - Código completo para ESP32-CAM

## Especificaciones

- **Resolución:** 1024×768 JPG
- **Servidor:** Puerto 80 y 81
- **Interfaz:** Web browser por IP
- **WiFi:** Configurable (SSID + Password)

## Cómo usar

1. Abre Arduino IDE
2. Instala librería: `esp32-camera` (Espressif)
3. Copia `wifi_stream_capture.ino`
4. Configura SSID y Password de tu WiFi
5. Selecciona Board: "AI Thinker ESP32-CAM"
6. Sube el código (Upload)
7. Abre Serial Monitor (115200 baud)
8. Copia la IP que aparece en consola
9. Abre navegador: `http://192.168.x.x` (tu IP)

## Características

- Transmisión WiFi en tiempo real
- Resolución 1024×768
- Consumo bajo en espera
- Compatible con deep sleep mode
- Simple interfaz web

## Dependencias

- Arduino IDE 1.8.13+
- ESP32 Board Support 2.0+
- ESP32-Camera library
----------------------------------------------------------------------------
🔧 INSTALACIÓN PASO A PASO EN ARDUINO IDE
1️⃣ Abre Arduino IDE
Inicia el programa Arduino IDE en tu computadora.

2️⃣ Abre el archivo WifiCam.ino
text
Menú: Archivo → Abrir
Busca y selecciona: WifiCam.ino
Haz clic en: Abrir
3️⃣ Verifica que las 3 pestañas están presentes
En la parte INFERIOR del editor, deberías ver 3 pestañas:

text
┌──────────────────────────────────────────────────────────┐
│ [WifiCam.ino]   [WifiCam.hpp]   [handlers.cpp]   ...     │
│     ↑ PRINCIPAL      ↑ HEADER        ↑ FUNCIONES         │
└──────────────────────────────────────────────────────────┘
Si ves las 3 pestañas, ¡todo está bien! ✅

4️⃣ Configura tu WiFi
En la pestaña WifiCam.ino, busca estas líneas:

cpp
const char* WIFI_SSID = "WIFI_V";           // ← CAMBIA AQUÍ
const char* WIFI_PASS = "vecino2021";       // ← CAMBIA AQUÍ
Reemplaza con tus credenciales:

cpp
const char* WIFI_SSID = "Mi_Red_WiFi";     // Tu SSID
const char* WIFI_PASS = "Mi_Contraseña";   // Tu contraseña
5️⃣ Selecciona el Board correcto
text
Menú: Herramientas → Placa
Busca: "AI Thinker ESP32-CAM"
Selecciona
6️⃣ Selecciona el Puerto COM
text
Menú: Herramientas → Puerto
Selecciona el puerto donde está conectado tu ESP32
Ej: COM3, COM4, /dev/ttyUSB0, etc.
7️⃣ Sube el código
text
Sketch → Subir
O presiona: Ctrl+U
Espera a que termine. Verás un mensaje de éxito:

text
Subiendo...
Escribiendo a 0x00010000... (100%)
¡Listo! La carga se ha completado.
8️⃣ Abre Serial Monitor
text
Herramientas → Serial Monitor
O presiona: Ctrl+Shift+M

Importante: Velocidad = 115200 baud
9️⃣ Obtén la IP de tu ESP32
En el Serial Monitor verás:

text
Conectando a WiFi...
...
✅ Conectado a WiFi
IP: 192.168.1.110    ← COPIA ESTA IP
Servidor iniciado en puerto 80
🔟 Abre en tu navegador
text
Escribe en la barra de direcciones:
http://192.168.1.110

O reemplaza con la IP que viste en Serial Monitor
¡Deberías ver la interfaz web!
