# liste de course

# fonction pour afficher la liste
def afficher_liste(liste):
    for article in liste:
        print("- " + article)
    return

# fonction pour ajouter un article à la liste
def ajouter_article(liste, article):
    liste.append(article)
    sauvegarder_liste(liste)
    return

# fonction pour retirer un article
def retirer_article(liste, article):
    if article in liste :
        liste.remove(article)
        print("- " + article)
        sauvegarder_liste(liste)
    return 

# fonction pour compter le nombre d'article
def compter_articles(liste):
    return len(liste)

# fonction pour sauvegarder la liste dans le fichier
def sauvegarder_liste(liste):
    with open('liste.txt', 'w', encoding='utf-8') as f:
        for item in liste:
            f.write(item + '\n')


# Programme principale
try:
    with open('liste.txt', 'r', encoding='utf-8') as f:
        liste_courses = [ligne.strip() for ligne in f.readlines()]
except FileNotFoundError:
    liste_courses = []

while True:
    print("Nombre d'article : " + str(compter_articles(liste_courses)))   
    action = input("Ajouter (a), Retirer (r), Afficher (f) ou Quitter (q) ").lower() # liste d'entrée

    # les conditions 
    if action == "a":                                   # si 'a' taper alors on peut ajouter un article
        article = input("Entrez l'article à ajouter: ").strip()
        if article:
            ajouter_article(liste_courses, article)         # envoie de l'input dans liste_courses
    elif action == "r":                                 # si 'r' taper alors on peut supprimer l'article
        article = input("Entrez l'article à supprimer: ").strip()
        if article:
            retirer_article(liste_courses, article)
    elif action == "f":                                 # si 'f' taper alors on affiche la liste
        afficher_liste(liste_courses) 

    elif action == "q":                                # si 'q' taper alors on quitte
        print("Au revoir!")
        break

    # exeption en cas de probleme
    else:
        print("Action non reconnue, veuillez réessayer.")
        continue