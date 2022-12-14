import pandas as pd
from os import listdir
from os.path import isfile, join

from functions.traiter_dataframe_aberant import traiter_dataframe_aberant

df = pd.DataFrame([], columns=['appid', 'price'])

listeFichiers = ["data/PriceHistory/" + f for f in listdir("data/PriceHistory") if isfile(join("data/PriceHistory", f))]

for file in listeFichiers:
    print(file)
    fileDataframe = pd.read_csv(file, sep=",", header="infer", encoding="Latin-1")
    fileDataframe = traiter_dataframe_aberant(fileDataframe)
    price = fileDataframe['Initialprice'].max()

    appid = file.split("/")[2].split(".")[0]

    df2 = pd.DataFrame([[appid, price]], columns=['appid', 'price'])
    df = pd.concat([df, df2], ignore_index=True)

df.to_csv('data/max_price_per_game.csv', index=False)