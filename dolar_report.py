import sqlite3
import requests
import pandas as pd

user = "186978803"
password = "TjqSjcEQJ9kj"

def generate_monthly_report(start_date, end_date):
    url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user={}&pass={}&firstdate={}&lastdate={}&timeseries=F073.TCO.PRE.Z.D&function=GetSeries".format(user, password, start_date, end_date)
    response = requests.get(url)
    response = response.json()
    response = response["Series"]["Obs"]

    df_data = pd.DataFrame(response)
    print(df_data)
     
    
 
    # Crea una conexión a la base de datos SQLite
    conn = sqlite3.connect("monthly_report_dolar_mayo.db")
    
    # Escribir los datos en una tabla de la base de datos
    df_data.to_sql("monthly_report_dolar", conn, if_exists="replace")
    
    # Cierra la conexión a la base de datos
    conn.close()

# Ejecuta la función para generar el reporte mensual
generate_monthly_report("2021-05-01", "2021-05-31")



    