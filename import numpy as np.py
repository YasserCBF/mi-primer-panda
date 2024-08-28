import numpy as np
import pandas as pd

# Crear un array de 5 números aleatorios entre 1 y 10
numeros = np.random.randint(1, 11, size=5)

# Crear el DataFrame df_numeros con la columna 'Numeros'
df_numeros = pd.DataFrame({'Numeros': numeros})

# Añadir la columna 'Dobles' con el doble de cada número en la columna 'Numeros'
df_numeros['Dobles'] = df_numeros['Numeros'] * 2

# Mostrar el DataFrame final
print(df_numeros)
