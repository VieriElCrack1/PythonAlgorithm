"""
Palíndromo:
Haz 2 funciones donde reciban un parametro donde se ingrese si la palabra es lo mismo alrevez
ejemplo:
bob = bob -> true
victor = rotciv -> false
"""

def esPalindromo(nombre) :
    palabra = []

    for i in range(0, len(nombre)):
        palabra.append(nombre[i])

    palabraInvertida = []

    for i in range(len(palabra) -1, -1, -1):
        palabraInvertida.append(palabra[i])

    invertida = ""

    for i in range(0, len(palabraInvertida), 1):
        invertida += palabraInvertida[i]

    return print(f"La palabra es un palindromo: {nombre == invertida}")

esPalindromo("ana")