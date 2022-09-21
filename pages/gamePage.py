import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from PIL import Image

st.markdown("# Evolution des heures de jeux au cours du temps")

# Chargement des données
df = pd.read_csv("data/applicationInformation.csv", sep=",", header="infer", encoding="Latin-1")
# Conversion de l"id en string
df["appid"] = df["appid"].astype(str)
# Ajout d"une colonne avec le nom du jeu et son id
df["title"] = df["name"] + "|" + df["appid"]
# Recuperation des jeux uniquements payant
df =  df[df['freetoplay'] == 0]
# On affiche la liste des jeux pour filtrer
option = st.selectbox("Quelle jeu voulez vous voir ?", df["title"])
# Résultat du filtre
st.write("Jeux sélectionné : ", option.split("|")[1] , option.split("|")[0])

appName = option.split("|")[0]
appId = option.split("|")[1]

if appId != "" and appName != "":
    if st.button("Afficher les graphiques"):
        st.markdown("## Graphique des heures de jeux : " + appName)
        imageLocation = "https://cdn.akamai.steamstatic.com/steam/apps/" + appId + "/header.jpg"
        st.markdown("![](" + imageLocation + ")")
        # On récupère le fichier des heures de jeux du jeu sélectionné
        fichierLocation = "data/PriceHistory/" + appId + ".csv"
        df = pd.read_csv(fichierLocation, sep=",", header="infer", encoding="Latin-1")
        
        df.columns = ['date','initialPrice','finalPrice','discount']
        df['date'] = pd.to_datetime(df['date'])

        st.dataframe(df)
        st.line_chart(df, x='date', y=['finalPrice','initialPrice'])

        # source = df
        # # source = source.reset_index().melt('date', var_name='category', value_name='y')

        # line_chart = alt.Chart(source).mark_line(interpolate='basis').encode(
        # alt.X('date', title='Year'),
        # alt.Y('finalPrice', title='Amount in liters'),
        # color='category:N'
        # ).properties(
        # title='Sales of consumer goods'
        # )

        st.altair_chart(line_chart)