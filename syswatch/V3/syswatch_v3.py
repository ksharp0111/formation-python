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