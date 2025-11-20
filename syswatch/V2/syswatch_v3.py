"""
SysWatch v3.0 - Export et collecte continue
"""

import collector
import csv
import json
import time
import sys
from datetime import datetime

def export_csv(metrique, fichier='syswatch.csv'):
    """
    Exporte les métriques dans un fichier CSV.
    """
    import os

    # Ligne de données
    ligne = {
        # Appel des metriques
        'timestamp': metrique['timestamp'],
        'hostname': metrique['systeme']['hostname'],
        'cpu_percent': metrique['cpu']['utilisation'],
        'mem_total_gb': metrique['memoire']['total'] / (1024**3),
        'mem_dispo_gb': metrique['memoire']['disponible'] / (1024**3),
        'mem_percent_gb': metrique['memmoire']['pourcentage']
    }

    # Ajout disque racine si dispo
    for disque in metrique['disque']:
        if disque['point_montage'] in ['/', 'C:\\']:    # Point de montage Windows ou linux
            ligne['disk_root_percent'] = disque['pourcentage']
            break
    else:
        ligne['ddisk_root_percent'] = None
    
    # Verifier si le fichier existe
    fichier_existe = os.path.isfile(fichier)

    # ouvrir syswatch.csv en mode ajout
    with open(fichier, 'a', newline='', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=ligne.key())

        # Ecrit l'entete si le fichier est nouveau
        if not fichier_existe:
            writer.writeheader()
        
        # Ecrit la ligne de données
        writer.writerow(ligne)

    print(f"Données exportées dans {fichier}")

def export_json(metrique, fichier='syswatch.csv'):
    """
    Exporte des métriques dans un fichier JSON.
    """
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(metrique, f, indent=2, ensure_ascii=False)
        print(f"Données exportées dans {fichier}")

def collecte_continu(intervalle=60, nombre=0, fichier='syswatch.csv'):
    """
    Effectue une collecte continue et les sauvegarde.
    """
    print(f"Collecte continue démarrée (intervalle: {intervalle}s)")
    print("Ctrl+C pour arrêter\n")

    compteur = 0

    try:
        while True:
            compteur += 1

            # Collecteur
            print(f"[{datetime.now().strftime('%H:%M:%S')}]")

            print(f"[{datetime.now().strftime('%H:%M:%S')}] Collecte #{compteur}...")
            metriques = collector.collecter_tout()

            # Affiche résumé
            print(f" CPU: {metriques['cpu']['utilisation']}%")
            print(f" RAM: {metriques['memoire']['pourcentage']}%")

            # Sauvegarde

            export_csv(metriques, fichier)

            # Vérifier si on doit s'arreter
            if nombre > 0 and compteur >= nombre:       # Controle la boucle infinie
                print(f"\n{nombre} collectes effectuées. Terminé.")
                break

            # Attendre avant la prochaine collecte
            print(f"  Prochaine collecte dans {intervalle}s...\n")
            time.sleep(intervalle)

    except KeyboardInterrupt:
        # si l'utilisateur a appuyer sur ctrl+C
        print(f"\n\nArrêt demandé. {compteur} collectes effectuées.")
        print(f"Données sauvegardées dans {fichier}")


def calcul_moyennes(fichier='syswatch.csv'):
    """
    Calcule des statistiques à partir du fichier CSV.
    """
    import os
    
    if not os.path.isfile(fichier):
        print(f"Erreur: fichier {fichier} introuvable")
        return
    
    # Listes pour stocker les valeurs
    valeurs_cpu = []
    valeurs_mem = []
    
    # Lire le fichier CSV
    with open(fichier, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for ligne in reader:
            # Convertir les chaînes en nombres
            try:
                cpu = float(ligne['cpu_percent'])
                mem = float(ligne['mem_percent'])
                valeurs_cpu.append(cpu)
                valeurs_mem.append(mem)
            except (ValueError, KeyError):
                # Ligne invalide, on l'ignore
                continue
    
    if not valeurs_cpu:
        print("Aucune donnée valide trouvée")
        return
    
    # Calculer les statistiques
    print("\n=== Statistiques ===")
    print(f"Nombre de mesures: {len(valeurs_cpu)}")
    print(f"\nCPU:")
    print(f"  Moyenne: {sum(valeurs_cpu)/len(valeurs_cpu):.2f}%")
    print(f"  Min: {min(valeurs_cpu):.2f}%")
    print(f"  Max: {max(valeurs_cpu):.2f}%")
    print(f"\nMémoire:")
    print(f"  Moyenne: {sum(valeurs_mem)/len(valeurs_mem):.2f}%")
    print(f"  Min: {min(valeurs_mem):.2f}%")
    print(f"  Max: {max(valeurs_mem):.2f}%")


def main():
    """Fonction principale avec gestion d'arguments."""
    print("=" * 50)
    print("SysWatch v3.0")
    print("=" * 50 + "\n")
    
    # Analyse simple des arguments
    if len(sys.argv) > 1:
        commande = sys.argv[1]
        
        if commande == '--stats':
            # Afficher les statistiques
            calcul_moyennes()
            
        elif commande == '--continu':
            # Collecte continue
            intervalle = 60  # Défaut
            nombre = 0       # Infini par défaut
            
            # Chercher --intervalle
            if '--intervalle' in sys.argv:
                idx = sys.argv.index('--intervalle')
                if idx + 1 < len(sys.argv):
                    intervalle = int(sys.argv[idx + 1])
            
            # Chercher --nombre
            if '--nombre' in sys.argv:
                idx = sys.argv.index('--nombre')
                if idx + 1 < len(sys.argv):
                    nombre = int(sys.argv[idx + 1])
            
            collecte_continu(intervalle, nombre)
            
        else:
            print(f"Commande inconnue: {commande}")
            print("Utilisations possibles:")
            print("  python syswatch_v3.py                    # Collecte unique")
            print("  python syswatch_v3.py --stats            # Statistiques")
            print("  python syswatch_v3.py --continu          # Collecte continue")
            print("  python syswatch_v3.py --continu --intervalle 30 --nombre 10")
    
    else:
        # Pas d'argument : collecte unique
        metriques = collector.collecter_tout()
        
        # Affichage console
        from syswatch_v2 import afficher_systeme, afficher_cpu, afficher_memoire, afficher_disques
        afficher_systeme(metriques['systeme'])
        afficher_cpu(metriques['cpu'])
        afficher_memoire(metriques['memoire'])
        afficher_disques(metriques['disques'])
        
        # Export
        export_csv(metriques)
        export_json(metriques)


if __name__ == "__main__":
    main()