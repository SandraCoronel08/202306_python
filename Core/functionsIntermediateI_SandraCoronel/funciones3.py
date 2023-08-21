#3. Obtener valores de una lista de diccionarios

def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            print(diccionario[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
#
print("Resultados para 'first_name':")
iterateDictionary2('first_name', estudiantes)

print("\nResultados para 'last_name':")
iterateDictionary2('last_name', estudiantes)
