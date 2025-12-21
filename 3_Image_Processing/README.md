# STEP 3: Preprocessing

Notebook to process and extract blobs from meter images.

## File

- `03_Preprocessing.ipynb` - Binarization and blob extraction

## Installation

```bash
pip install opencv-python numpy matplotlib tqdm
```

## How to Use

```bash
jupyter notebook 03_Preprocessing.ipynb
```

**Follow these steps:**

1. **Load images**
   - Upload ZIP file with JPG/PNG images
   - Extracts automatically

2. **Binarize images**
   - Converts to grayscale
   - Applies automatic threshold (OTSU)

3. **Define regions of interest (ROI)**
   - ROI 1: Main region [130:250, 220:700]
   - ROI 2: Secondary region [160:240, 725:770]

4. **Extract blobs**
   - 5 largest blobs from ROI 1
   - 1 largest blob from ROI 2
   - Total: 6 blobs per image

5. **Process blobs**
   - Applies morphology (closing)
   - Adds padding margins
   - Resizes to 28×28 pixels

6. **Export results**
   - Saves all blobs in ZIP
   - Format: `image_blob_N.png`

## Main Functions

| Function | Description |
|----------|-------------|
| `binarizar()` | Converts to binary with OTSU |
| `extraer_5_manchas_mas_grandes()` | Extracts blobs ordered by position |
| `procesar_zip()` | Processes complete ZIP |

## Adjustable Parameters

**ROI (Region of Interest)**

```python
roi1 = bin_img[130:250, 220:700]  # Main region
roi2 = bin_img[160:240, 725:770]  # Secondary region
```

**Blob Extraction**

```python
blobs = 5           # Number of blobs to extract
kernel_size = 3     # Morphology kernel size
```

**Output**

```python
tamaño_salida = 28  # Final blob size
margen = 10         # Padding pixels
```

## Input/Output

**Input:** ZIP with images (JPG/PNG)
**Output:** ZIP with extracted blobs (28×28 PNG)

---

**Status:** Active ✅
**Framework:** OpenCV + NumPy
