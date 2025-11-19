# Calculatrice de prix

def calculer_prix_ttc(prix_ht, taux_tva): # Fonction pour calculer le prix TTC
    
    # prend en paramètre le prix hors taxe et la TVA
    prix_ttc = prix_ht * (1 + taux_tva / 100) # Calcul du prix TTC
    return round(prix_ttc, 2)

# Demander à l'utilisateur le prix HT et le taux de TVA
try:
    prix_ht = float(input("Entrez le prix hors taxe (HT) : ")) 
    taux_tva = float(input("Entrez le taux de TVA (en %) : "))

    # Calculer le prix TTC
    prix_ttc = calculer_prix_ttc(prix_ht, taux_tva)

    # Afficher le résultat
    print(f"Le prix toutes taxes comprises (TTC) est : {prix_ttc} €")

# retour d'erreur
except ValueError:                 
    print("Valeur non valide.")
