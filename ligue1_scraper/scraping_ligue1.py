# scraping_ligue1.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2024-2025"

def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Erreur lors du chargement de la page : {response.status_code}")

def parse_club_table(html):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    
    for table in tables:
        # On cherche le bon tableau par la présence de certaines colonnes
        headers = [th.text.strip() for th in table.find_all("th")]
        if "Club" in headers and "Stade" in headers:
            df = pd.read_html(str(table))[0]
            return df
    return None

def clean_and_export(df):
    df = df.rename(columns=lambda x: x.strip())  # Nettoie les colonnes
    df.to_csv("clubs_ligue1.csv", index=False)
    print("✅ Données sauvegardées dans clubs_ligue1.csv")

def main():
    html = get_page_content(URL)
    df = parse_club_table(html)
    if df is not None:
        clean_and_export(df)
    else:
        print("❌ Tableau des clubs non trouvé.")

if __name__ == "__main__":
    main()
