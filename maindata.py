
import time
import pyttsx3  
import threading


def timer():
    while True:
        day = 0 
        year = None
        month = None
        link = f'Este es el enlace, el dia a consultar es {day}'
        print(link)
        dia = 0    
        semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

        #entra a cilco while interno y no se detenie hasta que se cumpla o asigne una condicion dada
        while dia < 7:
            print("Hoy es " + semana[dia])
            dia = dia + 1
            time.sleep(2)
            """ time.sleep(600)  """  # n segundos.
        
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()
