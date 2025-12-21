import requests
import time
import os
import random
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def seleccionar_carpeta():
    """Abre un diálogo para seleccionar carpeta y retorna la ruta"""
    root = tk.Tk()
    root.withdraw() # Ocultar la ventana principal
    root.attributes('-topmost', True) # Mantener la ventana en primer plano

    # Configurar el diálogo para seleccionar carpeta
    carpeta_seleccionada = filedialog.askdirectory(
        title="Seleccione la carpeta donde guardar las imágenes"
    )

    return carpeta_seleccionada

def capturar_imagenes():
    # Configuración inicial
    url = "http://192.168.1.110//1024x768.jpg"
    num_capturas = 20
    intervalo = 3 # segundos

    # Solicitar ruta de guardado mediante interfaz gráfica
    print("Por favor seleccione la carpeta donde guardar las imágenes...")
    ruta_guardado = seleccionar_carpeta()

    if not ruta_guardado: # Si el usuario cancela
        print("No se seleccionó carpeta. Usando directorio actual.")
        ruta_guardado = os.getcwd()

    print(f"\nLas imágenes se guardarán en: {ruta_guardado}")

    # Capturar imágenes
    nombres_imagenes = []
    for i in range(num_capturas):
        try:
            # Generar nombre único con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            nombre_archivo = f"captura_{timestamp}.jpg"
            ruta_completa = os.path.join(ruta_guardado, nombre_archivo)

            # Descargar imagen
            response = requests.get(url, timeout=10)
            response.raise_for_status() # Verificar si hubo error en la solicitud

            # Guardar imagen
            with open(ruta_completa, "wb") as f:
                f.write(response.content)

            nombres_imagenes.append(ruta_completa)
            print(f"Imagen {i + 1}/{num_capturas} capturada: {nombre_archivo}")

            # Esperar intervalo (excepto en la última captura)
            if i < num_capturas - 1:
                time.sleep(intervalo)

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión al capturar imagen {i + 1}: {str(e)}")
        except Exception as e:
            print(f"Error al capturar imagen {i + 1}: {str(e)}")

    return nombres_imagenes

def mostrar_imagenes_aleatorias(nombres_imagenes, num_mostrar=2):
    """Muestra un número específico de imágenes seleccionadas aleatoriamente"""
    if not nombres_imagenes:
        print("No hay imágenes para mostrar.")
        return

    # Seleccionar imágenes aleatorias
    if len(nombres_imagenes) <= num_mostrar:
        imagenes_a_mostrar = nombres_imagenes
    else:
        imagenes_a_mostrar = random.sample(nombres_imagenes, num_mostrar)

    # Configurar la visualización
    plt.figure(figsize=(8, 4 * num_mostrar))
    plt.suptitle(f"{num_mostrar} Imágenes Aleatorias de las Capturadas", fontsize=14)

    # Mostrar cada imagen en una columna
    for i, img_path in enumerate(imagenes_a_mostrar, 1):
        try:
            img = Image.open(img_path)
            plt.subplot(num_mostrar, 1, i)
            plt.imshow(img)
            plt.axis('off')
            plt.title(f"Imagen {i}: {os.path.basename(img_path)}", fontsize=10)
        except Exception as e:
            print(f"Error al mostrar imagen {img_path}: {str(e)}")

    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.96)) # Ajustar para el título principal
    plt.show()

if __name__ == "__main__":
    # Capturar imágenes
    print("=== Programa de Captura de Imágenes ===")
    imagenes = capturar_imagenes()

    # Mostrar solo 2 imágenes aleatorias
    if imagenes:
        print("\nSeleccionando 2 imágenes aleatorias para mostrar...")
        mostrar_imagenes_aleatorias(imagenes)

    print("\nPrograma finalizado.")