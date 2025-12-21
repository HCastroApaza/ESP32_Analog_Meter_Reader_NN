# PASO 4: Crear y Entrenar Red Neuronal

## Descripción

Dos notebooks para crear y entrenar la red neuronal:

1. `04_Hyperparameter_Tuning.ipynb` - Buscar parámetros óptimos
2. `05_Neural_Network_Training.ipynb` - Entrenar modelo final

## Notebooks

### 04_Hyperparameter_Tuning.ipynb

Usa Keras Tuner para encontrar:
- Número óptimo de neuronas (32-512)
- Tasa de aprendizaje óptima (1e-2, 1e-3, 1e-4)

**Resultado esperado:**
- Units: 448
- Learning Rate: 0.001

### 05_Neural_Network_Training.ipynb

Entrena la red neuronal final con arquitectura 448-224-10:
- Entrada: 784 (28×28 aplanado)
- Hidden 1: 448 (ReLU)
- Hidden 2: 224 (ReLU)
- Output: 10 (Softmax - dígitos 0-9)

**Resultado esperado:**
- Test Accuracy: 98.37%

## Requisitos

```bash
pip install tensorflow keras keras-tuner scikit-learn matplotlib
