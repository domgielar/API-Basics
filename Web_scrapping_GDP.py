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


#How to CHANGE from Int or float
df2["GDP (Millions USD)"] = df2["GDP (Millions USD)"].astype(int)

#Doing an Equation on a WHOLE column
df2["GDP (Millions USD)"] = df2["GDP (Millions USD)"]/1000

#ROUNDING WHOLE column to 2 decimal places
df2["GDP (Millions USD)"] = np.round(df2["GDP (Millions USD)"], 2)

df2 = df2.rename(columns={"GDP (Millions USD)": "GDP(Billions USD)" })

df2.to_csv("Largest_economies.csv")
df2=pd.read_csv("Largest_economies.csv")
print(df2)