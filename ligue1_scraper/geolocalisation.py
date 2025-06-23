# geolocalisation.py

import pandas as pd
import requests
import time

# Charger les données du CSV existant
df = pd.read_csv("clubs_ligue1.csv")

# Nettoyage capacité (supprimer espaces insécables)
df["Capacité en L1"] = df["Capacité en L1"].replace(u"\xa0", "", regex=True).astype(int)

# Créer une adresse à géocoder
df["Adresse"] = df["Stade"] + ", France"

# Fonction de géocodage via Nominatim
def geocode(adresse):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": adresse,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "ligue1-scraper-bot"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        return data[0]["lat"], data[0]["lon"]
    else:
        return None, None

# Appliquer géocodage avec pause pour éviter le bannissement
lats = []
lons = []

print("⏳ Géolocalisation des stades...")

for adresse in df["Adresse"]:
    lat, lon = geocode(adresse)
    lats.append(lat)
    lons.append(lon)
    print(f"✅ {adresse} -> ({lat}, {lon})")
    time.sleep(1)  # Respecte les limites de Nominatim

df["Latitude"] = lats
df["Longitude"] = lons

# Sauvegarde
df.to_csv("clubs_ligue1_geo.csv", index=False)
print("📍 Fichier enregistré : clubs_ligue1_geo.csv")
