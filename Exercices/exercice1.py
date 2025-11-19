# Saluer une personne
from datetime import *

# Fonction pour obtenir le nom
def name(nom):
    return f"{nom}"

# Fonction pour obtenir l'heure actuelle
def heure():
    heure_actuelle = int(datetime.today().strftime("%H"))
    return heure_actuelle

# Variables pour stocker le nom et l'heure
nom = input("Entrez votre nom: ") # Demande du prenom de l'utilisateur
h = heure()

# Programme principale avec les conditions pour saluer en fonction de l'heure

if 6 <= h < 12:
    print("Bonjour " + name(nom))

elif 12 <= h < 18:
    print("Bon après-midi " + name(nom))

elif 18 <= h < 22:
    print("Bonsoir " + name(nom))

else:
    print("Bonne nuit " + name(nom))

