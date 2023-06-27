"""
Determinar la sumatoria para los primeros n numeros impares
"""

def run():

    n = 0   #Inicializando la variable numero "n".
    n = int(input("Introduzca un numero 'n' entero: "))     #Pidiendo al usuario que introduzca un numero.

    sumatoria = n**2    #Usamos la formula para sumar los primeros "n" numeros impares naturales.

    print("la suma de los {} primeros numeros impares naturales es {}.".format(n, sumatoria))   #Imprimimos el resultado dando formato al texto.

if __name__ == "__main__":
    run()





