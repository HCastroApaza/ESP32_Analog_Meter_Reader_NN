# STEP 4: Neural Network Training and Prediction

Notebook to train a neural network on MNIST dataset and perform predictions.

## File

- `04_Neural_Network_Training_and_Prediction.ipynb` - Hyperparameter tuning, training and prediction

## Installation

```bash
pip install tensorflow keras keras-tuner scikit-learn matplotlib numpy pandas
```

## How to Use

```bash
jupyter notebook 04_Neural_Network_Training_and_Prediction.ipynb
```

**Follow these steps:**

1. **Import libraries and MNIST data**
   - Loads MNIST dataset automatically
   - Splits into train (60k), test (5k), validation (5k)

2. **Normalize data**
   - Converts 28×28 images to 784-dimensional array
   - Normalizes values from 0-255 to 0-1
   - Categorizes labels

3. **Optimize hyperparameters**
   - Uses Keras Tuner for search
   - Neuron range: 32-512
   - Learning rates: [0.01, 0.001, 0.0001]
   - **Result:** Units: 160, Learning Rate: 0.001

4. **Train final model**
   - Architecture: 784 → 448 → 224 → 10
   - 108 epochs, batch size 540
   - Validation on hold-out data

5. **Evaluate results**
   - Visualize accuracy vs epochs
   - Get final metrics on test set

6. **Make Predictions** ⭐
   - Predictions on test set
   - Predictions on validation set
   - Predictions on individual images
   - Get predicted class and confidence

## Network Architecture

Input (784) → Dense(448, ReLU) → Dense(224, ReLU) → Output(10, Softmax)

## Parameters

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Loss | Categorical Crossentropy |
| Batch Size | 540 |
| Epochs | 108 |
| Metrics | Accuracy, Precision |

## Expected Results

- **Training Accuracy:** ~99%
- **Validation Accuracy:** ~98%
- **Test Accuracy:** ~98.2%
- **Loss:** < 0.08

---

**Status:** Active ✅
**Framework:** TensorFlow 2.x + Keras
**Prediction:** Enabled ✅
