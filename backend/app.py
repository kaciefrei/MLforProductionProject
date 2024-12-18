from flask import Flask, request, jsonify
import joblib  # Si tu exportes ton modèle sous forme de fichier pickle
import numpy as np

app = Flask(__name__)

# Charger ton modèle ML pré-entraîné
model = joblib.load("forest_fire_model.pkl")  # Change le chemin selon l'emplacement réel

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données JSON du frontend
        data = request.json
        features = [
            data['Temperature'], data['RH'], data['Ws'], data['Rain'], 
            data['FFMC'], data['DMC'], data['DC'], data['ISI'], 
            data['BUI'], data['FWI']
        ]
        
        # Convertir en numpy array pour le modèle
        features_array = np.array(features).reshape(1, -1)
        
        # Faire une prédiction
        prediction = model.predict(features_array)
        risk_level = "High" if prediction[0] > 0.5 else "Low"  # Exemple de logique
        
        return jsonify({"risk_level": risk_level, "prediction_value": float(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)