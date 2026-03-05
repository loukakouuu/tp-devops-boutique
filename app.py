class Produit:
    """Modèle de produit exigé par le TP """
    def __init__(self, id_prod, nom, description, prix, quantite):
        self.id = id_prod
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite = quantite

class GestionBoutique:
    """Logique CRUD pour la gestion des produits """
    def __init__(self):
        self.produits = {}

    def creer(self, produit):
        if produit.id in self.produits:
            return False
        self.produits[produit.id] = produit
        return True

    def lire(self, id_prod):
        return self.produits.get(id_prod)

    def mettre_a_jour(self, id_prod, **kwargs):
        prod = self.lire(id_prod)
        if prod:
            for key, value in kwargs.items():
                if hasattr(prod, key):
                    setattr(prod, key, value)
            return True
        return False

    def supprimer(self, id_prod):
        if id_prod in self.produits:
            del self.produits[id_prod]
            return True
        return False