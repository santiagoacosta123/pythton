def decorador(funcion):
    def nueva_funcion():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return nueva_funcion
    
@decorador
def saludar():
    print("Hola")

saludar()



import time
from datetime import datetime

def decorador(funcion):
    def nueva_funcion():
        inicio = datetime.now()
        print("Hora de inicio:", inicio.strftime("%H:%M:%S"))

        tiempo_inicio = time.time()

        funcion()

        tiempo_fin = time.time()
        fin = datetime.now()

        print("Hora de fin:", fin.strftime("%H:%M:%S"))
        print("Tiempo transcurrido:", tiempo_fin - tiempo_inicio, "segundos")

    return nueva_funcion


@decorador
def saludar():
    print("Hola")
    time.sleep(2)   

saludar()