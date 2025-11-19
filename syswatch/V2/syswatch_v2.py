"""
SysWatch v2 - Version modulaire
"""

import collector    # module perso

def covert_o_to_go(octets):
    """
    Convertit les octets en Go
    """
    go = octets / (1024 ** 3)
    return f"{go:.2f} Go"   # Retourne un resultat .00 a la fin du résultat


def info_sys(data):
    """ 
    Affiche les infos système
    """
    print("\n=== Système ===")
    print(f"OS: {data['os']}")
    print(f"Version: {data['version']}")
    print(f"Architecture: {data['architecture']}")
    print(f"Hostname: {data['hostname']}")
    print(f"Python: {data['python']}")


def info_cpu(data):
    """ 
    Affiche les infos du CPU
    """
    print("\n=== CPU ===")
    print(f"Coeurs Phisique: {data['coeurs_ph']}")
    print(f"Coeurs Logique: {data['coeurs_lo']}")
    print(f"Utilisation: {data['utilisation']}")


def info_memoire(data):
    """ 
    Affiche les infos de la mémoire
    """
    print("\n=== Mémoire ===")
    # Fonction de conversion
    print(f"Total: {covert_o_to_go(data['total'])}")
    print(f"Disponible: {covert_o_to_go(data['disponible'])}")
    print(f"Utilisation: {data['pourcentage']}%")


def info_disque(data):
    """ 
    Affiche les infos des disques
    """
    print("\n=== Disques ===")

    if not data:        # Si vide
        print("Aucun disque disponible")
        return
    
    for disque in data:
        point = disque['point_montage']
        pourcent = disque['pourcentage']
        print(f"{point} : {pourcent}% utilisé")


def main():
    """Fonction principale du programme."""
    print("=" * 50)
    print("SysWatch v2.0 - Version modulaire")
    print("=" * 50)

    # Collecte de toutes les données
    collect_all = collector.collecter_tout()

    # Afficher les sections
    info_sys(collect_all['systeme'])
    info_cpu(collect_all['cpu'])
    info_memoire(collect_all['memoire'])
    info_disque(collect_all['disque'])

    # Afficher timestamp
    print(f"\nCollecté à: {collect_all['timestamp']}")
    print("=" * 50)


if __name__ == "__main__":
    main()