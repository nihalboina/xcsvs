import pandas as pd
import json

country_list = []
town_list = []

with open("api/woeids.json") as f:
    all = json.load(f)


for i in all:
    if i["placeType"]["name"] == "Country":
        country_list.append(i["name"])
    else:
        town_list.append(i["name"])


pd_countries = pd.read_csv("api/old/Cities database.csv")
pd_cities = pd.read_csv("api/old/Countries.csv")

pd_countries_new = pd.DataFrame(columns = list(pd_countries.columns))
pd_cities_new = pd.DataFrame(columns = list(pd_cities.columns) )

for i in range(len(pd_countries)-1,-1,-1):
    if pd_countries.iloc[i].values[1] in country_list:
        print(len(pd_countries_new))
        pd_countries_new.loc[len(pd_countries_new)] = pd_countries.iloc[i]


for i in range(len(pd_cities)-1,-1,-1):
    if pd_cities.iloc[i].values[1] in town_list:
        pd_cities_new.loc[len(pd_cities_new)] = pd_cities.iloc[i]

pd_countries_new.to_csv("api/csvs/countries.csv")
pd_cities_new.to_csv("api/csvs/cities.csv")