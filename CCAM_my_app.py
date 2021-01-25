import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df_2015 = pd.read_csv("Actes_techniques_de_la_CCAM_en_2015.csv",delimiter=';')
df_2015['Année'] = 2015
df_2016 = pd.read_csv("Actes_techniques_de_la_CCAM_en_2016.csv",delimiter=';')
df_2016['Année'] = 2016
df_2017 = pd.read_csv("Actes_techniques_de_la_CCAM_en_2017.csv",delimiter=';')
df_2017['Année'] = 2017
df_2018 = pd.read_csv("Actes_techniques_de_la_CCAM_en_2018.csv",delimiter=';')
df_2018['Année'] = 2018
df_2019 = pd.read_csv("Actes_techniques_de_la_CCAM_en_2019.csv",delimiter=';')
df_2019['Année'] = 2019

frames = [df_2015,df_2016,df_2017, df_2018,df_2019]
result = pd.concat(frames)

result.columns = result.columns.str.replace('^ +| +$', '')
result.columns = result.columns.str.replace(' ', '_')
result.columns = result.columns.str.replace('\'', '_')
result = result.fillna(0)
st.markdown('# Explorer la base de données de la CCAM de 2015 à 2019')
st.markdown('----')
code = st.text_input("Entrer le Code Acte","DZQM006")
sub_result = result[result['Code_Acte']==code]
st.markdown('Ce code acte correspond au libellé :')
st.markdown("***{}***".format(sub_result['Libellé_long'].iloc[0]))
st.markdown('----')
st.dataframe(sub_result)

CAGR = np.round(((sub_result['Libellé_long'].iloc['Année'==2019]/sub_result['Libellé_long'].iloc['Année'==2015])^(1/4)-1)*100,2)
# Use directly Columns as argument. You can use tab completion for this!
st.markdown("***CAGR 2015-2019: {}***".format(CAGR))
fig = px.scatter(sub_result,x='Année', y="Quantité_d_actes")
st.plotly_chart(fig) 
