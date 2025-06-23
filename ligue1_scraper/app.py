from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Charger les données une fois au démarrage
df = pd.read_csv("clubs_ligue1_geo.csv")

@app.route('/api/clubs', methods=['GET'])
def get_clubs():
    # Convertir le DataFrame en liste de dictionnaires JSON-friendly
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
