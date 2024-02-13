import pandas as pd 
import requests
from bs4 import BeautifulSoup

year= 2024       # set year 
season= "winter" # set season => [winter,spring,summer,fall]
url='https://myanimelist.net/anime/season/{}/{}'.format(str(year),season)

list_name_anime=[]
list_description_anime=[]
list_studio_anime=[]

res=requests.get(url,timeout=5) # res => response

if (res.status_code == requests.codes.not_found):
  print('Not Found !!!')
else:
  print('Found :)')

html_data=BeautifulSoup(res.text,'html')
name_anime_html_data=html_data.find_all('a',{"class":"link-title"})
description_anime_html_data=html_data.find_all('p',{"class":"preline"}) 
studio_anime_html_data=html_data.select('div.properties') 

for i in range(len(name_anime_html_data)):
  list_name_anime.append(name_anime_html_data[i].text)

for i in range(len(description_anime_html_data)):
  text_del_n=(description_anime_html_data[i].text).replace(r"\n", "")
  text_del_r=text_del_n.replace(r"\r", "")
  list_description_anime.append(text_del_r.replace("\r\n\r\n",""))

for i in range(len(studio_anime_html_data)):
  list_studio_anime.append(studio_anime_html_data[i].select('div.property')[0].select('span.item')[0].text)

dict_data = {'Name': list_name_anime, 'Description': list_description_anime, 'Studio': list_studio_anime} 
    
anime_df = pd.DataFrame(dict_data)

anime_df.to_csv("result.csv",index=False)   # write csv file