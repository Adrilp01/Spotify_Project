#SPOTIFY  PROJECT

import pandas as pd
import json
import os

folder = "C:/Users/adril/Desktop/Spotify project"
dataframes = []

for x in os.listdir(folder):
    if x.endswith(".json"):
        with open(os.path.join(folder, x), "r", encoding = "utf-8") as r:
            data = json.load(r)
            df = pd.DataFrame(data)
            dataframes.append(df)

df_merged = pd.concat(dataframes, ignore_index = True)


df_merged.to_csv("C:/Users/adril/Desktop/Spotify project/My_Spotify_history.csv", index = False)
