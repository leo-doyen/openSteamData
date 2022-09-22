import streamlit as st
import math
import matplotlib.pyplot as plt
import os
import pandas as pd

st.markdown("# Répartition du nombre d'heures de jeu cumulées sur tous les jeux steam")

tags=pd.read_csv(r'data/applicationTags.csv', sep=',',header=None, encoding='Latin-1')
hours=pd.read_csv(r'data/hours_total_per_game.csv', sep=',',header='infer', encoding='Latin-1')
nom=pd.read_csv(r'data/applicationInformation.csv', sep=',',header='infer', encoding='Latin-1')
tags[1] = tags[1].fillna("_")
tags[2] = tags[2].fillna("_")
tags[3] = tags[3].fillna("_")
tags[4] = tags[4].fillna("_")
tags[5] = tags[5].fillna("_")
tags[6] = tags[6].fillna("_")
tags[7] = tags[7].fillna("_")
tags[8] = tags[8].fillna("_")
tags[9] = tags[9].fillna("_")
tags[10] = tags[10].fillna("_")
tags[11] = tags[11].fillna("_")
tags[12] = tags[12].fillna("_")
tags[13] = tags[13].fillna("_")
tags[14] = tags[14].fillna("_")
tags[15] = tags[15].fillna("_")
tags[16] = tags[16].fillna("_")
tags[17] = tags[17].fillna("_")
tags[18] = tags[18].fillna("_")
tags[19] = tags[19].fillna("_")
tags[20] = tags[20].fillna("_")
tags[1]= tags[1]+","+ tags[2]+","+ tags[3]+","+ tags[4]+","+ tags[5]+","+ tags[6]+","+ tags[7]+","+ tags[8]+","+ tags[9]+","+ tags[10]+","+ tags[11]+","+ tags[12]+","+ tags[12]+","+ tags[14]+","+ tags[15]+","+ tags[16]+","+ tags[17]+","+ tags[18]+","+ tags[19]+","+ tags[20]
tags = tags.drop([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], axis=1)
tags[1] = tags[1].str.replace(',_', '')
tags[1] = tags[1].str.replace('_', '')
tags=tags[tags[1].str.contains(' ')]
tags.columns = ['idx', 'tags']
hours.columns = ['idx', 'hours']
nom.columns=['idx','type','name','releasedate','freetoplay']
final = tags.merge(hours, left_on='idx', right_on='idx')

final2 = final.merge(nom, left_on='idx', right_on='idx')
final2.drop('type', inplace=True, axis=1)
final2.drop('releasedate', inplace=True, axis=1)
final2.drop('freetoplay', inplace=True, axis=1)
# final2=final2.sort_values(by=['idx'], ascending=True)
final2=final2.sort_values(by='hours',ascending=False)

time_autre=final2.iloc[3:].hours.sum(axis=0)

hour_graph=final2.sort_values(by='hours',ascending=False).iloc[:3]

autre={'idx':0, 'tags':'other', 'hours':time_autre, 'name':'autre'}

hour_graph=hour_graph.append(autre,ignore_index=True)


fig1, ax1 = plt.subplots()
ax1.pie(hour_graph['hours'], labels=hour_graph['name'], autopct='%1.1f%%', startangle=90)
ax1.axis('equal') 

st.pyplot(fig1)

