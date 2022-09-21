import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("# Evolution des heures de jeux au cours du temps")

# Chargement des données
df = pd.read_csv("data/applicationInformation.csv", sep=",", header="infer", encoding="Latin-1")
# Conversion de l"id en string
df["appid"] = df["appid"].astype(str)
# Ajout d"une colonne avec le nom du jeu et son id
df["title"] = df["name"] + "|" + df["appid"]
# On affiche la liste des jeux pour filtrer
option = st.selectbox("Quelle jeu voulez vous voir ?", df["title"])
# Résultat du filtre
st.write("Jeux sélectionné : ", option.split("|")[0])

appName = option.split("|")[0]
appId = option.split("|")[1]

if appId != "" and appName != "":
    if st.button("Afficher les graphiques"):
        st.markdown("## Graphique des heures de jeux : " + appName)
        imageLocation = "https://cdn.akamai.steamstatic.com/steam/apps/" + appId + "/header.jpg"
        st.markdown("![](" + imageLocation + ")")
        # On récupère le fichier des heures de jeux du jeu sélectionné
        fichierLocation = "data/PlayerCountHistory/" + appId + ".csv"
        df = pd.read_csv(fichierLocation, sep=",", header="infer", encoding="Latin-1")
        # On convertit la colonne Time du type object en datetime
        df['Time'] = pd.to_datetime(df['Time'])
        # On convertit la colonne Time du format datetime en date
        df["Time"] = df["Time"].dt.strftime("%Y-%m-%d")
        # On regroupe les heures par jours pour avoir un dataframe plus petit
        df = df.groupby("Time").sum().reset_index()
        # On affiche le dataframe en tableau
        st.dataframe(df)
        # On affiche le dataframe en courbe
        st.line_chart(df, x='Time', y=['Playercount'])