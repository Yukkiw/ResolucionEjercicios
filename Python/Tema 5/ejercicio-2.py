def es_primo():
    numero = int(input('Introduce un número entero: '))

    if numero > 1:
        for i in range (2, numero):
            if (numero % i == 0):
                print(numero, " - No es primo", i, "es divisor")
                return False
        print("Es primo", numero)
        return True
    else:
        print("Los números primos son mayores que 1")

es_primo()