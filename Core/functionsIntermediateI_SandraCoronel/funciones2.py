# 2. Iterar a traves  de una lista de diccionarios
def iterateDictionary(some_list):
    for diccionario in some_list:
        cadena = ""
        for clave, valor in diccionario.items():
            cadena += f"{clave} - {valor}, "
        print(cadena[:-2]) #elimina la coma

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)
