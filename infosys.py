import platform # permet d'avoir des infos sur le systeme 


# information sur le systeme

print("====== SYSTEME D'EXPLOITATION =====")
print("OS :", platform.system())
print("Sortie :", platform.release())
print("Version :",platform.version())
print()


# Information sur la machine

print("========= SYSTEME MACHINE ==========")
print("Processeur :", platform.processor())
print(platform.machine())

print(platform.platform())
print(platform.architecture())
print()


# Information sur la version de python

print("========= VERSION PYTHON ==========")
print(platform.python_version())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_implementation())
print()


# Autres informations  

print("========== AUTRES INFOS ===========")
import os
current_user = os.getlogin()
print("Utilisateurs :",current_user)
print("========== FIN DES INFOS ==========")