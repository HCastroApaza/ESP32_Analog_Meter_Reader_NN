# PASO 3: Preprocessing

Notebook para procesar y extraer manchas de imágenes de medidores.

## Archivo

- `03_Preprocessing.ipynb` - Binarización y extracción de manchas

## Instalación

pip install opencv-python numpy matplotlib tqdm

text

## Cómo Usar

jupyter notebook 03_Preprocessing.ipynb

text

**Sigue estos pasos:**

1. **Carga imágenes**
   - Sube archivo ZIP con imágenes JPG/PNG
   - Extrae automáticamente

2. **Binariza imágenes**
   - Convierte a escala de grises
   - Aplica threshold automático (OTSU)

3. **Define regiones de interés (ROI)**
   - ROI 1: Región principal [130:250, 220:700]
   - ROI 2: Región secundaria [160:240, 725:770]

4. **Extrae manchas**
   - 5 manchas más grandes de ROI 1
   - 1 mancha más grande de ROI 2
   - Total: 6 manchas por imagen

5. **Procesa manchas**
   - Aplica morphology (closing)
   - Agrega márgenes (padding)
   - Redimensiona a 28×28 píxeles

6. **Exporta resultados**
   - Guarda todas las manchas en ZIP
   - Formato: `imagen_mancha_N.png`

## Funciones Principales

| Función | Descripción |
|---------|-------------|
| `binarizar()` | Convierte a binaria con OTSU |
| `extraer_5_manchas_mas_grandes()` | Extrae manchas ordenadas por posición |
| `procesar_zip()` | Procesa ZIP completo |

## Parámetros Ajustables

ROI (Region of Interest)
roi1 = bin_img[130:250, 220:700] # Región principal
roi2 = bin_img[160:240, 725:770] # Región secundaria

Extracción de manchas
blobs = 5 # Número de manchas a extraer
kernel_size = 3 # Tamaño kernel morphology

Salida
tamaño_salida = 28 # Tamaño final de mancha
margen = 10 # Píxeles de margen

text

## Entrada/Salida

**Entrada:** ZIP con imágenes (JPG/PNG)
**Salida:** ZIP con manchas extraídas (28×28 PNG)

---

**Status:** Activo ✅
**Framework:** OpenCV + NumPy
