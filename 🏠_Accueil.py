import streamlit as st

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
)

st.markdown("![](https://indigobuzz.fr/wp-content/uploads/2018/11/steam-logo.jpg)")
st.markdown("# Accueil")
st.warning("Cette application est en cours de développement. Certaines pages peuvent ne pas fonctionner correctement.")

st.write("## Open Data Steam")
st.write("#### Ce projet a pour but de récupérer des données sur Steam et de les analyser.")
st.write("#### Certaines données sont récupérées grâce à l'API de Steam et d'autre par fichiers csv.")
st.write("#### Les fichiers csv sont récupérées sur https://data.mendeley.com/datasets/ycy3sy3vj2/1.")
st.write("#### Les données sont ensuite analysées et visualisées grâce à Streamlit.")
st.write("#### Notre projet est disponible sur [GitHub] https://github.com/leo-doyen/openSteamData.")
st.write("#### Notre equipe est composée de: Clément, Léo, Nolan et Guillaume.")

st.write("## 📄 Nos pages")
st.write("### [📅 Date de sortie](5_Date_sortie)")
st.info("##### Cette page permet de voir le nombre de jeux qui ont été sortis par mois et par année.")

st.write("### [📈 Evolution heure par jeux](3_Evolution_heure_par_jeux)")
st.info("##### Cette page permet de voir l'évolution du nombre d'heure par jeux.")

st.write("### [💸 Evolution prix par jeux](6_Evolution_prix_par_jeux)")
st.info("##### Cette page permet de voir le prix de jeux qui ont été sortis par mois et par année ainsi que leur prix remisé.")

st.write("### [🥇 Statistiques par joueurs](4_Statistique_par_joueur)")
st.info("##### Cette page permet de voir les statistiques par joueurs.")

st.write("### [🔟 Top 10](1_Top_10)")
st.info("##### Cette page permet de voir les 10 jeux les plus chers et les moins chers.")