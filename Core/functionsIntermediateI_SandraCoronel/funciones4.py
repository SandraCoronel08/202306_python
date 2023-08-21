# 4. Iterar a través de un diccionarios con valores de lista

# dojo = {
#     'ubicaciones': ['San Jose', 'Seatle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 
# 'Burbank'],
#     'instructores': ['Michael', 'Any', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)
# # salida
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORES
# Michael
# Any 
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
def printInfo(some_dict):
    for clave, lista in some_dict.items():
        print(len(lista), clave.upper())
        for valor in lista:
            print(valor)

dojo = {
    'ubicaciones': ['San Jose', 'Seatle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Any', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
