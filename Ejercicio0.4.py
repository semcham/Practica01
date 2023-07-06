"""
Calcular la serie Fibonacci hasta el n-énesimo termino

"""

def fibonacci(n): #creando una funcion para hallar la serie fibonacci de forma recursiva.
    if n==0 : # si ingresamos n =0 nos retornara 0 y si no es cero continua.
        return 0
    elif n==1: #si ingresamos n =1 nos retornara 1 y si no es 1 continua.
        return 1    
    else :
        return fibonacci(n - 1) + fibonacci(n - 2) # lo hacemos por la formula F(n) = F(n-1)  + F (n – 2) ademas tiene que ser  n>=2

def run():

    n = 0 #Inicializando la variable numero "n".
    n = int(input("Introduzca un numero 'n' entero: ")) #Pidiendo al usuario que introduzca un numero entero .

    print("La sucecion de fibonacci hasta el {} termino es:".format(n))#Imprimimos el resultado dando formato al texto.
    for i in range(0,n+1):
        print(fibonacci(i))

if __name__ == "__main__":
    run()