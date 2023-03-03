import threading
import requests
import datetime
import pyttsx3  
import time
import pandas as pd
from playsound import playsound
from gtts import gTTS

while True:
    for i in range(1,32):

        dia = i
        print(dia)
        
        print("\nGenerando direccion . . . ")
        time.sleep(1)

        

        
        if i >= 10:
            link_base = f'https://www.sismologia.cl/sismicidad/catalogo/2020/01/202001{i}.html'
            
        else:
            link_base = f'https://www.sismologia.cl/sismicidad/catalogo/2020/01/2020010{i}.html'

        print(f'La direccion generada es {link_base} ')
        response = requests.get(link_base)
        code = (response.status_code)
        print(f'Codigo de respuesta: {code}')
        time.sleep(1)
        if code != 200:
            print("Direccion no disponible esperando . . .")
            time.sleep(60)
        print("Obteniendo informacion . . .")
        table_MN = pd.read_html(link_base)
        #print(f'Total tables: {len(table_MN)}')

        df = table_MN[1]
        
        info = (df.head())
        print(info)
        """ df.to_csv('file_name.csv', encoding='utf-8') """
        print("\nEscribiendo data en csv . . .")
        df.to_csv('datasismos.csv', mode='a', index=False, header=True, encoding='utf-8')
        fecha_data = datetime.datetime.now()
        time.sleep(1)
        if i == 32:
            tts = gTTS('Secuencia enero terminada')
            tts.save('speak.mp3')
            playsound('speak.mp3')
            break

        print("\n")



