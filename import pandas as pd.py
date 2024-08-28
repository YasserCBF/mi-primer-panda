import pandas as pd

# Crear el DataFrame inicial
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    'Nota': [8.5, 9.0, 7.5, 8.0]    
}

df = pd.DataFrame(data)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Añadir la nueva columna 'Ciudad' con los valores correspondientes
df['Ciudad'] = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']

# Mostrar el DataFrame actualizado
print(df)

