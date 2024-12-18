# Backend - Forest Fire Risk Prediction

## Description
Ce backend Flask expose une API permettant de prédire le risque d'incendie de forêt en utilisant un modèle Machine Learning pré-entraîné.

## Installation
1. Installe Python 3.9 ou supérieur.
2. Clone ce dépôt :
   ```bash
   git clone https://ton-repo.git
   cd backend
3.

Voici une section que tu peux ajouter à ton fichier `README` pour expliquer comment créer un environnement virtuel (`venv`), installer les dépendances nécessaires, et lancer ton application Flask.

---

## Installation et exécution de l'application

### 1. Créer un environnement virtuel

Pour commencer, tu dois créer un environnement virtuel pour gérer les dépendances Python de ton projet. Dans le terminal (ou PowerShell), suis les étapes suivantes :

1. Ouvre ton terminal et navigue jusqu'au répertoire de ton projet :

    ```bash
    cd chemin/vers/ton/projet
    ```

2. Crée un environnement virtuel nommé `venv` :

    - **Sur Windows** :
    
        ```bash
        python -m venv venv
        ```

    - **Sur Mac/Linux** :
    
        ```bash
        python3 -m venv venv
        ```

3. Active l'environnement virtuel :

    - **Sur Windows** :
    
        ```bash
        .\venv\Scripts\activate
        ```

    - **Sur Mac/Linux** :
    
        ```bash
        source venv/bin/activate
        ```

   Une fois l'environnement virtuel activé, tu devrais voir `(venv)` dans ton terminal.

### 2. Installer les dépendances

Avec l'environnement virtuel activé, tu peux maintenant installer toutes les dépendances nécessaires pour faire fonctionner l'application.

1. Installe Flask et les autres bibliothèques :

    ```bash
    pip install Flask numpy tensorflow scikit-learn joblib flask-cors
    ```

   Cette commande installera toutes les bibliothèques suivantes :
   - **Flask** : Framework web pour créer l'API.
   - **NumPy** : Bibliothèque pour la manipulation des matrices et des données numériques.
   - **TensorFlow** : Bibliothèque pour les modèles d'apprentissage automatique et deep learning.
   - **scikit-learn** : Bibliothèque pour les outils d'apprentissage automatique, y compris les prétraitements des données.
   - **joblib** : Utilisé pour la sauvegarde et le chargement des modèles.
   - **flask-cors** : Permet de gérer les requêtes CORS dans Flask (pour autoriser les appels API provenant de différentes origines).

### 3. Lancer l'application Flask

Une fois les dépendances installées, tu peux lancer ton application Flask.

1. Assure-toi que ton environnement virtuel est activé.
2. Dans le terminal, lance le fichier `app.py` avec la commande suivante :

    ```bash
    python app.py
    ```

   L'application devrait maintenant être en fonctionnement et accessible à l'adresse suivante :

   ```
   http://127.0.0.1:5000/
   ```

3. Vérifie que le serveur Flask fonctionne correctement en accédant à cette URL dans ton navigateur. Tu devrais voir la réponse suivante :

   ```
   Algerian Forest Fires Prediction API is running!
   ```
