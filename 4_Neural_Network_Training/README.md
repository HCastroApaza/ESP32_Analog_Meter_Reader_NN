# PASO 4: Neural Network Training

Notebook para entrenar una red neuronal en dataset MNIST.

## Archivo

- `04_Neural_Network_Training.ipynb` - Hiperparameter tuning y entrenamiento

## Instalación

pip install tensorflow keras keras-tuner scikit-learn matplotlib numpy pandas

text

## Cómo Usar

jupyter notebook 04_Neural_Network_Training.ipynb

text

**Sigue estos pasos:**

1. **Importa librerías y datos MNIST**
   - Carga el dataset MNIST automáticamente
   - Divide en train (60k), test (5k), validation (5k)

2. **Normaliza datos**
   - Convierte imágenes de 28×28 a array 784 dimensiones
   - Normaliza valores de 0-255 a 0-1
   - Categoriza etiquetas

3. **Optimiza hiperparámetros**
   - Usa Keras Tuner para búsqueda
   - Rango neuronas: 32-512
   - Tasas de aprendizaje: [0.01, 0.001, 0.0001]
   - **Resultado:** Units: 160, Learning Rate: 0.001

4. **Entrena modelo final**
   - Arquitectura: 784 → 448 → 224 → 10
   - 108 épocas, batch size 540
   - Validación en datos hold-out

5. **Evalúa resultados**
   - Visualiza accuracy vs epochs
   - Obtén métricas finales en test set

## Arquitectura de la Red

Input (784) → Dense(448, ReLU) → Dense(224, ReLU) → Output(10, Softmax)

text

## Parámetros

| Parámetro | Valor |
|-----------|-------|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Loss | Categorical Crossentropy |
| Batch Size | 540 |
| Epochs | 108 |
| Métricas | Accuracy, Precision |

## Resultados Esperados

- **Training Accuracy:** ~99%
- **Validation Accuracy:** ~98%
- **Loss:** < 0.08

---

**Status:** Activo ✅
**Framework:** TensorFlow 2.x + Keras
