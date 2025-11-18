# Verfifie le mot de passe

def est_mot_de_passe_valide(mot_de_passe):
    # Vérifie si le mot de passe a au moins 8 caractères, une majuscule, une minuscule et un chiffre
    if (len(mot_de_passe) < 8): # longueur minimale
        return False
    if not any(c.isupper() for c in mot_de_passe): # isupper verifie la majuscule
        return False      
    if not any(c.islower() for c in mot_de_passe): # islower verifie la minuscule
        return False
    if not any(c.isdigit() for c in mot_de_passe): # isdigit verifie le chiffre
        return False
    return True 

password = input("Entrez votre mot de passe : ")


# entré du mot de passe pour verification
if est_mot_de_passe_valide(password):
    print("mot de passe valide.")

else: print("mot de passe invalide.")