from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer CORS
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib

# Initialisation de l'application Flask
app = Flask(__name__)

# Activer CORS pour autoriser les requêtes venant de n'importe quelle origine (ou spécifier ton frontend)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Autorise toutes les origines sur la route /predict

# Charger le modèle Deep Learning
model = load_model("models/forest_fire_model_dl.h5")

# Charger le scaler pour la normalisation
scaler = joblib.load("models/scaler.pkl")  # Sauvegarde du scaler après prétraitement des données

@app.route("/")
def home():
    return "Algerian Forest Fires Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Récupérer les données du formulaire (JSON envoyé par le frontend)
        data = request.json
        features = [
            data["Temperature"],
            data["RH"],
            data["Ws"],
            data["Rain"],
            data["FFMC"],
            data["DMC"],
            data["DC"],
            data["ISI"],
            data["BUI"],
            data["FWI"]
        ]

        # Convertir en array NumPy
        features = np.array(features).reshape(1, -1)

        # Normaliser les données avec le scaler
        features_scaled = scaler.transform(features)

        # Prédire avec le modèle
        prediction = model.predict(features_scaled)

        # Arrondir la prédiction à 0 ou 1
        result = int(prediction[0][0] > 0.5)

        # Retourner la réponse
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)