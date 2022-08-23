kg = input('Ingresar su peso en Kg: ')
metro = input('Ingresar su estatura en Metros: ')

resultado = round(float(kg)/float(metro)**2,2)
print('Tu índice de masa corporal es: ' + str(resultado))