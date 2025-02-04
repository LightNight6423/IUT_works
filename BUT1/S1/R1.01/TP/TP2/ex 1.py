if __name__ == "__main__" :
    
    a,b = int
    
    a = int(input("Veuillez saisir la première valeur : "))
    b = int(input("Veuillez sasir la deuxième valeur : "))
    if a > b :
        print(a, ">", b)
    else :
        if a == b :
            print(a, "=", b)
        else : 
            print(a, "<", b)
            