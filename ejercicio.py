# Paso 1: Importar bibliotecas

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Paso 2: Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Paso 3: Preprocesar los datos
x_train = x_train.astype('float32') / 255  # Normalización
x_test = x_test.astype('float32') / 255
x_train = x_train.reshape(-1, 28 * 28)     # Aplanar las imágenes
x_test = x_test.reshape(-1, 28 * 28)

y_train = tf.keras.utils.to_categorical(y_train, 10)  # One-hot encoding
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Paso 4: Definir el modelo MLP
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))  # 10 clases de salida

# Paso 5: Compilar el modelo

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Paso 6: Entrenar el modelo

history = model.fit(x_train, y_train, epochs=50, batch_size=128, validation_split=0.2)

# Paso 7: Evaluar el modelo

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Precisión en el conjunto de prueba: {test_acc}')

# Paso 8: Probar el modelo con una imagen del conjunto de prueba

# imagen = x_test[0].reshape(-1, 28 * 28)
# prediccion = model.predict(imagen)
# digit_predicho = np.argmax(prediccion)

# Cargar la imagen
imagen = Image.open('img.png').convert('L')  # Convertir a escala de grises
imagen = imagen.resize((28, 28))  # Cambiar el tamaño a 28x28 píxeles
imagen = np.array(imagen)  # Convertir la imagen a un arreglo numpy
imagen = imagen.astype('float32') / 255  # Normalizar
imagen = imagen.reshape(-1, 28 * 28)  # Aplanar la imagen

# Hacer la predicción
prediccion = model.predict(imagen)
digit_predicho = np.argmax(prediccion)

# Mostrar la imagen y el dígito predicho
plt.imshow(imagen.reshape(28, 28), cmap='gray')
plt.title(f'Predicción: {digit_predicho}')
plt.show()
