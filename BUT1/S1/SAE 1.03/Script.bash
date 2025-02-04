# Script qui prend en compte 2 arguments et qui vérifie leur validité 
# Puis contrôle si l'emprunt est bien enregistré dans le fichier
# Si l'emprunt est enregistré, le script supprime la ligne dans le fichier 
# Et modifie le fichier de stock en ajoutant la ligne de l'exemplaire

#!/bin/bash
#Vérification du nombre d'arguments
if [ $# -ne 2 ]; then
    echo "Erreur: Nombre d'arguments incorrect"
    exit 1
fi

#Vérification de l'existence des fichiers
if [ ! -f "emprunts.txt" ]; then
    echo "Erreur: Fichier emprunts.txt introuvable"
    exit 1
fi

if [ ! -f "stock.txt" ]; then
    echo "Erreur: Fichier stock.txt introuvable"
    exit 1
fi

#Vérification de la validité des arguments
if ! grep -q "^$1;$2" emprunts.txt; then
    echo "Erreur: Emprunt non enregistré"
    exit 1
fi

#Suppression de la ligne dans le fichier emprunts.txt
sed -i "/^$1;$2/d" emprunts.txt
#Ajout de la ligne dans le fichier stock.txt
echo "$2" >> stock.txt
echo "Emprunt rendu avec succès"
exit 0
