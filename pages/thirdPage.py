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
        # On calcule la totalité des heures de jeux
        total = df["Playercount"].sum()
        st.markdown("## Total des heures de jeux : " + str(total))
        # Nombre d'heures pour construire la tour Eiffel 2 ans, 2 mois et 5 jours
        nbHourToBuildEiffelTower = 2 * 365 * 24 + 2 * 30 * 24 + 5 * 24
        # Nombre d'heures pour construire une maison 10 mois
        nbHourToBuildHouse = 10 * 30 * 24
        # Nombre d'heures pour assembler un airbus a320 4 jours
        nbHourToBuildAirbusA320 = 4 * 24
        # Nombre d'heures pour construire la Grande Pyramide de Gizeh 20 ans, 4 mois et 5 jours
        nbHourToBuildGreatPyramidOfGiza = 20 * 365 * 24 + 4 * 30 * 24 + 5 * 24
        # Nombre d'heures de vie moyenne d'un humain 80 ans
        nbHourToLive = 80 * 365 * 24

        # On affiche le nombre de Tour Eiffel que l'on aurait pu construire
        st.markdown("## Nombre de Tour Eiffel que l'on aurait pu construire : " + str(int(total / nbHourToBuildEiffelTower)))
        # On affiche le nombre de maison que l'on aurait pu construire
        st.markdown("## Nombre de maison que l'on aurait pu construire : " + str(int(total / nbHourToBuildHouse)))
        # On affiche le nombre d'Airbus A320 que l'on aurait pu construire
        st.markdown("## Nombre d'Airbus A320 que l'on aurait pu construire : " + str(int(total / nbHourToBuildAirbusA320)))
        # On affiche le nombre de Grande Pyramide de Gizeh que l'on aurait pu construire
        st.markdown("## Nombre de Grande Pyramide de Gizeh que l'on aurait pu construire : " + str(int(total / nbHourToBuildGreatPyramidOfGiza)))
        # On affiche le nombre de vie que l'on aurait pu vivre
        st.markdown("## Nombre de vie que l'on aurait pu vivre : " + str(int(total / nbHourToLive)))