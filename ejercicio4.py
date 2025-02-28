"""
Enunciado Ejercicio 4:
Crea una funcion que convierta un número romano en un número decimal.

Ejemplos:
- Si el número romano es "III" debería devolver 3.
- Si el número romano es "IV" debería devolver 4.

romanoAEntero("XVIII") => 18
romanoAEntero("CXX") => 120
"""

def romanoAEntero(romano):

    #Crear un objeto con numero romanos y sus correspondientes valores numercios
    valoresRomanos = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    #almacenar el resultado
    resultado = 0

    #recorrer el parametro que se ingresará
    for i in range(0, len(romano), 1):
        #print(romano[i], valoresRomanos[romano[i]])
        
        '''
        si la letra actual es la ultima o si el valor del siguiente caracter
        es menor o igual al de la actual, entonces añadimos el valor al "resultado"
        '''
        if i == len(romano) - 1 or valoresRomanos[romano[i + 1]] <= valoresRomanos[romano[i]]:
             resultado += valoresRomanos[romano[i]]
        else:
            resultado -= valoresRomanos[romano[i]]
        
    return resultado

print(romanoAEntero("XXX")) #14