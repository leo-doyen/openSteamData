import pandas as pd
from os import listdir
from os.path import isfile, join

df = pd.DataFrame([], columns=['appid', 'price'])

listeFichiers = ["data/PriceHistory/" + f for f in listdir("data/PriceHistory") if isfile(join("data/PriceHistory", f))]

for file in listeFichiers:
    print(file)
    fileDataframe = pd.read_csv(file, sep=",", header="infer", encoding="Latin-1")
    price = fileDataframe['Initialprice'].max()
    print(price)

    appid = file.split("/")[2].split(".")[0]
    print(appid)

    df2 = pd.DataFrame([[appid, price]], columns=['appid', 'price'])
    print(df2)
    df = pd.concat([df, df2], ignore_index=True)

print(df)
df.to_csv('out.csv', index=False)