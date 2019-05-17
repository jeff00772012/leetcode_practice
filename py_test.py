import numpy as np
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

station = urlopen('https://sta.ci.taiwan.gov.tw/STA_AirQuality_v2/v1.0/Things?$expand=Locations&$select=name,properties&$count=true&$filter=properties/authority%20eq%20%27%E8%A1%8C%E6%94%BF%E9%99%A2%E7%92%B0%E5%A2%83%E4%BF%9D%E8%AD%B7%E7%BD%B2%27%20and%20substringof(%27%E7%A9%BA%E6%B0%A3%E5%93%81%E8%B3%AA%E6%B8%AC%E7%AB%99%27,name)')
data = urlopen('https://sta.ci.taiwan.gov.tw/STA_AirQuality_v2/v1.0/Datastreams?$expand=Thing,Observations($orderby=phenomenonTime%20desc;$top=1)&$filter=name%20eq%20%27PM2.5%27%20and%20Thing/properties/authority%20eq%20%27%E8%A1%8C%E6%94%BF%E9%99%A2%E7%92%B0%E5%A2%83%E4%BF%9D%E8%AD%B7%E7%BD%B2%27%20and%20substringof(%27%E7%A9%BA%E6%B0%A3%E5%93%81%E8%B3%AA%E6%B8%AC%E7%AB%99%27,Thing/name)&$count=true')
soup_station = BeautifulSoup(station, "lxml")
soup_data=BeautifulSoup(data,'lxml')

dict_station = json.loads(soup_station.text)
dict_data=json.loads(soup_data.text)


#print(dict_station['value'][0]['name'])
#print(dict_station['value'][0]['properties']['areaName'])
#print(dict_station['value'][0]['Locations'][0]['location']['coordinates'])
#print(dict_data['value'][0]['Observations'][0]['result'])
counter = np.zeros((2,6))
for st in range(len(dict_station['value'])) :

    result = dict_data['value'][st]['Observations'][0]['result']

    if dict_station['value'][st]['properties']['areaName'] == "北部空品區" :
          counter[0][0]=counter[0][0]+result
          counter[1][0]=counter[1][0]+1
    elif dict_station['value'][st]['properties']['areaName'] == "竹苗空品區" :
          counter[0][1]=counter[0][1]+result
          counter[1][1]=counter[1][1]+1
    elif dict_station['value'][st]['properties']['areaName'] == "中部空品區" :
          counter[0][2]=counter[0][2]+result
          counter[1][2]=counter[1][2]+1
    elif dict_station['value'][st]['properties']['areaName'] == "雲嘉南空品區" :
          counter[0][3]=counter[0][3]+result
          counter[1][3]=counter[1][3]+1
    elif dict_station['value'][st]['properties']['areaName'] == "高屏空品區" :
          counter[0][4]=counter[0][4]+result
          counter[1][4]=counter[1][4]+1
    elif dict_station['value'][st]['properties']['areaName'] == "其他" :
          counter[0][5]=counter[0][5]+result
          counter[1][5]=counter[1][5]+1

avg_data=counter[0][0:6]/counter[1][0:6]
print(avg_data)
print(counter[1][0:6])
plt.plot(avg_data,'ro')
plt.show()
