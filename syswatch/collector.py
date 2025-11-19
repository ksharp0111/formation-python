#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de collecte des metriques du système
"""


import platform
import psutil
from datetime import datetime

def collect_sys():
    """
    Collecte les informations générales du système.
    """
    return {
        'os': platform.system(),
        'version': platform.release(),
        'architecture': platform.architecture(),
        'hostname': platform.node(),
        'python': platform.python_version()
    }


def collect_cpu():
    """
    Collecte les infos du processeur.
    """
    return {
        'coeurs_ph': psutil.cpu_count(logical=False),
        'coeurs_lo': psutil.cpu_count(logical=True),
        'utilisation': psutil.cpu_percent(interval=1)
    }


def collect_memoire():
    """
    Collecte les infos de la RAM.
    """
    memoire = psutil.virtual_memory()
    return {
        'total': memoire.total,
        'disponible': memoire.available,
        'pourcentage': memoire.percent
    }


def collect_disque():
    """
    Collecte les infos des disques.
    """
    disques = []        # variable de stockage des info des disques et des partitions
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            # Recuperation des points de montage des differents disques
            usage = psutil.disk_partitions(partition.mountpoint)
            disques.append({
                'point_montage': partition.mountpoint,
                'total': usage.total,
                'utilise': usage.used,
                'pourcentage': usage.percent
            })
        
        except PermissionError:
            # partition inaccessible ignorées
            continue
    return disques


def collect_all():
    """
    Collecte les infos du système.
    """
    return {
        # rappel des fonctions précédements créé et ajout de la date au format YYYY-MM-DD
        'timestamp': datetime.now().isoformat(),
        'systeme': collect_sys,
        'cpu': collect_cpu,
        'memoire': collect_memoire,
        'disque': collect_disque
    }
