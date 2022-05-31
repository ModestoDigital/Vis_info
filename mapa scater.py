import plotly.express as px
import pandas as pd
import json

data = pd.read_csv("olist_geolocation_dataset.csv",usecols=["geolocation_state"])
data.rename(columns={"geolocation_state":"estados"},inplace = True)
ndata = data.value_counts().rename_axis("estados").reset_index(name="vendas");

geojson = json.load(open("brasil_estados.json"))
fig = px.scatter_geo(ndata, geojson=geojson,locations="estados", size = "vendas", scope="south america")

fig.write_html('Mapa_vendas_por_estado_scatter.html', auto_open=True)