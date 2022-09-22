import streamlit as st
import pandas as pd
import requests

st.markdown("# Statistique par joueur")

userId = st.text_input("Entrer un id utilisateur", "")

if(userId != ""):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=236BCFFB4BA51FFFC8B24AFF935C39A9&include_appinfo=1&include_played_free_games=0&appids_filter&steamid=" + userId
    resp = requests.get(url=url)
    data = resp.json()
    listOfPlayeddGame = pd.DataFrame.from_dict(data.get("response").get("games"))
    if(listOfPlayeddGame.empty):
        st.markdown("Profil privé ou aucun jeu trouvé")
    else:
        listOfPlayeddGame['playtime_forever'] = listOfPlayeddGame['playtime_forever'].apply(lambda x: x / 60)
        st.dataframe(listOfPlayeddGame)

        topTenOfPlayedGame = listOfPlayeddGame.sort_values(by=['playtime_forever'], ascending=False).head(10)

        st.bar_chart(topTenOfPlayedGame, x='name', y='playtime_forever')  

        # Nombre d'heure de jeux total
        total = listOfPlayeddGame["playtime_forever"].sum()
        st.markdown("## Total des heures de jeux : " + str(total))
        st.markdown("## Total des jours de jeux : " + str(total/24))
        st.markdown("## Total des années de jeux : " + str(total/24/365))