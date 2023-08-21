# 1. Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Aqui cambia el valor 10 en x a 15
x[1][0] = 15

#y aqui el "apellido" del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant'

# cambia "Messi" por "Andrés"
directorio_deportes['futbol'][0] = 'Andrés'

# Cambia el valor 20 en z a 30
z[0]['y'] = 30

# Imprimo para ver mis results de una forma mas organizada..
print("x actualizado:", x)
print("intercambio de nombres:", estudiantes)
print("directorio deport ahora:", directorio_deportes)
print("z ahora:", z)


