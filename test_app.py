import pytest
from app import Produit, GestionBoutique

@pytest.fixture
def boutique():
    return GestionBoutique()

@pytest.fixture
def produit_test():
    return Produit(1, "Clavier", "Clavier mécanique", 50.0, 10)

def test_creer_produit_succes(boutique, produit_test):
    assert boutique.creer(produit_test) is True
    assert boutique.lire(1).nom == "Clavier"

def test_creer_produit_existant(boutique, produit_test):
    boutique.creer(produit_test)
    assert boutique.creer(produit_test) is False

def test_lire_produit_inexistant(boutique):
    assert boutique.lire(99) is None

def test_mettre_a_jour_succes(boutique, produit_test):
    boutique.creer(produit_test)
    assert boutique.mettre_a_jour(1, prix=45.0, quantite=5) is True
    prod = boutique.lire(1)
    assert prod.prix == 45.0
    assert prod.quantite == 5

def test_mettre_a_jour_inexistant(boutique):
    assert boutique.mettre_a_jour(99, prix=10.0) is False

def test_supprimer_succes(boutique, produit_test):
    boutique.creer(produit_test)
    assert boutique.supprimer(1) is True
    assert boutique.lire(1) is None

def test_supprimer_inexistant(boutique):
    assert boutique.supprimer(99) is False