import pandas as pd
import folium
import geojson, geopandas, pandas
import json


# Lecture des données de population
pop_data = pd.read_csv(
    "insee-pop-communes.csv",
    sep=";", dtype={"DEPCOM": str}
)
pop2_data=pd.read_csv("parisdonnees.csv", sep=";",dtype={"Code INSEE": str})

# Récupération des codes des communes
dpt_code = pop_data["DEPCOM"]
dpt_code2 = pop2_data["Code INSEE"]

# Sélection des communes d’Île-de-France
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

mask2 = (
    dpt_code2.str.startswith("75")
    & (
        dpt_code2.str.endswith("01")
        | dpt_code2.str.endswith("02")
        | dpt_code2.str.endswith("03")
        | dpt_code2.str.endswith("04")
        | dpt_code2.str.endswith("05")
        | dpt_code2.str.endswith("06")
        | dpt_code2.str.endswith("07")
        | dpt_code2.str.endswith("08")
        | dpt_code2.str.endswith("09")
        | dpt_code2.str.endswith("10")
        | dpt_code2.str.endswith("11")
        | dpt_code2.str.endswith("12")
        | dpt_code2.str.endswith("13")
        | dpt_code2.str.endswith("14")
        | dpt_code2.str.endswith("15")
        | dpt_code2.str.endswith("16")
        | dpt_code2.str.endswith("17")
        | dpt_code2.str.endswith("18")
        | dpt_code2.str.endswith("19")
        | dpt_code2.str.endswith("20")
    )
)

# Application du filtre
pop_data = pop_data[mask]
pop2_data = pop2_data[mask2]

print("Nombre de lignes sélectionnées :", len(pop_data))
print("Nombre de lignes sélectionnées :", len(pop2_data))

paris_geojson = {
    "type": "FeatureCollection",
    "features": []
}

for _, arrondissement in pop2_data.iterrows():
    paris_geojson["features"].append({
        "type": "Feature",
        "geometry": json.loads(arrondissement["geo_shape"]),
        "properties": {
            "code_commune": arrondissement["Code INSEE"]
        }
    })
    
# Création de la carte
coords = (48.7190835, 2.4609723)

# Lecture du GeoJSON d’Île-de-France
with open("idf.geojson", "r", encoding="utf-8") as fichier:
    idf_geojson = json.load(fichier)

# Lecture du GeoJSON des arrondissements de Paris
with open("arrondissements.geojson", "r", encoding="utf-8") as fichier:
    paris_geojson = json.load(fichier)

# Suppression de Paris entier (75056) du GeoJSON francilien
idf_geojson["features"] = [
    feature
    for feature in idf_geojson["features"]
    if feature["properties"]["code_commune"] != "75056"
]

# Ajout des 20 arrondissements
idf_geojson["features"].extend(
    paris_geojson["features"]
)

# Résultat fusionné
geo_data = idf_geojson

carte = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=9
)

# Création de la carte choroplèthe
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

folium.Choropleth(
    geo_data=paris_geojson,
    name="Arrondissements de Paris",
    data=pop_data,
    columns=["DEPCOM", "PTOT"],
    key_on="feature.properties.code_commune",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.5
).add_to(carte)

carte.save("map_population.html")
print(pop_data[pop_data["DEPCOM"] == "75056"])