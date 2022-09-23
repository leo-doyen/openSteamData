import pandas as pd
import streamlit as st

from functions.traiter_dataframe_aberant import traiter_dataframe_aberant

st.set_page_config(
    page_title="Evolution du prix par jeux",
    page_icon="💸",
)

st.markdown("# Evolution du prix des jeux au cours du temps")

# Chargement des données
df = pd.read_csv("data/applicationInformation.csv", sep=",", header="infer", encoding="Latin-1")
# Conversion de l"id en string
df["appid"] = df["appid"].astype(str)
# Recuperation des jeux uniquements payant
df =  df[df['freetoplay'] == 0]
# On affiche la liste des jeux pour filtrer
option = st.selectbox("Quelle jeu voulez vous voir ?", df["name"])
# Résultat du filtre
# st.write("Jeux sélectionné : ", option)

appName = option
appId = df[df["name"] == appName]["appid"].values[0]

if appId != "" and appName != "":
    if st.button("Afficher les graphiques"):
        gameName = df["name"]
        st.markdown("## Graphique des heures de jeux : " + appName)
        imageLocation = "https://cdn.akamai.steamstatic.com/steam/apps/" + appId + "/header.jpg"
        st.markdown("![](" + imageLocation + ")")
        # On récupère le fichier des heures de jeux du jeu sélectionné
        fichierLocation = "data/PriceHistory/" + appId + ".csv"
        df = pd.read_csv(fichierLocation, sep=",", header="infer", encoding="Latin-1")
        
        df = traiter_dataframe_aberant(df)

        df.columns = ['date','initialPrice','finalPrice','discount']

        # On récupere un dataframe avec le prix maximum du jeu
        dfPrixMaximum = df.sort_values('initialPrice', ascending=False).drop_duplicates(['initialPrice']).head(1)

        st.write('Le prix maximum de '+ appName +' est de ' + str(dfPrixMaximum['initialPrice'].values[0]) + '€')
       
        df['date'] = pd.to_datetime(df['date'])

        # st.dataframe(df)
        st.line_chart(df, x='date', y=['finalPrice','initialPrice'])

        # source = data.stocks()

        # lines = (
        #     alt.Chart(source)
        #     .mark_line()
        #     .encode(x="date", y="price", color="symbol")
        # )

        # xrule = (
        #     alt.Chart()
        #     .mark_rule(color="cyan", strokeWidth=2)
        #     # .encode(x=alt.datum(alt.DateTime(year=2006, month="November")))
        # )

        # yrule = (
        #     alt.Chart().mark_rule(strokeDash=[df['finalPrice'], df['initialPrice']], size=2).encode(y=alt.datum(df['date']))
        # )


        # lines + yrule + xrule
        # source = df
        # # source = source.reset_index().melt('date', var_name='category', value_name='y')

        # line_chart = alt.Chart(source).mark_line(interpolate='basis').encode(
        # alt.X('date', title='Year'),
        # alt.Y('finalPrice', title='Amount in liters'),
        # color='category:N'
        # ).properties(
        # title='Sales of consumer goods'
        # )

        # st.altair_chart(line_chart)