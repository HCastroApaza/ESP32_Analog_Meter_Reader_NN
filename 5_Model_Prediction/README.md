# PASO 5: Predicciones con el Modelo

## Descripción

Notebook que carga el modelo entrenado y realiza predicciones
en imágenes reales del medidor.

## Notebook

- `06_Model_Testing.ipynb` - Pruebas del modelo

## Características

✅ Carga modelo `trained_model.keras`
✅ Prueba en 275 imágenes reales
✅ Genera matriz de confusión
✅ Calcula métricas: Accuracy, Precision, Recall
✅ Exporta predicciones a CSV

## Resultado esperado

**Accuracy: 96.18%** (264/275 dígitos correctos)

## Requisitos

```bash
pip install tensorflow scikit-learn matplotlib pandas
