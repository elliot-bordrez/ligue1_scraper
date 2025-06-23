# carte_interactive.py

import pandas as pd
import folium

# Charger le CSV enrichi
df = pd.read_csv("clubs_ligue1_geo.csv")

# Filtrer les clubs avec coordonnées valides
df = df.dropna(subset=["Latitude", "Longitude"])

# Nettoyer la capacité (en entier)
df["Capacité en L1"] = pd.to_numeric(df["Capacité en L1"], errors="coerce")

# Créer la carte centrée sur la France
m = folium.Map(location=[46.8, 2.5], zoom_start=6, tiles="CartoDB positron")

# Création des groupes par capacité
petit_stades = folium.FeatureGroup(name="Capacité < 20 000")
moyen_stades = folium.FeatureGroup(name="20 000 - 40 000")
grand_stades = folium.FeatureGroup(name="Capacité > 40 000")

# Ajout des points dans les groupes
for _, row in df.iterrows():
    popup_text = f"<strong>{row['Club']}</strong><br>Stade : {row['Stade']}<br>Capacité : {row['Capacité en L1']}"
    marker = folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.7,
        popup=folium.Popup(popup_text, max_width=300)
    )
    if row["Capacité en L1"] < 20000:
        petit_stades.add_child(marker)
    elif 20000 <= row["Capacité en L1"] <= 40000:
        moyen_stades.add_child(marker)
    else:
        grand_stades.add_child(marker)

# Ajouter les groupes à la carte
m.add_child(petit_stades)
m.add_child(moyen_stades)
m.add_child(grand_stades)

# Ajouter contrôle des couches (pour filtrer)
m.add_child(folium.LayerControl())

# Sauvegarde en HTML
m.save("ligue1_map.html")
print("✅ Carte générée : ligue1_map.html")
