import pandas as pd
from os import listdir
from os.path import isfile, join

df = pd.DataFrame([], columns=['appid', 'time'])

print(df)

listeFichiers = ["data/PlayerCountHistory/" + f for f in listdir("data/PlayerCountHistory") if isfile(join("data/PlayerCountHistory", f))]
# print(listeFichiers)
for file in listeFichiers:
    print(file)
    print(listeFichiers[0])
    fileDataframe = pd.read_csv(file, sep=",", header="infer", encoding="Latin-1")
    Total = fileDataframe['Playercount'].sum()
    print(file.split("/")[2].split(".")[0])
    appid = file.split("/")[2].split(".")[0]
    print(Total)
    df2 = pd.DataFrame([[appid, Total]], columns=['appid', 'time'])
    print(df2)
    df = pd.concat([df, df2], ignore_index=True)

print(df)
df.to_csv('out.csv', index=False)