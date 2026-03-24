from fastapi.testclient import TestClient
from main import app, db

client = TestClient(app)

# On vide la base de données virtuelle avant chaque test pour éviter les conflits
def setup_function():
    db.clear()

def test_create_produit():
    response = client.post("/produits/", json={
        "id": 1, "nom": "Ordinateur", "description": "PC Portable", "prix": 1200.50, "quantite_stock": 10
    })
    assert response.status_code == 201
    assert response.json()["nom"] == "Ordinateur"

def test_create_produit_duplicate_id():
    # Test pour l'erreur 400 (ID déjà pris)
    client.post("/produits/", json={
        "id": 1, "nom": "PC 1", "description": "Desc", "prix": 100, "quantite_stock": 1
    })
    response = client.post("/produits/", json={
        "id": 1, "nom": "PC 2", "description": "Desc", "prix": 200, "quantite_stock": 2
    })
    assert response.status_code == 400

def test_read_produits_empty():
    response = client.get("/produits/")
    assert response.status_code == 200
    assert response.json() == []

def test_read_produit_not_found():
    response = client.get("/produits/999")
    assert response.status_code == 404

def test_update_produit():
    # On crée un produit
    client.post("/produits/", json={
        "id": 1, "nom": "Clavier", "description": "Mécanique", "prix": 50.0, "quantite_stock": 5
    })
    # On le modifie
    response = client.put("/produits/1", json={
        "id": 1, "nom": "Clavier RGB", "description": "Mécanique", "prix": 70.0, "quantite_stock": 2
    })
    assert response.status_code == 200
    assert response.json()["nom"] == "Clavier RGB"

def test_update_produit_not_found():
    # Test l'erreur 404 du PUT
    response = client.put("/produits/999", json={
        "id": 999, "nom": "Inconnu", "description": "X", "prix": 0, "quantite_stock": 0
    })
    assert response.status_code == 404

def test_delete_produit():
    client.post("/produits/", json={
        "id": 1, "nom": "Souris", "description": "Souris sans fil", "prix": 25.0, "quantite_stock": 50
    })
    response = client.delete("/produits/1")
    assert response.status_code == 200
    
    # Vérifier que le produit n'existe plus
    response_get = client.get("/produits/1")
    assert response_get.status_code == 404

def test_delete_produit_not_found():
    # Test l'erreur 404 du DELETE
    response = client.delete("/produits/999")
    assert response.status_code == 404