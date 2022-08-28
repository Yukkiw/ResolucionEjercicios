class Alumno:
    #Inicializamos los atributos
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    #Imprimir los datos
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    #Funcion para obtener los resultados
    def resultados(self):
        if self.nota < 5:
            print("El Alumno ha Suspendido")
        else:
            print("El Alumno ha Aprobado")
# bloque principal
# creamos los nuevos objetos
alumno1 = Alumno()
alumno2 = Alumno()

# inicializamos los atributos
alumno1.inicializar("Maria",7)
alumno2.inicializar("Maifre",1)

# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultados()

alumno2.imprimir()
alumno2.resultados()