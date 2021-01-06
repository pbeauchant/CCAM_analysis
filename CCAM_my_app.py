import pandas as pd
import plotly.express as px
import streamlit as st

df_2015 = pd.read_excel("Actes_techniques_de_la_CCAM_en_2015.xls", sep=r'\s*,\s*',)
df_2015['Année'] = 2015
df_2016 = pd.read_excel("Actes_techniques_de_la_CCAM_en_2016.xls", sep=r'\s*,\s*',)
df_2016['Année'] = 2016
df_2017 = pd.read_excel("Actes_techniques_de_la_CCAM_en_2017.xls", sep=r'\s*,\s*',)
df_2017['Année'] = 2017
df_2018 = pd.read_excel("Actes_techniques_de_la_CCAM_en_2018.xls", sep=r'\s*,\s*',)
df_2018['Année'] = 2018
df_2019 = pd.read_excel("Actes_techniques_de_la_CCAM_en_2019.xls", sep=r'\s*,\s*',)
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


# Use directly Columns as argument. You can use tab completion for this!
fig = px.scatter(sub_result,x=sub_result['Année'], y=sub_result["Quantité_d_actes"],labels =sub_result["Sous-catégorie_d_acte"],color=sub_result['Code_Acte'])#, size=result["Montants_remboursés"])#,labels=result["Catégorie_d_acte"])
st.plotly_chart(fig) 