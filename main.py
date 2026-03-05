from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Boutique en ligne - API Produits",
    description="API CRUD pour la gestion des produits de la boutique."
)

# Modèle de données du produit
class Produit(BaseModel):
    id: int
    nom: str
    description: str
    prix: float
    quantite_stock: int

# Base de données simulée (en mémoire)
db: List[Produit] = []

@app.post("/produits/", response_model=Produit, status_code=201)
def create_produit(produit: Produit):
    for p in db:
        if p.id == produit.id:
            raise HTTPException(status_code=400, detail="Un produit avec cet ID existe déjà")
    db.append(produit)
    return produit

@app.get("/produits/", response_model=List[Produit])
def read_produits():
    return db

@app.get("/produits/{produit_id}", response_model=Produit)
def read_produit(produit_id: int):
    for p in db:
        if p.id == produit_id:
            return p
    raise HTTPException(status_code=404, detail="Produit non trouvé")

@app.put("/produits/{produit_id}", response_model=Produit)
def update_produit(produit_id: int, produit_maj: Produit):
    for i, p in enumerate(db):
        if p.id == produit_id:
            db[i] = produit_maj
            return produit_maj
    raise HTTPException(status_code=404, detail="Produit non trouvé")

@app.delete("/produits/{produit_id}")
def delete_produit(produit_id: int):
    for i, p in enumerate(db):
        if p.id == produit_id:
            del db[i]
            return {"message": "Produit supprimé avec succès"}
    raise HTTPException(status_code=404, detail="Produit non trouvé")