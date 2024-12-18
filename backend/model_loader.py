import tensorflow as tf

# Charger le modèle existant
model = tf.keras.models.load_model("models/forest_fire_model_dl.h5")

# Convertir en TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Sauvegarder le modèle TFLite
with open("models/forest_fire_model.tflite", "wb") as f:
    f.write(tflite_model)
