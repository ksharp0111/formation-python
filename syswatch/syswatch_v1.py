#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SysWatch v1.0 - Monitoring système basique
"""

import platform
import psutil

def info_sys():
    """ Affiche les info système """
    print("\n=== Système ===")
    print(f"OS: {platform.system()}")
    print(f"version: {platform.release()}")
    print(f"Arhitecture: {platform.machine()}")
    print(f"Hostname: {platform.node()}")
    print(f"Python: {platform.python_version()}")


def info_cpu():
    """" Affiche les infos du processeur"""
    print("\n=== CPU ===")
    # Nombre de coeurs
    coeurs_ph = psutil.cpu_count(logical=False)
    coeurs_lo = psutil.cpu_count(logical=True)
    print(f"Coeurs physique: {coeurs_ph}")
    print(f"Coeurs logique: {coeurs_lo}")
    # Utilisation CPU
    utilisation = psutil.cpu_percent(interval=1)
    print(f"Utilisation: {utilisation}%")


def info_memoire():
    """ Affiche les infos memoire """
    print("\n=== Mémoire ===")

    # Récupérer les infos mémoire
    memoire = psutil.virtual_memory()

    # Conversion octets vers gigaoctets
    # 1 Go = 1024 * 1024 * 1024 octets = 1024^3
    total_gb = memoire.total / (1024 ** 3)
    disponible_gb = memoire.available / (1024 ** 3)

    # Formatage avec deux décimales
    print(f"Total: {total_gb:.2f} GB")
    print(f"Disponible: {disponible_gb:.2f}")
    print(f"Utilisation {memoire.percent}%")


def info_disque():
    """ Affiche les infos des disques"""
    print("\n=== Disques ===")

    # Récupération des partitions
    partitions = psutil.disk_partitions()

    for partition in partitions:
        point_montage = partition.mountpoint

        try:
            # Utilisation du disque
            usage = psutil.disk_usage(point_montage)
            print(f"{point_montage} : {usage.percent}% utilisé")

        except PermissionError:
            # partition inaccessible
            print(f"{point_montage} : Accès refuser")
            continue


def main():
    """ Fonction prinncipale """

    # Afficher le titre
    print("=" * 50)
    print("SysWatch v1.0 - Monitoring Système")
    print("=" * 50)

    # Appel des fonctions d'affichages d'etat
    info_sys()
    info_cpu()
    info_memoire()
    info_disque()

    print("=" * 50)

# point d'entrée
if __name__ == "__main__":
    main()

