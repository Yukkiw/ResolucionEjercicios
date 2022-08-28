import time
import pprint

#pprint.pprint(dir(time))
def laboral():
    hora = time.strftime('%I')
    minutos = time.strftime('%M')

    print(hora,":",minutos)

    if int(hora) >= 7:
        print("Es hora de ir a casa")
    else:
        print("Quedan {} horas y {} minutos para irnos a casa".format(6 - int(hora), 59 - int(minutos)))

laboral()