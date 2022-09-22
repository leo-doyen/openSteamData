import pandas as pd

df = pd.read_csv("data/Video_Games_Sales_as_at_22_Dec_2016.csv", sep=",", header="infer", encoding="Latin-1")

# On garde que les jeux PC
df = df[df["Platform"] == "PC"]
# On supprime la colonne Platform
df = df.drop("Platform", axis=1)

df.to_csv('data/Video_Games_Sales_as_at_22_Dec_2016_Only_Pc.csv', index=False)