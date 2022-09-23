import pandas as pd
from os import listdir
from os.path import isfile, join

# df = pd.DataFrame([], columns=['appid', 'time'])

# listeFichiers = ["data/PriceHistoty/" + f for f in listdir("data/PriceHistoty") if isfile(join("data/PriceHistoty", f))]

# for file in listeFichiers:
#     print('________________________________')
#     print(file)
    


# df = pd.read_csv('data/Pricehistory/209660.csv', sep=",", header="infer", encoding="Latin-1")


# dfTmp = df.Initialprice.value_counts(normalize=True)

# print(dfTmp)
# df7 = pd.concat([dfTmp], ignore_index=False)

# print(df7)
# maxPrice = df7[0].max()

# # boucle allant de 1 a a1000
# # for i in range(1, 1000):
 



# # get line with the max price
# df8 = df7[df7[0] == maxPrice]

# print(df8)