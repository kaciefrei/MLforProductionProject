import mlflow
import mlflow.keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np
import os

MLFLOW_TRACKING_URI = "https://dagshub.com/kaciefrei/MLforProductionProject.mlflow"
MLFLOW_USERNAME = "kaciefrei"
MLFLOW_TOKEN = "39830c587d2cb958defd76237cff4f58652cc101"
MLFLOW_EXPERIMENT_NAME = "Forest Fire Prediction" 

os.environ["MLFLOW_TRACKING_USERNAME"] = MLFLOW_USERNAME
os.environ["MLFLOW_TRACKING_PASSWORD"] = MLFLOW_TOKEN


mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

def create_model(input_dim):
    """Créer et retourner le modèle Keras."""
    model = Sequential()
    model.add(Dense(10, input_dim=input_dim, activation='relu'))

    for _ in range(10):
        model.add(Dense(16, activation='relu'))

    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return model

def train_and_log_model(X_train, y_train, X_test, y_test):
    """Entraîner et suivre le modèle avec MLFlow."""

    experiment = mlflow.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME)
    if experiment is None:
        mlflow.create_experiment(MLFLOW_EXPERIMENT_NAME)
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)


    with mlflow.start_run():

        X_train_scaled = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
        X_test_scaled = (X_test - np.mean(X_test, axis=0)) / np.std(X_test, axis=0)


        model = create_model(input_dim=X_train_scaled.shape[1])


        history = model.fit(
            X_train_scaled, y_train,
            epochs=20,
            batch_size=32,
            validation_data=(X_test_scaled, y_test),
            verbose=1
        )


        mlflow.log_param("input_dim", X_train_scaled.shape[1])
        mlflow.log_param("epochs", 20)
        mlflow.log_param("batch_size", 32)


        for epoch, (loss, val_loss, acc, val_acc) in enumerate(
            zip(
                history.history['loss'],
                history.history['val_loss'],
                history.history['accuracy'],
                history.history['val_accuracy']
            )
        ):
            mlflow.log_metric("loss", loss, step=epoch)
            mlflow.log_metric("val_loss", val_loss, step=epoch)
            mlflow.log_metric("accuracy", acc, step=epoch)
            mlflow.log_metric("val_accuracy", val_acc, step=epoch)


        model_path = "models/forest_fire_model_dl"
        mlflow.keras.log_model(model, artifact_path=model_path)

        print(f"Model and metrics have been logged to MLFlow at {MLFLOW_TRACKING_URI}.")

if __name__ == "__main__":

    X_train = np.random.rand(1000, 20)
    y_train = np.random.randint(0, 2, 1000)
    X_test = np.random.rand(200, 20)
    y_test = np.random.randint(0, 2, 200)

    train_and_log_model(X_train, y_train, X_test, y_test)
