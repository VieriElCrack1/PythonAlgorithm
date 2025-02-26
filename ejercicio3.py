'''
Crea una funcion a la cual le pase un array de numeros y un numero
que será el resultado de la suma de dos de los valores

Ejemplos:
sumarDos([3,7,8,2], 10) //[3,7] ambos suman 10
'''

def sumarDos(numeros, resultado):
    #recorrer el array de numeros
    for i in range(0, len(numeros), 1):
        #Calculo, para sacar el segundo numero para devolver
        primeroNumero = numeros[i]
        segundoNumero = resultado - primeroNumero
        
        #Comprobar si existe un segundo numero en el array que sumado al actual
        #sea igual al resultado esperado y comprobar tambien que la variable segundoNumero
        #el valor es distinto al numero actual que estoy recorriendo
        if segundoNumero != primeroNumero:
            resultado = [primeroNumero, segundoNumero]
            print(resultado)
            return resultado
    
    
sumarDos([3,7,8,1],10)
