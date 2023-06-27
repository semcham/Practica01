"""
Calcular la serie Fibonacci hasta el n-énesimo termino

"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def run():

    n = 0
    n = int(input("Introduzca un numero 'n' entero: "))

    print("La sucecion de fibonacci hasta el {} termino es:".format(n))
    for i in range(n):
        print(fibonacci(i))

if __name__ == "__main__":
    run()