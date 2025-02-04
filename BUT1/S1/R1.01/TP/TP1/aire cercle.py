if __name__ == "__main__" :
    rayon : float
    aire : float
    
    rayon = float(input("Veuillez sasir le rayon de votre cercle en cm : "))
    if rayon <= 0 :
        print("La saisie du rayon a une erreur")
    else: 
        aire = rayon*rayon* 3.1415
        print("L'aire du cercle est de: ", aire, "cm²")