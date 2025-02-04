if __name__ == "__main__" :
    demande : int
    res : int
    res1 : int
    res2 : int
    res3 : int
    res4 : int
    res5 : int
    res6 : int
    convert : str
    transaction : str
    secondes : int
    minutes : int
    heurs : int
    jours : int
    semaines : int
    mois : int
    années : int
    resultat_annees :int
    resultat_mois :int
    resultat_semaines :int
    resultat_jours :int
    resultat_heures :int
    resultat_minutes :int
    resultat_secondes :int
    
    secondes = 1
    minutes = 60 * secondes
    heures = 60 * minutes 
    jours = 24 * heures
    semaines = 7 * jours
    mois = 4 * semaines #par convention, on dira qu'il y a 4 semaines par mois
    années = 12 * mois
    
    transaction = str(input("Voulez vous convertir un résultat de secondes en tout = (1), ou tout en secondes = (2) : "))
    if transaction == "1" :
        demande = int(input("Veuillez saisir un nombres de secondes à convertir : "))
        #convert = str(input("Veuillez saisir le modèle de conversion (en années, mois, semaines, jours heures, minutes, secondes) : "))
        
        res1 = demande // années 
        res = demande % années
        res2 = res // mois
        res = res % mois
        res3 = res // semaines
        res = res % semaines
        res4 = res // jours
        res = res % jours
        res5 = res // heures
        res = res % heures
        res6 = res // minutes
        res = res % minutes
        res = res % secondes
        
        print("La conversion est égal à : \n", res1, "années\n", res2, "mois\n", res3, "semaines\n", res4, "jours\n", res5, "heures\n", res6, "minutes\n", res, "secondes.\n")
        
    else :
        if transaction == "2" :
            print("Bien, suivez les instructuions suivantes.")
            resultat_annees = int(input("Entrez le nombre d'années : "))
            resultat_mois = int(input("Entrez le nombre de mois : "))
            resultat_semaines = int(input("Entrez le nombre de semaines : "))
            resultat_jours = int(input("Entrez le nombre de jours : "))
            resultat_heures = int(input("Entrez le nombre d'heures : "))
            resultat_minutes = int(input("Entrez le nombre de minutes : "))
            resultat_secondes = int(input("Entrez le nombre de secondes : "))
            resultat = resultat_annees * années + resultat_mois * mois + resultat_semaines * semaines + resultat_jours * jours + resultat_heures * heures + resultat_minutes * minutes + resultat_secondes * secondes
            print("Cela fait", resultat, "secondes")
        else :
            print("Erreur de choix, veuillez recommencer")