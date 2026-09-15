import requests
import json
import urllib.parse
import folium
import urllib.parse

def construire_url(adresse):
    """Construit les paramètres d'une URL de géocodage.

    >>> construire_url("Paris")
    'q=Paris'

    >>> construire_url("Noisy le Grand")
    'q=Noisy+le+Grand'
    """
    parametres = {"q": adresse}
    return urllib.parse.urlencode(parametres)

api_url = "https://data.geopf.fr/geocodage/search/"
adresse = "2, boulevard Blaise Pascal, 93160 Noisy le Grand"

parametres = {
    "q": adresse
}

url = api_url + "?" + urllib.parse.urlencode(parametres)

reponse = requests.get(url)

texte_json = reponse.content.decode("utf8")
donnees = json.loads(texte_json)

coordonnees = donnees["features"][0]["geometry"]["coordinates"]

longitude = coordonnees[0]
latitude = coordonnees[1]

print("Longitude :", longitude)
print("Latitude :", latitude)

coords = (latitude, longitude)

carte = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=15
)
folium.Marker(location=coords, popup = "ESIEE Paris").add_to(carte)
carte.save(outfile="map.html")