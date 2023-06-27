"""
Encontrar la factorial de un numero

"""
def factorial(n):   #creando una funcion para hallar el factorial de forma recursiva.
    if n != 0:  #Si el numero usado como parametro no es 0 la funcion se llamara a si misma.
        resultado = n * factorial(n-1)  #se llamara a la funcion pasando como parametro el numero-1, y multiplicandose por el numero
                                        #obteniendo de esta manera una cadena de multiplicacion n * (n-1) * (n-2) * (n-3)...
    else:
        resultado = 1   #Aqui es donde se rompe la cadena de llamados a la funcion, pues en algun momento "n" sera 0 y el if ya no llamara a la funcion.
    return resultado    #Retornamos el resultado de la multiplicacion es decir el factorial.

def run():

    n = 0   #Inicializando la variable numero "n".
    n = int(input("Introduzca un numero 'n' entero: ")) #Pidiendo al usuario que introduzca un numero.

    resultado = factorial(n)    #Asignando un valor numerico llamando a la funcion factorial el cual devuelve el resultado numerico.

    print("El factorial de {} es {}.".format(n, resultado)) #Imprimimos el resultado dando formato al texto.

if __name__ == "__main__":
    run()