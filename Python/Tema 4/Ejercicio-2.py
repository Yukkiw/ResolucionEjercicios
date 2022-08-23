contador = 2
impar = []

while contador <= 8:
    #print("El contador es ", contador)
    if contador % 2 != 0:
        print("El siguiente número impar: ", contador)
        impar.append(contador)
    contador += 1
    
print(impar)
