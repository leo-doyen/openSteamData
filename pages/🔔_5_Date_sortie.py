import streamlit as st
import pandas as pd
import altair as alt

st.markdown("# Les sorties")

# Chargement des données
df = pd.read_csv('data/applicationInformation.csv', sep=',', encoding='Latin-1')
# split de la colonne releasedate
splitCount = df['releasedate'].str.split('-', expand=True)
# compter le nombre de - dans la colonne releasedate
count = df['releasedate'].str.count('-') 
# ajout 01- pour les jeux qu'ils ont un -
df['releasedate'] = df['releasedate'].mask(count == 1, '01-' + splitCount[0] + '-' + splitCount[1])
#supprimer les jeux qui n'ont pas de date de sortie
df = df.dropna(subset=['releasedate'])  
# compter les jeux qui ont la même mois et année de sortie en excluant les jours
splitCount = df['releasedate'].str.split('-', expand=True)
df['Mois'] = splitCount[1]
df['Année'] = splitCount[2]
# sort by année
df = df.groupby(['Mois','Année']).size().reset_index(name='count').sort_values(by=['Année'], ascending=True)
st.write("Graphique des jeux par année de sortie")
chart = alt.Chart(df).mark_bar().encode(
    x='Année',
    y='count',
    color='Année',
    tooltip=['Année', 'count']
)
st.altair_chart(chart, use_container_width=True)
st.write("Graphique des jeux par mois de sortie")
chart = alt.Chart(df).mark_bar().encode(
    x='Mois',
    y='count',
    color='Mois',
    tooltip=['Mois', 'count']
)
st.altair_chart(chart, use_container_width=True)

df