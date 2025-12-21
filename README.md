# Sistema de Clasificación de Dígitos con Redes Neuronales

Proyecto completo para capturar imágenes con ESP32-CAM, procesarlas y entrenar una red neuronal para clasificar dígitos (0-9) con accuracy de 98.2%.

## Estructura del Proyecto

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

## Cómo Replicar el Proyecto

### Paso 1: Configurar ESP32-CAM

1. Abre `1_ESP32_Arduino/WifiCam.ino` en Arduino IDE
2. Configura WiFi en el código
3. Carga el firmware en tu ESP32-CAM
4. Obtén la IP del ESP32 desde Serial Monitor

Archivos necesarios:
- `WifiCam.hpp` - Definiciones
- `handlers.cpp` - Controladores

### Paso 2: Descargar Imágenes

```bash
cd 2_Image_Capture
python capture_esp32_images.py
```

Configura en el script:
- `url = "http://[TU_IP]/1024x768.jpg"`
- `num_capturas = 20`
- `intervalo = 3` (segundos)

Salida: 20 imágenes JPG en la carpeta seleccionada

Ver: `2_Image_Capture/README.md`

### Paso 3: Procesar Imágenes

```bash
cd 3_Image_Processing
jupyter notebook 03_Preprocessing.ipynb
```

Proceso:
1. Carga ZIP con imágenes
2. Binariza con threshold OTSU
3. Extrae 6 manchas por imagen
4. Redimensiona a 28×28 píxeles
5. Exporta ZIP con manchas

Salida: 120+ imágenes procesadas (6 por foto original)

Ver: `3_Image_Processing/README.md`

### Paso 4: Entrenar Red Neuronal

```bash
cd 4_Neural_Network_Training
jupyter notebook 04_Neural_Network_Training_and_Prediction.ipynb
```

Procesos:
1. Carga dataset MNIST (60k train, 5k test, 5k val)
2. Normaliza imágenes [0-1]
3. Busca hiperparámetros óptimos
4. Entrena red neuronal
5. Realiza predicciones

Arquitectura Final:
```
Input (784) → Dense(448, ReLU) → Dense(224, ReLU) → Output(10, Softmax)
```

Resultados:
- Accuracy Entrenamiento: ~99%
- Accuracy Validación: ~98%
- Accuracy Test: ~98.2%

Ver: `4_Neural_Network_Training/README.md`

## Instalación Rápida

### Requisitos

```bash
pip install tensorflow keras keras-tuner scikit-learn matplotlib numpy pandas opencv-python requests pillow
```

O instala todos:

```bash
pip install -r requirements.txt
```

### Hardware

- ESP32-CAM con módulo WiFi
- Computadora con Python 3.8+
- GPU recomendada (opcional)

## Flujo Completo en 5 Minutos

```
┌─────────────────────────────────┐
│ 1. CAPTURA (ESP32-CAM)          │
│    ↓ 20 imágenes               │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│ 2. DESCARGAR (Python Script)    │
│    ↓ Almacena JPG              │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│ 3. PROCESAR (Jupyter)           │
│    ↓ Extrae 6 manchas/imagen   │
│    ↓ Binariza y redimensiona   │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│ 4. ENTRENAR (Jupyter)           │
│    ↓ Red neuronal MNIST         │
│    ↓ Accuracy: 98.2%            │
│    ↓ Predicciones               │
└─────────────────────────────────┘
```

## Archivos Importantes

| Archivo | Descripción |
|---------|-------------|
| `1_ESP32_Arduino/WifiCam.ino` | Firmware ESP32-CAM |
| `2_Image_Capture/capture_esp32_images.py` | Descarga imágenes |
| `3_Image_Processing/03_Preprocessing.ipynb` | Procesa imágenes |
| `4_Neural_Network_Training/04_Neural_Network_Training_and_Prediction.ipynb` | Entrena y predice |

## Configuración Necesaria

Edita estos valores según tu setup:

**ESP32:**
```cpp
const char* ssid = "tu_wifi";
const char* password = "tu_password";
int camera_resolution = FRAMESIZE_XGA; // 1024x768
```

**Python (capture):**
```python
url = "http://192.168.1.110/1024x768.jpg"  # Tu IP del ESP32
num_capturas = 20
intervalo = 3  # segundos
```

**Procesamiento:**
```python
roi1 = bin_img[130:250, 220:700]     # Región principal
roi2 = bin_img[160:240, 725:770]     # Región secundaria
tamaño_salida = 28                   # Tamaño manchas
```

**Entrenamiento:**
```python
epochs = 108                    # Número de épocas
batch_size = 540               # Tamaño batch
learning_rate = 0.001          # Tasa aprendizaje
units_capa1 = 448              # Neuronas capa 1
units_capa2 = 224              # Neuronas capa 2
```

## Características

✅ Captura automática con ESP32-CAM
✅ Descarga por HTTP sin SD card
✅ Procesamiento automático de imágenes
✅ Binarización con threshold OTSU
✅ Extracción inteligente de manchas
✅ Red neuronal entrenada (98.2% accuracy)
✅ Predicciones en tiempo real
✅ Código modular y reutilizable

## Solución de Problemas

**"No se conecta al ESP32"**
- Verifica IP en Serial Monitor
- Asegúrate WiFi esté configurado
- Prueba ping a la IP

**"Error en procesamiento de imágenes"**
- Verifica resolución sea 1024x768
- Ajusta ROI según tu imagen
- Revisa paths absolutos/relativos

**"Accuracy bajo en predicciones"**
- Aumenta epochs a 150+
- Prueba batch_size = 256
- Normaliza bien las imágenes

## Documentación Detallada

Para información específica de cada paso, consulta:
- `1_ESP32_Arduino/README.md`
- `2_Image_Capture/README.md`
- `3_Image_Processing/README.md`
- `4_Neural_Network_Training/README.md`

## Resultados Esperados

### Captura
- 20 imágenes con extensión clara
- Resolución 1024×768

### Procesamiento
- 120+ manchas extraídas
- Imágenes binarizadas y limpias
- Tamaño uniforme 28×28

### Entrenamiento
- Accuracy train: ~99%
- Accuracy validation: ~98%
- Accuracy test: ~98.2%
- Loss final: < 0.08

### Predicción
- Predice dígitos 0-9
- Confianza: 85-95%
- Tiempo: <100ms por imagen

## Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE`.

## Autor

Proyecto de clasificación de dígitos con aprendizaje profundo.
Última actualización: Diciembre 2025

---

**Estado:** Activo ✅
**Versión:** 1.0
**Framework:** TensorFlow + Keras + OpenCV
**Accuracy:** 98.2%
