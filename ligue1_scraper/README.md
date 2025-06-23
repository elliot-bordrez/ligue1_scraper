# Projet Web Scraping & Carte Interactive : Clubs de Ligue 1

## Description

Ce projet vise à automatiser la collecte d’informations sur les clubs de football de Ligue 1 française via du web scraping, puis à visualiser ces données sous forme d’une carte interactive et de graphiques statistiques. Une API Flask expose aussi les données en JSON.

---

## Fonctionnalités

- **Scraping** des données clubs depuis Wikipédia (clubs, stades, entraîneurs, classements, etc.)  
- Nettoyage et structuration des données dans un fichier CSV/JSON  
- Géolocalisation des stades pour création d’une carte interactive avec Folium  
- Filtrage interactif des clubs par capacité du stade  
- Visualisation statistique des capacités des stades sous forme de graphique  
- API Flask simple exposant les données au format JSON  

---

## Structure du projet

- `scraping_ligue1.py` : script de web scraping et nettoyage  
- `clubs_ligue1_geo.csv` : fichier CSV des données enrichies  
- `carte_interactive.py` : génération de la carte interactive HTML  
- `stats_ligue1.py` : création des graphiques statistiques  
- `app.py` : API Flask exposant les données  
- `ligue1_map.html` : carte interactive générée  
- `README.md` : ce fichier  
- `notebook_demo.ipynb` : notebook Jupyter de démonstration 

---

## Installation

1. Cloner le dépôt  
```bash
git clone <URL_DU_DEPOT>
cd ligue1_scraper

2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Installer les dépendances
pip install -r requirements.txt

## Utilisation

1. Lancer le script de scraping pour récupérer les données (optionnel si le CSV est déjà fourni) :
python scraping_ligue1.py

2. Générer la carte interactive :
python carte_interactive.py

3. Générer les graphiques statistiques :
python stats_ligue1.py

4. Lancer l’API Flask :
python app.py

5. Ouvrir la carte interactive dans un navigateur :
ligue1_map.html

6. Accéder à l’API JSON :
http://127.0.0.1:5000/api/clubs

## Choix techniques

Requests + BeautifulSoup pour le scraping web (fiabilité et simplicité)
Pandas pour le traitement et nettoyage des données
Folium pour la carte interactive (intégration facile de Leaflet.js)
Matplotlib pour les graphiques statistiques simples et lisibles
Flask pour exposer une API légère et facilement extensible

## Améliorations possibles

Ajout d’un filtre par région sur la carte
Intégration de budgets et classements dans les graphiques
Interface web complète avec Flask + frontend JS
Mise à jour automatique périodique des données