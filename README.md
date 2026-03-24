# API Gestion de Produits - Boutique en ligne

> **Projet de TP DevOps : Intégration Continue, Tests et Analyse de Qualité.**
> Ce projet implémente le Backend (API CRUD) d'une boutique en ligne avec **FastAPI**. Il est entièrement automatisé par un pipeline CI/CD (**Jenkins**) et audité par **SonarQube** pour garantir une qualité de code optimale.

---

## 1. Installation locale

Pour déployer et faire tourner ce projet sur votre machine locale, ouvrez votre terminal et exécutez les commandes suivantes étape par étape :

**1. Cloner le dépôt :**
`git clone https://github.com/VOTRE_NOM_UTILISATEUR/tp-devops-boutique.git`

**2. Créer et activer l'environnement virtuel :**
*Sur Linux / macOS :*
`python3 -m venv venv`
`source venv/bin/activate`

*Sur Windows :*
`python -m venv venv`
`venv\Scripts\activate`

**3. Installer les dépendances requises :**
`pip install -r requirements.txt`

---

## 2. Exécution et Accès à la Boutique

Une fois les installations terminées, lancez le serveur local de l'API avec Uvicorn :
`uvicorn main:app --reload`

Le serveur est maintenant démarré ! L'interaction avec la boutique (création, modification, suppression de produits) se fait via l'interface interactive générée automatiquement :

* **Interface de la boutique (Swagger UI)** : http://127.0.0.1:8000/docs
* **Données brutes (JSON)** : http://127.0.0.1:8000/produits/

---

## 3. Documentation de l'API (CRUD complet)

L'API respecte le standard OpenAPI. Voici les routes disponibles pour gérer le catalogue de la boutique :

| Méthode | Endpoint | Description des fonctionnalités |
| :--- | :--- | :--- |
| `GET` | `/produits/` | Liste tous les produits en stock. |
| `POST` | `/produits/` | Ajoute un nouveau produit (Renvoie une erreur `400` si l'ID existe déjà). |
| `GET` | `/produits/{id}` | Affiche les détails d'un produit spécifique (Renvoie une erreur `404` si introuvable). |
| `PUT` | `/produits/{id}` | Met à jour toutes les informations d'un produit (Renvoie une erreur `404` si introuvable). |
| `DELETE` | `/produits/{id}` | Supprime un produit du catalogue (Renvoie une erreur `404` si introuvable). |

---

## 4. Tests Unitaires et Complexité Locale

Si vous souhaitez lancer les tests manuellement sur votre machine (hors Jenkins) :

* **Lancer les tests et voir la couverture de code :**
`pytest --cov=. --cov-report=term`

* **Analyser la complexité cyclomatique et la maintenabilité (Radon) :**
`radon cc main.py -a`
`radon mi main.py -s`

---

## 5. Pipeline CI/CD (Jenkins)

L'intégration continue est totalement automatisée par le fichier `Jenkinsfile` inclus à la racine du projet. À chaque push sur la branche principale, Jenkins exécute les actions suivantes :

1. **Checkout Code** : Récupération du code source depuis GitHub.
2. **Installation Dépendances** : Création d'un environnement Python isolé (`venv`).
3. **Analyse de Complexité (Radon)** : Vérification de la maintenabilité du code.
4. **Tests Unitaires & Couverture** : Exécution de `pytest` et génération du rapport XML.
5. **Analyse SonarQube** : Scan de sécurité, détection des "Code Smells" et validation du Quality Gate.

---

## 6. Métriques et Qualité du Code (SonarQube)

Grâce à l'application stricte des bonnes pratiques de développement, les derniers scans SonarQube ont validé les métriques suivantes :

* **Couverture de tests (Coverage)** : **95.2%** *(L'objectif initial du TP de 80% est largement dépassé).*
* **Complexité Cyclomatique** : **Grade A** *(Moyenne de 2.33, code hautement maintenable).*
* **Code Smells & Vulnérabilités** : **0** *(Aucun bug, aucune duplication).*