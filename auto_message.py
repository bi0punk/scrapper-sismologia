import threading
import time
import urllib.request
import pandas as pd
import requests
import datetime
# Tarea a ejecutarse cada determinado tiempo.





def timer():
    while True:
        print("El link usado es: ")
        table_MN = pd.read_html('https://www.sismologia.cl/sismicidad/catalogo/2022/12/20221226.html')
        print(f'Total tables: {len(table_MN)}')
        global df
        df = table_MN[1]
        
        print(df)
        """ df.to_csv('file_name.csv', encoding='utf-8') """
        df.to_csv('datasismos.csv', mode='a', index=False, header=True, encoding='utf-8')
        fecha_data = datetime.datetime.now()
        print("\n")
        print(fecha_data)
        time.sleep(600)   # n segundos.
        
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()
