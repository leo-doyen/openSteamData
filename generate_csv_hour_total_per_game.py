import pandas as pd
from os import listdir
from os.path import isfile, join

df = pd.DataFrame([], columns=['appid', 'time'])

listeFichiers = ["data/PlayerCountHistory/" + f for f in listdir("data/PlayerCountHistory") if isfile(join("data/PlayerCountHistory", f))]

for file in listeFichiers:
    print(file)
    fileDataframe = pd.read_csv(file, sep=",", header="infer", encoding="Latin-1")
    total = fileDataframe['Playercount'].sum()

    appid = file.split("/")[2].split(".")[0]

    df2 = pd.DataFrame([[appid, total]], columns=['appid', 'time'])
    df = pd.concat([df, df2], ignore_index=True)

df.to_csv('data/hours_total_per_game.csv', index=False)