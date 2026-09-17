import pandas as pd
import folium
import geojson, geopandas, pandas


pop_data = pd.read_csv(
    "insee-pop-communes.csv",
    sep=";",
    dtype={"DEPCOM": str}
)

dpt_code = pop_data["DEPCOM"]

mask = (
    dpt_code.str.startswith("75")
    | dpt_code.str.startswith("77")
    | dpt_code.str.startswith("78")
    | dpt_code.str.startswith("91")
    | dpt_code.str.startswith("92")
    | dpt_code.str.startswith("93")
    | dpt_code.str.startswith("94")
    | dpt_code.str.startswith("95")
)


pop_data = pop_data[mask]

print("Nombre de lignes sélectionnées :", len(pop_data))

coords = (48.7190835, 2.4609723)

carte = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=9
)

folium.Choropleth(
    geo_data="idf.geojson",
    name="choropleth",
    data=pop_data,
    columns=["DEPCOM", "PTOT"],
    key_on="feature.properties.code_commune",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population"
).add_to(carte)

carte.save("map_population.html")