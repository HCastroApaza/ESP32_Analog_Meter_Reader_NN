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
