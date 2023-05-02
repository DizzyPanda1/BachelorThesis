import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import pickle
from math import log

st.set_page_config(layout='wide', page_title="Mattia Fornasiero's Thesis", page_icon="🅱️")


c1, c2 = st.columns((1,3))
###processing labeled data && getting totals
d = pd.read_csv('finalfr.csv')




###
df = pd.read_csv('final.csv')
dscatter = pd.read_csv('3dscatter.csv')
dtset = pd.read_csv('dataset.csv')

with open('scores.pickle', 'rb') as handle:
    scores = pickle.load(handle)


year = c1.slider("Year", 2017, 2021)
company = c1.radio('Choose the organization', d['name'].unique())

df = d[d.name ==  company]
df = df[df.year == year]
r = df[[
 '1_risk_safety_health',
 '2_sustainability_rights_climate',
 '3_board_directors_remuneration',
 '4_water_waste_impairment',
 '5_emissions_scope_energy',
 '8_tax_taxes_group',
 '9_mobility_transport_sustainable',
 '10_green_bond_green bond',
 '11_circular_circular economy_economy',
 '12_digital_transformation_digital transformation',
 '13_disabilities_people_accessibility',
 '17_leave_maternity_paternity',
 '18_noise_noise pollution_pollution']]
df = pd.DataFrame(dict(
    value = r.loc[:].values.flatten().tolist(),
    variable =[
 '1_risk_safety_health',
 '2_sustainability_rights_climate',
 '3_board_directors_remuneration',
 '4_water_waste_impairment',
 '5_emissions_scope_energy',
 '8_tax_taxes_group',
 '9_mobility_transport_sustainable',
 '10_green_bond_green bond',
 '11_circular_circular economy_economy',
 '12_digital_transformation_digital transformation',
 '13_disabilities_people_accessibility',
 '17_leave_maternity_paternity',
 '18_noise_noise pollution_pollution']))

labels = [
 '1_risk_safety_health',
 '2_sustainability_rights_climate',
 '3_board_directors_remuneration',
 '4_water_waste_impairment',
 '5_emissions_scope_energy',
 '8_tax_taxes_group',
 '9_mobility_transport_sustainable',
 '10_green_bond_green bond',
 '11_circular_circular economy_economy',
 '12_digital_transformation_digital transformation',
 '13_disabilities_people_accessibility',
 '17_leave_maternity_paternity',
 '18_noise_noise pollution_pollution']

fig = px.line_polar(df, r = 'value', theta = 'variable', line_close = True)
fig.update_traces(fill = 'toself')

c2.plotly_chart(fig)

cont = st.container()

l = []

c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = st.columns(13)


contat = 0
for i in [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13]:
    n = labels[contat]
    i.metric(value= round(r[n]*100, 2), label=n)
    contat +=1



fig = px.scatter_3d(
    dscatter, x='x', y='y', z='z',
    color=dscatter.name, hover_data = 'year'
)
fig.update_traces(marker_size=8)

st.plotly_chart(fig)