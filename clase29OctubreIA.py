# Función Sigmoide predicción de aprobación de crédito

# caso puntaje de riesgo  crediticio

import numpy as np
import matplotlib.pyplot as plt

# Función sigmoide
def sigmoid (x):
    return 1 / (1 + np.exp(-x))

# Datos de ejemplo para puntaje de credito de 10 clientes

credit_score = np.array([-8, -4, 0, 2, 5, 7, -6, 3, 10, 2])


# Datos de ejemplo para puntaje entre -10 y 10 para 100 clientes generados aleatoriamente

credit_score_random = np.random.uniform(-10, 10, 100)

# Aplicar la función sigmoide a los puntajes de crédito

#approved_probabilities = sigmoid(credit_score_random)

approved_probabilities = sigmoid(credit_score)

# Visualizar las probabilidades de aprobación de credito


plt.plot(credit_score, approved_probabilities, marker='o', linestyle='-', color='orange')
#plt.plot(credit_score_random, approved_probabilities, marker='o', linestyle='-', color='orange') 
plt.title('Probabilidad de aprobación del crédito')
plt.xlabel('Puntaje de crédito')
plt.ylabel('Probabilidad de aprobación')
plt.legend(['Probabilidad de aprobación'])
plt.grid(True)
plt.show()


print ("probabilidades de aprobación de crédito: ", approved_probabilities)


