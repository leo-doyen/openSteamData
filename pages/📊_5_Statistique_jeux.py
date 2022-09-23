import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Statistiques sur les jeux",
    page_icon="📊",
)

st.markdown("# Statistiques plateforme, jeux, genre et vente")

# Chargement des données
df = pd.read_csv('data/Video_Games_Sales_as_at_22_Dec_2016.csv', sep=',', encoding='Latin-1')
# Graphique sur les ventes par plateforme
st.write("Graphique des ventes par plateforme")
chart = alt.Chart(df).mark_bar().encode(
    x='Platform',
    y='Global_Sales',
    color='Platform',
    tooltip=['Platform', 'Global_Sales']
)
st.altair_chart(chart, use_container_width=True)
# Graphique sur les ventes par genre
st.write("Graphique des ventes par genre")
chart = alt.Chart(df).mark_bar().encode(
    x='Genre',
    y='Global_Sales',
    color='Genre',
    tooltip=['Genre', 'Global_Sales']
)
st.altair_chart(chart, use_container_width=True)
# Graphique sur les ventes par éditeur de jeu vidéo > 100 millions de ventes
st.write("Graphique des ventes par éditeur de jeu vidéo > 5 millions de ventes")
df2 = df[df['Global_Sales'] > 5]
chart = alt.Chart(df2).mark_bar().encode(
    x='Publisher',
    y='Global_Sales',
    color='Publisher',
    tooltip=['Publisher', 'Global_Sales']
)
st.altair_chart(chart, use_container_width=True)
# Graphique nombre de jeux par plateforme
st.write("Graphique nombre de jeux par plateforme")
df3 = df.groupby(['Platform']).size().reset_index(name='count')
chart = alt.Chart(df3).mark_bar().encode(
    x='Platform',
    y='count',
    color='Platform',
    tooltip=['Platform', 'count']
)
st.altair_chart(chart, use_container_width=True)
# Graphique nombre de jeux par genre
st.write("Graphique nombre de jeux par genre")
df4 = df.groupby(['Genre']).size().reset_index(name='count')
chart = alt.Chart(df4).mark_bar().encode(
    x='Genre',
    y='count',
    color='Genre',
    tooltip=['Genre', 'count']
)
st.altair_chart(chart, use_container_width=True)
# Graphique pourcentage genre par plateforme
st.write("Graphique pourcentage genre par plateforme")
df5 = df.groupby(['Platform', 'Genre']).size().reset_index(name='count')
df5['count'] = df5['count'] / df5.groupby('Platform')['count'].transform('sum')*100
chart = alt.Chart(df5).mark_bar().encode(
    x='Platform',
    y='count',
    color='Genre',
    tooltip=['Platform', 'Genre', 'count']
)
st.altair_chart(chart, use_container_width=True)

