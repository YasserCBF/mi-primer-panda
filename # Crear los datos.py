# Crear los datos
nombres = ['Juan', 'Ana', 'Luis', 'Marta']
edades = [15, 14, 16, 15]
notas = [8.5, 9.0, 7.5, 8.0]
ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']

# Crear una lista de diccionarios para simular un DataFrame
data = []
for i in range(len(nombres)):
    data.append({
        'Nombre': nombres[i],
        'Edad': edades[i],
        'Nota': notas[i],
        'Ciudad': ciudades[i]
    })

# Mostrar el "DataFrame"
for row in data:
    print(row)