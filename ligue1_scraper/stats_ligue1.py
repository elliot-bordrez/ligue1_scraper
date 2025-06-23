# stats_ligue1.py

import pandas as pd
import matplotlib.pyplot as plt

# Lire les données
df = pd.read_csv("clubs_ligue1_geo.csv")

# Nettoyage : s'assurer que la colonne capacité est bien en numérique
df["Capacité en L1"] = pd.to_numeric(df["Capacité en L1"], errors="coerce")

# Tri décroissant par capacité
df_sorted = df.sort_values(by="Capacité en L1", ascending=False)

# Plot
plt.figure(figsize=(12, 6))
plt.barh(df_sorted["Club"], df_sorted["Capacité en L1"], color="skyblue")
plt.xlabel("Capacité du stade")
plt.title("Capacité des stades des clubs de Ligue 1")
plt.gca().invert_yaxis()  # Pour avoir le plus grand en haut
plt.tight_layout()

# Sauvegarde
plt.savefig("capacite_stades.png")
plt.show()
