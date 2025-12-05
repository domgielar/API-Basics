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

#How to Capture specific columns in DataFrames
df2 =pd.DataFrame(df[[0,2]])


#How to ACCESS rows in dataFrames
df2 =df2.iloc[1:11]

#How to CHANGE COLUMNS
df2.columns =["Country", "GDP (Millions USD)"]
print(df2)


