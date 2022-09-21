import streamlit as st
import pandas as pd
import altair as alt
st.markdown("# Top🔟 les jeux plus chers")

# Chargement des données
dfMin = pd.read_csv('data/min_price_per_game.csv', sep=',', encoding='Latin-1')
dfMax = pd.read_csv('data/max_price_per_game.csv', sep=',', encoding='Latin-1')
dfName = pd.read_csv('data/applicationInformation.csv', sep=',', encoding='Latin-1')

# jointure des deux csv
dfMax = dfMax.merge(dfName, on='appid')
dfMin = dfMin.merge(dfName, on='appid')
# drop des colonnes type
dfMax = dfMax.drop(columns=['type'])
dfMin = dfMin.drop(columns=['type'])
# drop des colonnes release_date
dfMax = dfMax.drop(columns=['releasedate'])
dfMin = dfMin.drop(columns=['releasedate'])
# drop des colonnes freeToPlay
dfMax = dfMax.drop(columns=['freetoplay'])  
dfMin = dfMin.drop(columns=['freetoplay'])
# prix le plus élevé
dfMax = dfMax.sort_values(by=['price'], ascending=False)
# prix le plus bas
dfMin = dfMin.sort_values(by=['price'], ascending=True)
# 10 premiers
dfMax = dfMax.head(10)
dfMin = dfMin.head(10)
# tableau des prix les plus élevés
st.write("Les jeux les plus chers")
dfMax
# tableau des prix les plus bas
st.write("Les jeux les moins chers")
dfMin
# graphique max
st.write("Graphique des 10 jeux les plus chers")
chart = alt.Chart(dfMax).mark_bar().encode(
    x='name',
    y='price',
    color='price',
    tooltip=['name', 'price']
)
st.altair_chart(chart, use_container_width=True)
# graphique min
st.write("Graphique des 10 jeux les moins chers")
chart = alt.Chart(dfMin).mark_bar().encode(
    x='name',
    y='price',
    color='price',
    tooltip=['name', 'price']
)
st.altair_chart(chart, use_container_width=True)
