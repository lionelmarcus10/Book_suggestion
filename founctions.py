from listes import *

""""Une fonction qui permet de demander le pseudonyme"""

def ask_pseudonyme():
    ask_pseudonyme = str(input("Pseudonyme : "))
    return ask_pseudonyme

"""Une fonction qui demande le sexe de l'utilisateur """

def ask_genre():
    print(" Quel votre genre ? ","\n","Tapez les numéro qui vous correspondent")
    print("1 - HOMME ")
    print("2 - FEMME ")
    print("3 - PEU IMPORTE ")
    ask_genre=(input("..."))
    while (ask_genre != '1' and ask_genre != '2' and ask_genre != '3' ) :
        print(" Quel votre genre ? ", "\n", "Tapez les numéro qui vous correspondent")
        print("1 - HOMME ")
        print("2 - FEMME ")
        print("3 - PEU IMPORTE ")
        ask_genre = (input("..."))
    return ask_genre


"""Une fonction qui demande  l'âge de l'utilisateur"""

def ask_age():
    print("Quel est votre âge ? ","\n"," Tapez le numéro 1 ou 2 ou 3 pour saisir votre âge ")
    print("1 - <= 18 ans")
    print("2 - Entre 18 ans et 25 ans")
    print('3 - > 25 ans ')
    ask_age = (input("..."))
    while (ask_age != '1' and ask_age != '2' and ask_age != '3' ) :
        print(" Quellez votre genre ? ", "\n", "Tapez les numéro qui vous correspond")
        print("1 - <= 18 ans")
        print("2 - Entre 18 ans et 25 ans")
        print('3 - > 25 ans ')
        ask_age = (input("..."))
    return ask_age

"""Une fonction qui permet de savoir le style de lecture"""

def ask_style_de_lecture():
    print("Quel est votre style de lecture ? ","\n","Tapez le numéro qui vous correspond")
    from listes import liste_style_de_lecture
    for style in range(0,len(liste_style_de_lecture)):
        print(style + 1,' - ',liste_style_de_lecture[style])
    ask_style_de_lecture = int(input("Saisir votre style de lecture : "))
    while (ask_style_de_lecture < 1 or ask_style_de_lecture > 7):
        ask_style_de_lecture = int(input("..."))

    return str(ask_style_de_lecture)

""""Une fonction qui donne le menu qui proposer par ce programme """

def ask_menu():
    print("Tapez le numéro qui vous correspond")
    print("1 - Profils des lecteurs")
    print("2 - Visiter le dépôt des livres")
    print("3 - Recommandation")
    choix_menu = (input(" ... "))
    while (( choix_menu !='1' and choix_menu !='3' and choix_menu != '2')):
        choix_menu = (input("Saissez à nouveau le numéro : "))
    return int(choix_menu)

"""" une fonction qui permet .................."""

def ask_menu_profil():
    print("Tapez le numéro qui vous correspond")
    print("1 - Ajouter un lecteur")
    print("2 - Afficher un lecteur")
    print("3 - Modifier un lecteur")
    print("4 - Supprimer un lecteur")
    profil_menu = input(" ... ")
    while (profil_menu != '1' and profil_menu  !='2' and profil_menu != '3'and profil_menu != '4'):
        profil_menu = input(" Saisisez à nouveau le numéro : ")
    return int(profil_menu)

def ask_menu_dépot_livres():
    print("Tapez le numéro qui vous correspond ")
    print("1 - Afficher la liste des livres dans le dépôt  \n "
          "2 - Ajouter un livre au dépôt \n 3 - Modifier le titre d’un livre dans le dépôt \n 4 - Supprimer un livre du dépôt ")
    dépot_menu = input(" ... ")
    while (dépot_menu != '1' and dépot_menu !='2'and dépot_menu != '3'and dépot_menu != '4' ):
        dépot_menu = input(" Saisisez à nouveau le numéro ")
    return int(dépot_menu)

"""une fonction qui recommande des livres ......"""

def ask_recommandation_livre():
    print("Tapez le numéro qui vous correspond")
    print("1 - Noter un livre")
    print("2 - Suggére des livres")
    livrereco_menu = input(" ...  ")
    while (livrereco_menu !='1' and livrereco_menu != '2'):
        livrereco_menu = input(" Saisissez à nouveau le numéro ")
    return int(livrereco_menu)

""" -----------------------------------------------------------------------------------------------------"""
""""Ube fonction qui vérifie si un lecteur existe déja"""

def check_profile(pseudo_to_del):
    with open('readers.txt' , 'r',encoding='utf-8') as profile_checkers:
        profile_checker = profile_checkers.readlines()
        for profile_data_number in range(len(profile_checker)):
            profile_ind_data = profile_checker[profile_data_number]
            profile_ind_data_value = profile_ind_data.split(",")
            if profile_ind_data_value[0]== pseudo_to_del:
                return True
    return False



