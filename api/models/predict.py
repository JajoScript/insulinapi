import os

# Rutas de los archivos.
modeloPath = f"{os.getcwd()}\\api\\models\\modelo.h5"
pesosPath = f"{os.getcwd()}\\api\\models\\pesos.h5"

async def predecir_fruta():
    return "[🐶] Es una fruta del dragon!"

# import os
# import numpy as np
# from keras.preprocessing.image import load_img, img_to_array
# from keras.models import load_model

# altura, longitud = 200, 200
# modelo = 'modelo.h5'  # Cambia esto a la ruta correcta de tu modelo
# pesos = 'pesos.h5'  # Cambia esto a la ruta correcta de tus pesos

# cnn = load_model(modelo)
# cnn.load_weights(pesos)

# def predict_image(file):
#     x = load_img(file, target_size=(200, 200))
#     x = img_to_array(x)
#     x = np.expand_dims(x, axis=0)
#     arreglo = cnn.predict(x)
#     resultado = arreglo[0]
#     respuesta = np.argmax(resultado)

#     clases = ['BANANA', 'FRUTILLA', 'KIWI', 'NARANJA', 'PINA', 'PITAHAYA', 'SANDIA', 'UVA']
#     return clases[respuesta]

# # Nombre del archivo que deseas predecir
# archivo_a_predecir = 'imagen.png'

# # Realizar la predicción para el archivo especificado
# prediccion = predict_image(archivo_a_predecir)

# print(f"Predicción para {archivo_a_predecir}: {prediccion}")