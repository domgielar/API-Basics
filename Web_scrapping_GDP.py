import requests
import numpy as np 
import pandas as pd 
from bs4 import BeautifulSoup


url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


response = requests.get(url, verify=False)
data = pd.read_html(response.text)
df=data[2]
#print(df)
df.columns=range(df.shape[1])
print(df)