"""une fonction qui ajoute un lecteur"""

def ajouter_un_lecteur():

    nom_pseudo = ask_pseudonyme()
    name_to_add_verified = check_profile(nom_pseudo)
    while name_to_add_verified == True:
        print("Ce lecteur existe déjà, veuillez saisir un nom different ")
        nom_pseudo = ask_pseudonyme()
        name_to_add_verified = check_profile(nom_pseudo)
    numero_genre = ask_genre()
    numero_age = ask_age()
    numero_style_lecture = ask_style_de_lecture()
    with open("readers.txt", "a",encoding='utf-8') as readers_db:
        readers_db.write(nom_pseudo +"," + numero_genre + ','+ numero_age +','+ numero_style_lecture+ '\n')

""""Une fonction qui supprime un lecteur"""

def supprimer_un_lecteur():
    name_a_sup = ask_pseudonyme()
    name_a_sup_verified = check_profile(name_a_sup)
    while name_a_sup_verified == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        name_a_sup = ask_pseudonyme()
        name_a_sup_verified = check_profile(name_a_sup)
    with open("readers.txt", "r",encoding='utf-8') as readers_db:
        sup_lecteur= readers_db.readlines()
        for lines in (sup_lecteur):
            if name_a_sup in lines :
                 sup_lecteur.remove(lines)
                 print('lecteur {} deleted'.format(name_a_sup))
                 with open("readers.txt", "w",encoding='utf-8') as readers_db2:
                     for lecteur_restant in sup_lecteur:
                         readers_db2.write(lecteur_restant)
                 readers_db2.close()
    readers_db.close()


""""Une fonction qui affiche un lecteur """

def afficher_un_lecteur():
     afficher_un_lecteur = ask_pseudonyme()
     affichier_un_lecteur_verifid = check_profile(afficher_un_lecteur)
     while affichier_un_lecteur_verifid == False:
         afficher_un_lecteur = ask_pseudonyme()
         affichier_un_lecteur_verifid = check_profile(afficher_un_lecteur)
     with open("readers.txt","r",encoding='utf-8') as affichier_db :
            affichier_lecteur = affichier_db.readlines()
     for lines in affichier_lecteur:
         if afficher_un_lecteur in lines:
              lines = lines.replace(","," ").split()
              lines[1] = liste_genre[int(lines[1])-1]
              lines[2] = liste_age[int(lines[2]) - 1]
              lines[3] = liste_style_de_lecture[int(lines[3])-1]
              for i in lines:
                 print(i,end=' ')


def modifier_un_lecteur():
    name_to_modify = ask_pseudonyme()
    name_to_modify_verified  = check_profile(name_to_modify)
    while name_to_modify_verified == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        name_to_modify = ask_pseudonyme()
        name_to_modify_verified = check_profile(name_to_modify)
    modifi_options = input("Veuillez espacer les chiffres : ")
    modifi_options = modifi_options.split()
    for chiffres in range(len(modifi_options)):
        modifi_options[chiffres] = int(modifi_options[chiffres])


    return print(modifi_options)

# SECONDE PARTIE ----------------------------------------------------------------

def ask_book_name():
    book_name = input('Saisir le nom du livre')
    return book_name

def check_book_name(book_to_check):
    with open('books.txt' , 'r',encoding='utf-8') as books_checkers:
        list_books_checker = books_checkers.readlines()
        for index_books in range(len(list_books_checker)):
            books_ind_data = list_books_checker[index_books]
            if books_ind_data == book_to_check + '\n':
                return True
    return False

def display_books():
    with open('books.txt','r',encoding='utf-8') as display_books:
        books_names_index = 1
        for books_names in display_books:
            print('{} - {}'.format(books_names_index,books_names), end='')
            books_names_index+=1

def add_books():
    book_name = ask_book_name()
    book_name_verified = check_book_name(book_name)
    while (book_name_verified == True):
        print('Ce livre existe déjà \n veuillez saisir un autre nom')
        book_name = ask_book_name()
        book_name_verified = check_book_name(book_name)
    with open("books.txt", "a",encoding='utf-8') as books_db:
        books_db.write(book_name + '\n')

def modify_book_title():
    book_title = ask_book_name()
    book_title_verified = check_book_name(book_title)
    while (book_title_verified == False):
        print("Ce livre existe n'existe pas \n veuillez saisir un autre nom")
        book_title = ask_book_name()
        book_title_verified = check_book_name(book_title)
    new_title_of_book = input('Saisir le nom du nouveau livre : ')
    with open("books.txt", "r", encoding='utf-8') as books_db:
        list_books_db = books_db.readlines()
        with open('books.txt','w', encoding='utf-8') as books_modification_part:
            for books in list_books_db:
                if book_title + '\n' == books:
                    books_modification_part.write(new_title_of_book + '\n')
                    print(book_title,'modified to ', new_title_of_book)
                else:
                    books_modification_part.write(books)