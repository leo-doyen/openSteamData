import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from functions.traiter_dataframe_aberant import traiter_dataframe_aberant

st.set_page_config(
    page_title="Top 10",
    page_icon="🔟",
)

st.markdown("# Top🔟")

# Chargement des données
dfMin = pd.read_csv('data/min_price_per_game.csv', sep=',', encoding='Latin-1')
dfMax = pd.read_csv('data/max_price_per_game.csv', sep=',', encoding='Latin-1')
dfName = pd.read_csv('data/applicationInformation.csv', sep=',', encoding='Latin-1')

# colonne price to Initialprice
dfMin = dfMin.rename(columns={'price': 'Initialprice'})
dfMax = dfMax.rename(columns={'price': 'Initialprice'})

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
dfMax = dfMax.sort_values(by=['Initialprice'], ascending=False)
# prix le plus bas
dfMin = dfMin.sort_values(by=['Initialprice'], ascending=True)
# 10 premiers
dfMaxTop10 = dfMax.head(10)
dfMinTop10 = dfMin.head(10)
# tableau des prix les plus élevés
st.write("Les jeux les plus chers")
dfMaxTop10
# tableau des prix les plus bas
st.write("Les jeux les moins chers")
dfMinTop10
# graphique max
st.write("Graphique des 10 jeux les plus chers")
chart = alt.Chart(dfMaxTop10).mark_bar().encode(
    x='name',
    y='Initialprice',
    color='Initialprice',
    tooltip=['name', 'Initialprice']
)
st.altair_chart(chart, use_container_width=True)
# graphique min
st.write("Graphique des 10 jeux les moins chers")
chart = alt.Chart(dfMinTop10).mark_bar().encode(
    x='name',
    y='Initialprice',
    color='Initialprice',
    tooltip=['name', 'Initialprice']
)
st.altair_chart(chart, use_container_width=True)

# nombre de jeux par prix   
st.write("Graphique nombre de jeux par prix")
df3 = dfMin.groupby(['Initialprice']).size().reset_index(name='count')

chart = alt.Chart(df3).mark_bar().encode(
    x='Initialprice',
    y='count',
    color='count',
    tooltip=['Initialprice', 'count']
)
st.altair_chart(chart, use_container_width=True)

# nombre de jeux par prix entre 0 et 20 
st.write("Graphique nombre de jeux par prix entre 0 et 20 $")
df4 = dfMin[dfMin['Initialprice'] < 20]
df4 = df4.groupby(['Initialprice']).size().reset_index(name='count')
chart = alt.Chart(df4).mark_bar().encode(
    x='Initialprice',
    y='count',
    color='count',
    tooltip=['Initialprice', 'count']
)
st.altair_chart(chart, use_container_width=True)

# Camembert de jeux par prix entre 0 et 20
st.write("Camembert nombre de jeux par prix entre 0 et 20 $")
df5 = dfMin[dfMin['Initialprice'] < 20]
df5 = df5.groupby(['Initialprice']).size().reset_index(name='count')
df5 = df5.sort_values(by=['count'], ascending=False)

fig1, ax1 = plt.subplots()
ax1.pie(df5['count'], labels=df5['Initialprice'], autopct='%1.1f%%',  startangle=90)
ax1.axis('equal') 

st.pyplot(fig1)