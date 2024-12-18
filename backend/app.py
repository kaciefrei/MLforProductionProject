from flask import Flask, request, jsonify
import numpy as np
import tflite_runtime.interpreter as tflite
from flask_cors import CORS

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)

# Charger le modèle TFLite
interpreter = tflite.Interpreter(model_path="models/forest_fire_model.tflite")
interpreter.allocate_tensors()

# Récupérer les détails des entrées et sorties
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Fonction de prédiction
def predict(features):
    # Mettre en forme les données pour l'entrée
    features = np.array(features, dtype=np.float32).reshape(input_details[0]['shape'])
    
    # Passer les données au modèle
    interpreter.set_tensor(input_details[0]['index'], features)
    interpreter.invoke()

    # Récupérer le résultat
    prediction = interpreter.get_tensor(output_details[0]['index'])
    return prediction

@app.route("/")
def home():
    return "Algerian Forest Fires Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict_route():
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

        # Appeler la fonction de prédiction
        prediction = predict(features)

        # Arrondir la prédiction à 0 ou 1
        result = int(prediction[0][0] > 0.5)

        # Retourner la réponse
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
