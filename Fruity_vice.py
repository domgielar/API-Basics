import requests
import json
import pandas as pd 



data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)
pd.DataFrame(results)

df2 = pd.json_normalize(results)
#print(df2)

#cherry=df2.loc[df2["name"]=="Cherry"]
#print((cherry.iloc[0]["family"]), (cherry.iloc[0]["genus"]))

#cherry = df2.loc[df2["name"] == 'Cherry']
#print((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus']))

#banana = df2.loc[df2["name"]=="Banana"]
#print((banana.iloc[0]["name"]), (banana.iloc[0]["nutritions.calories"]))

data2= requests.get("https://official-joke-api.appspot.com/jokes/ten")

loaded = json.loads(data2.text)
pd.DataFrame(loaded)

df3 = pd.json_normalize(loaded)
df3.drop(columns=["type","id"],inplace=True)
print(df3)

# Inplace changes the the original dataFramce. 
