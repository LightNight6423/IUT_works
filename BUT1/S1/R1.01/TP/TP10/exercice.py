class Auteur :
    """
    Classe qui représente un auteur
    Attributs:
        nom (str): le nom de l'auteur
        nationalité (str): la nationalité de l'auteur
        dateNaissance (int): la date de naissance de l'auteur
    """
    
    def __init__(self, nom: str, prenom : str , nationalité: str, dateNaissance: int, annee_deces: int):
        self.nom = nom
        self.prenom = prenom
        self.nationalité = nationalité
        self.dateNaissance = dateNaissance
        self.annee_deces = annee_deces

    def __str__(self):
        return f"Nom: {self.nom}, Nationalité: {self.nationalité}, Date de naissance: {self.dateNaissance}"

class Livre:
    """
    Classe qui représente un livre
    Attributs:
        titre (str): le titre du livre
        auteur (str): le nom de l'auteur
        annee (int): l'année de publication
        nbPages (int): le nombre de pages
    """
    
    def __init__(self, titre: str, auteur: Auteur, annee: int, nbpages: int):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.nbPages = nbpages
        
        

    def __str__(self):
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Année de publication: {self.annee}, Nombre de pages: {self.nbPages}"

############################################
############################################
############################################

def afficher_liste_auteurs(bibliothèque: list[Auteur]) -> None:
    """
    Fonction qui affiche la liste des auteurs de la bibliothèque
    Args:
        bibliothèque (list[Auteur]): la liste des auteurs de la bibliothèque
    Returns:
        None
    """
    for auteur in bibliothèque:
        print(auteur)
    if len(bibliothèque) == 0:
        print("La bibliothèque ne comporte pas d'auteur")

############################################
############################################
############################################
def ajouter_auteur(bibliothèque: list[Auteur]) -> None:
    """
    Fonction qui ajoute un auteur à la bibliothèque
    Args:
        bibliothèque (list[Auteur]): la liste des auteurs de la bibliothèque
    Returns:
        None
    """
    choix : str
    
    nom : str 
    nom = input("Entrez le nom de l'auteur: ")

    prenom : str 
    prenom = input("Entrez le prénom de l'auteur: ")

    nationalité : str 
    nationalité = input("Entrez la nationalité de l'auteur: ")

    dateNaissance : int 
    dateNaissance = int(input("Entrez la date de naissance de l'auteur: "))

    print("Votre auteur est-il décédé ?")
    choix = input("oui/non: ")
    if choix == "oui":
        annee_deces : int
        annee_deces = int(input("Entrez l'année de décès de l'auteur: "))
    else:
        annee_deces = -1
    
    auteur = Auteur(nom, prenom, nationalité, dateNaissance, annee_deces)
    if auteur not in bibliothèque:
        bibliothèque_auteur.append(auteur)
    else:
        print("L'auteur est déjà dans la liste")
    
############################################
############################################
############################################

def afficher_menu() -> int: 
    """
    Fonction qui affiche le menu de la bibliothèque et qui retourne le choix de l'utilisateur
    Args:
        None : None
    Returns:
        int: le choix de l'utilisateur
    """
    choix : int

    print("1. Afficher l'ensembles des livres de la bibliothèque")
    print("2. Ajouter un nouveau livre")
    print("3. Rechercher un livre par son titre")
    print("4. Ajourter un auteur")
    print("5. Quitter")

    choix = int(input("Entrez votre choix: "))

    return choix

############################################
############################################
############################################

def afficher_bibliothèque(bibliothèque: list[Livre]) -> None:
    """
    Fonction qui affiche l'ensemble des livres de la bibliothèque
    Args:
        bibliothèque (list[Livre]): la liste des livres de la bibliothèque
    Returns:
        None
    """
    for livre in bibliothèque:
        print(livre)
    if len(bibliothèque) == 0:
        print("La bibliothèque est vide")

############################################
############################################
############################################

def ajouter_livre(bibliothèque: list[Livre], bibliothèque_auteur : list[Auteur]) -> None:
    """
    Fonction qui ajoute un livre à la bibliothèque
    Args:
        bibliothèque (list[Livre]): la liste des livres de la bibliothèque
    Returns:
        None
    """
    print("Liste des auteurs disponibles :")
    choix : str
    auteur : Auteur
    for i in bibliothèque_auteur:
        print("Nom :",i.nom,"|Prénom :", i.prenom,"|Nationalité :", i.nationalité,"|DateNaissance :", i.dateNaissance,"|Annee de décès :", i.annee_deces)
        print("Est-ce l'auteur de votre livre ?")
        choix = input("oui/non: ")
        if choix == "oui":
            auteur = Auteur(i.nom, i.prenom, i.nationalité, i.dateNaissance, i.annee_deces)
        else :
            print("Auteur suivant")
    print("Fin de la liste auteur, si l'auteur de votre livre n'est pas dans la liste, veuillez l'ajouter")
    ajouter_auteur(bibliothèque_auteur)
    auteur = bibliothèque_auteur[-1]
    
    
    titre : str 
    titre = input("Entrez le titre du livre: ")

    annee : int 
    annee = int(input("Entrez l'année de publication: "))

    nbpages : int 
    nbpages = int(input("Entrez le nombre de pages: "))

    livre = Livre(titre, auteur, annee, nbpages)
    bibliothèque.append(livre)

############################################
############################################
############################################

def rechercher_livre(bibliothèque: list[Livre]) -> None:
    """
    Fonction qui recherche un livre par son titre
    Args:
        bibliothèque (list[Livre]): la liste des livres de la bibliothèque
    Returns:
        None
    """
    titre : str 
    tmp : int
    titre = input("Entrez le titre du livre: ")
    tmp = -1

    for livre in bibliothèque :
        if livre.titre == titre :
            print(livre)
            tmp += 1

    if tmp == -1 :
        print("La bibliothèque ne comporte pas votre livre")


############################################
############################################
############################################

if __name__ == "__main__":
    bibliothèque : list[Livre] = []
    bibliothèque_auteur : list[Auteur] = []
    choix : int

    while True:
        choix = afficher_menu()

        if choix == 1:
            afficher_bibliothèque(bibliothèque)
        if choix == 2:
            ajouter_livre(bibliothèque, bibliothèque_auteur)
        if choix == 3:
            rechercher_livre(bibliothèque)
        if choix == 4:
            ajouter_auteur(bibliothèque_auteur)
        if choix == 5:
            exit()
        if choix < 1 or choix > 5:
            print("Choix invalide")