import threading
import requests
import datetime
import pyttsx3  
import time
import pandas as pd


while True:
    for i in range(1,31):
        print(i)
        
        if i >= 10:
            link_base = f'https://www.sismologia.cl/sismicidad/catalogo/2020/01/202001{i}.html'
            
        else:
            link_base = f'https://www.sismologia.cl/sismicidad/catalogo/2020/01/2020010{i}.html'
            
        

        print("Generando direccion . . . \n")

        response = requests.get(link_base)
        code = (response.status_code)

        if code != 200:
            print("Direccion no disponible esperando . . .")
            time.sleep(60)

        table_MN = pd.read_html(link_base)
        print(f'Total tables: {len(table_MN)}')


        global df
        df = table_MN[1]
        
        print(df)
        """ df.to_csv('file_name.csv', encoding='utf-8') """
        print("Escribiendo data en csv . . .")
        df.to_csv('datasismos.csv', mode='a', index=False, header=True, encoding='utf-8')
        fecha_data = datetime.datetime.now()
        print("\n")

    time.sleep(40) 


