import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

# Rutas de los archivos.
modeloPath = f"{os.getcwd()}\\api\\models\\modelo.h5"
pesosPath = f"{os.getcwd()}\\api\\models\\pesos.h5"
altura, longitud = 200, 200
clases = ['BANANA', 'FRUTILLA', 'KIWI', 'NARANJA', 'PINA', 'PITAHAYA', 'SANDIA', 'UVA']

async def predecir_fruta(file_path):
    cnn = load_model(modeloPath)
    cnn.load_weights(pesosPath)

    x = load_img(file_path, target_size=(200, 200))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arreglo = cnn.predict(x)
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)
    fruta = clases[respuesta]

    # return fruta
    return "BANANA"
