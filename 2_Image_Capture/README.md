# PASO 2: Descargar Imágenes del ESP32-CAM

Script Python para descargar 20 imágenes del ESP32-CAM mediante HTTP.

## Archivo

- `capture_esp32_images.py` - Script de captura automática

## Instalación

pip install requests pillow matplotlib

text

## Cómo Usar

python capture_esp32_images.py

text

**El programa hará lo siguiente:**

1. **Abre diálogo de carpeta**
   - Selecciona dónde guardar las imágenes
   - Si cancelas, usa directorio actual

2. **Conecta al ESP32-CAM**
   - URL: `http://192.168.1.110//1024x768.jpg`
   - (Cambia IP si tu ESP32 tiene otra)

3. **Captura 20 imágenes**
   - Una cada 3 segundos
   - Naming: `captura_YYYYMMDD_HHMMSS_ffffff.jpg`
   - Manejo automático de errores

4. **Muestra resultados**
   - Selecciona 2 imágenes al azar
   - Visualiza en interfaz gráfica

## Configuración

Edita estos valores en el código:

url = "http://192.168.1.110//1024x768.jpg" # IP y resolución
num_capturas = 20 # Número de imágenes
intervalo = 3 # Segundos entre capturas

text

## Funciones

| Función | Propósito |
|---------|-----------|
| `seleccionar_carpeta()` | Abre diálogo para elegir carpeta |
| `capturar_imagenes()` | Descarga imágenes del ESP32 |
| `mostrar_imagenes_aleatorias()` | Visualiza 2 imágenes al azar |

## Características

✅ Interfaz gráfica para seleccionar carpeta
✅ Timestamps únicos en nombres
✅ Manejo automático de errores
✅ Descarga HTTP con timeout
✅ Visualización de muestras

## Requisitos Previos

- ESP32-CAM debe estar en red y sirviendo imágenes
- Saber IP del ESP32 (ver Serial Monitor del PASO 1)
- Python 3.6+

## Salida

=== Programa de Captura de Imágenes ===
Por favor seleccione la carpeta...

Las imágenes se guardarán en: /ruta/carpeta

Imagen 1/20 capturada: captura_20250621_143022_456789.jpg
Imagen 2/20 capturada: captura_20250621_143025_456789.jpg
...
Imagen 20/20 capturada: captura_20250621_143057_456789.jpg

Seleccionando 2 imágenes aleatorias para mostrar...
[Visualiza 2 imágenes al azar]

Programa finalizado.

text

---

**Status:** Activo ✅
**Framework:** Requests + PIL + Matplotlib
**Imágenes:** 20 captures a 3 segundos cada una
