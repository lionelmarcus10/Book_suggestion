def ask_pseudonyme():
    ask_pseudonyme=str(input("Psedudonyme : "))
    return ask_pseudonyme
def ask_genre():
    print("1 - HOMME ")
    print("2 - FEMME ")
    print("3 - PEU IMPORTE ")
    ask_genre=int(input("Qullez votre genre ?  "))
    while (ask_genre != 1 and ask_genre != 2 and ask_genre != 3 ) :
        print("1 - HOMME ")
        print("2 - FEMME ")
        print("3 - PEU IMPORTE ")
        ask_genre = int(input("Quel votre genre ?  "))
    return ask_genre

def ask_age():
    print("1 - <= 18 ans")
    print("2 - Entre 18 ans et 25 ans")
    print('3 - > 25 ans ')
    ask_age = int(input("Quel est votre âge ? "))
    while (ask_age != 1 and ask_age != 2 and ask_age != 3 ) :
        print("1 - <= 18 ans")
        print("2 - Entre 18 ans et 25 ans")
        print('3 - > 25 ans ')
    return ask_age

def ask_style_de_lecture():
    print("Quel est votre style de lecture ? ")
    from listes import liste_style_de_lecture
    for style in range(0,len(liste_style_de_lecture)):
        print(style + 1,' - ',liste_style_de_lecture[style])
    ask_style_de_lecture = int(input("Saisir votre style de lecture : "))
    while (ask_style_de_lecture < 1 or ask_style_de_lecture > 7):
        ask_style_de_lecture = int(input("Saisir votre style de lecture : "))
    print(ask_style_de_lecture)
    return ask_style_de_lecture

def ask_menu():
    print("1 - Profils des lecteurs")
    print("2 - Visiter le dépôt des livres")
    print("3 - Recommandation")
    choix_menu = int(input(" Que voulez vous visiter ? "))
    while ( choix_menu < 1 or choix_menu > 3):
        choix_menu = int(input(" Que voulez vous visiter ? "))
    return choix_menu

def ask_menu_profil():
    print("1 - Ajouter un lecteur")
    print("2 - Afficher un lecteur")
    print("3 - Modifier un lecteur")
    print("4 - Supprimer un lecteur")
    profil_menu = int(input(" Que voulez vous faire ? "))
    while (profil_menu < 1 or profil_menu > 4):
        profil_menu = int(input(" Que voulez vous faire ? "))
    return profil_menu

def ask_menu_dépot_livres():
    print("1 - Afficher la liste des livres dans le dépôt (liste initiale fournie dans le fichier books.txt) \n "
          "2 - Ajouter un livre au dépôt \n 3 - Modifier le titre d’un livre dans le dépôt \n 4 - Supprimer un livre du dépôt ")
    dépot_menu = int(input(" Que voulez vous faire ? "))
    while (dépot_menu < 1 or dépot_menu > 4):
        dépot_menu = int(input(" Que voulez vous faire ? "))
def ask_recommandation_livre():
    print("1 - Noter un livre")
    print("2 - Suggére des livres")
    livrereco_menu = int(input(" Que voulez vous faire ? "))
    while (livrereco_menu < 1 or livrereco_menu > 4):
        livrereco_menu = int(input(" Que voulez vous faire ? "))
    return livrereco_menu


def ajouter_un_lecteur():
    numero_pseudo = ask_pseudonyme()
    numero_genre = ask_genre()
    numero_age = ask_age()
    numero_style_lecture = ask_style_de_lecture()


