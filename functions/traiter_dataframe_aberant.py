import pandas as pd

# Traitement du dataframe pour les valeurs abérantes
# Clément 23/09/2022
def traiter_dataframe_aberant(df):
    # On group les prix
    df2 = df["Initialprice"].value_counts()
    # On transforme le dataframe en pourcentage par prix
    df2 = df2 / df2.sum() * 100

    # On met les prix dans l'ordre décroissant
    df2 = df2.reset_index().sort_values(by="index", ascending=False).reset_index(drop=True)

    # On récupère le prix maximun
    dfPrixMaximum = df2['index'][0]
    # On récupère le pourcentage du prix maximum
    dfPrixMaximumPercentage = df2['Initialprice'][0]
    # On récupère le prix minimum
    dfPrixMinimum = pd.Series(df["Initialprice"], name='price').min()

    # Si le prix maximum est supérieur à 3 fois le prix minimum 
    # Et que le pourcentage du prix maximum est inférieur à 10% 
    # On le considère comme abérant
    if( (dfPrixMaximum > 2*dfPrixMinimum) and (dfPrixMaximumPercentage<10) ):
        # On filtre donc tous les prix pour ne plus les avoir dans le dataframe
        df = df[df['Initialprice'] != dfPrixMaximum]

    return df