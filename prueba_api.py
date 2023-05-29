import requests
import pandas as pd
url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=197794062&pass=5EHIVx6C7vQH&firstdate=2021-01-01&lastdate=2023-05-20&timeseries=F073.TCO.PRE.Z.D&function=GetSeries"
response = requests.get(url)
response = response.json()
response = response ["Series"] ["Obs"]
df_data = pd.DataFrame(response)
df_data.tail(3)

print(df_data.tail(1))
