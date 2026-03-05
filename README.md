# tp-devops-boutique
# API Gestion de Produits - Boutique en ligne

Ce projet est une API backend développée en Python (FastAPI) pour la gestion CRUD des produits d'une boutique en ligne. Il inclut un pipeline CI complet (Jenkins) avec analyse de code (SonarQube, Radon) et tests unitaires (Pytest).

## 🚀 Installation locale

1. Cloner le dépôt.
2. Créer un environnement virtuel : `python3 -m venv venv`
3. Activer l'environnement : `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Installer les dépendances : `pip install -r requirements.txt`

## ⚙️ Exécution

Lancer le serveur de développement :
`uvicorn main:app --reload`

L'API sera disponible sur `http://127.0.0.1:8000`.

## 📚 Documentation de l'API

Une fois le serveur lancé, la documentation interactive générée automatiquement (Swagger) est accessible à l'adresse :
`http://127.0.0.1:8000/docs`

## 🧪 Tests et Qualité
- **Tests** : Lancer `pytest`
- **Couverture** : Lancer `pytest --cov=.`
- **Complexité** : Lancer `radon cc main.py -a`