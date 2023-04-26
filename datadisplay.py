import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import json
from math import log
c1, c2 = st.columns((1,3))
###processing labeled data && getting totals
d = pd.read_csv('finalfr.csv')




###
df = pd.read_csv('final.csv')
dscatter = pd.read_csv('3dscatter.csv')
dtset = pd.read_csv('dataset.csv')

with open('scores.pickle', 'rb') as handle:
    scores = json.load(handle)


year = c1.slider("Year", 2017, 2021)
company = c1.radio('Choose the organization', d['name'].unique())

df = d[d.name ==  company]
df = df[df.year == year]
r = df[[
 '0_energy_emissions_climate',
 '1_sustainability_risk_rights',
 '2_group_women_training',
 '3_tax_million_income',
 '4_board_suppliers_directors',
 '5_transport_cars_railway',
 '6_cables_cable_general cable',
 '7_customer_customers_satisfaction',
 '9_innovation_patents_patent',
 '10_biodiversity_species_areas',
 '11_green_bond_green bond',
 '12_circular_circular economy_economy',
 '13_digital_transformation_digital transformation']]
df = pd.DataFrame(dict(
    value = r.loc[:].values.flatten().tolist(),
    variable = [
 '0_energy_emissions_climate',
 '1_sustainability_risk_rights',
 '2_group_women_training',
 '3_tax_million_income',
 '4_board_suppliers_directors',
 '5_transport_cars_railway',
 '6_cables_cable_general cable',
 '7_customer_customers_satisfaction',
 '9_innovation_patents_patent',
 '10_biodiversity_species_areas',
 '11_green_bond_green bond',
 '12_circular_circular economy_economy',
 '13_digital_transformation_digital transformation']))

labels = [
 '0_energy_emissions_climate',
 '1_sustainability_risk_rights',
 '2_group_women_training',
 '3_tax_million_income',
 '4_board_suppliers_directors',
 '5_transport_cars_railway',
 '6_cables_cable_general cable',
 '7_customer_customers_satisfaction',
 '9_innovation_patents_patent',
 '10_biodiversity_species_areas',
 '11_green_bond_green bond',
 '12_circular_circular economy_economy',
 '13_digital_transformation_digital transformation']

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
