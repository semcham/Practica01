"""
Determinar la sumatoria para los primeros n numeros
naturales
"""
def run():

    n = 0   #Inicializando la variable numero "n".
    n = int(input("Introduzca un numero 'n' natural: "))    #Pidiendo al usuario que introduzca un numero.

    sumatoria = (n*(n+1))/2 #Usando la formula para lo suma de los "n" primeros numero naturales.

    print("la suma de los {} primeros numeros naturales es {}.".format(n, sumatoria))   #Imprimimos el resultado dando formato al texto.

if __name__ == "__main__":
    run()
