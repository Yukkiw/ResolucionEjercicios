import operaciones

def main():
    suma = operaciones.suma(2,2)
    resta = operaciones.restar(5,3)
    multi = operaciones.multiplicar(5,5)
    divi = operaciones.dividir(6,2)

    print("La Suma es: ", suma)
    print("La Resta es: ", resta)
    print("La Multiplicación es: ", multi)
    print("La Divisón es: ", divi)

if __name__ == '__main__':
    main()

