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

def test_read_produits_empty():
    response = client.get("/produits/")
    assert response.status_code == 200
    assert response.json() == []

def test_read_produit_not_found():
    response = client.get("/produits/999")
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