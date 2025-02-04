#!/bin/bash

echo "Vous allez entrer une date sous la forme JJ/MM/AAAA"

# Demander le jour, mois et année
read -p "Entrez le jour : " jour
read -p "Entrez le mois : " mois
read -p "Entrez l'année : " annee
read -p "Entrer la date complète : " date

# Vérifications initiales
while [[ $jour -le 0 || $jour -gt 31 ]]; do
    echo "Les jours doivent être des entiers positifs non nuls"
    read -p "Entrez le jour : " jour
done

while [[ $mois -le 0 || $mois -gt 12 ]]; do
    echo "Les mois doivent être des entiers positifs non nuls"
    read -p "Entrez le mois : " mois
done

# Vérifier si l'année est bissextile
bissextile=false
if (( annee % 4 == 0 )); then
    if (( annee % 100 != 0 || annee % 400 == 0 )); then
        bissextile=true
    fi
fi

#Compare le nombre de jour entre eux et vérifie si il y un mois qui est passé ou non
if [[ $mois -eq 2 && $bissextile == true && $jour -gt 29 ]]; then
    echo "Erreur: Février ne peut pas avoir plus de 29 jours"
    exit 7
elif [[ $mois -eq 2 && $bissextile == false && $jour -gt 28 ]]; then
    echo "Erreur: Février ne peut pas avoir plus de 28 jours"
    exit 7
elif [[ $mois -eq 4 || $mois -eq 6 || $mois -eq 9 || $mois -eq 11 && $jour -gt 30 ]]; then
    echo "Erreur: Ce mois ne peut pas avoir plus de 30 jours"
    exit 7
fi

#Renvoi un exit différent pour chaque cas en fonction de la date courante et de la date passé en argument sous lla forme jour/mois/année
#Exit 0 si la date  est postérieur ou égale à la date courante
#Exit 1 si la date est antérieur de plus d'un an à la date courante
#Exit 2 si la date est antérieur de moins d'un an et de plus d'un mois à la date courante
#Exit 3 si la date est antérieur de moins d'un mois à la date courante
if [[ $annee -eq $(date +%Y) && $mois -lt $(date +%m) ]]; then
    echo "La date est antérieure à la date courante"
    exit 1
elif [[ $]]

elif [[ $annee -eq $(date +%Y) && $mois -eq $(date +%m) && $jour -lt $(date +%d) ]]; then
    echo "La date est antérieure à la date courante"
    exit 3
elif [[ $annee -eq $(date +%Y) && $mois -eq $(date +%m) && $jour -eq $(date +%d) ]]; then
    echo "La date est égale à la date courante"
    exit 0
elif [[ $annee -eq $(date +%Y) && $mois -eq $(date +%m) && $jour -gt $(date +%d) ]]; then
    echo "La date est postérieure à la date courante"
    exit 0
elif [[ $annee -eq $(date +%Y) && $mois -gt $(date +%m) ]]; then
    echo "La date est postérieure à la date courante"
    exit 0
elif [[ $annee -gt $(date +%Y) ]]; then
    echo "La date est postérieure à la date courante"
    exit 0
fi
