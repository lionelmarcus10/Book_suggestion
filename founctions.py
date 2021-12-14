from listes import *
import time


"""Partie I : Profils des lecteurs"""

""""Une fonction qui permet de demander le pseudonyme"""

def demander_un_pseudonyme():
    pseudonyme = str(input("Pseudonyme : "))
    return pseudonyme


"""Une fonction qui demande le sexe de l'utilisateur """

def demander_genre():
    print(" Quel votre genre ? ","\n","Tapez les numéro qui vous correspondent")
    print("1 - HOMME ")
    print("2 - FEMME ")
    print("3 - PEU IMPORTE ")
    demander_genre=(input("..."))
    while (demander_genre != '1' and demander_genre != '2' and demander_genre != '3' ) :
        print(" Quel votre genre ? ", "\n", "Tapez les numéro qui vous correspondent")
        print("1 - HOMME ")
        print("2 - FEMME ")
        print("3 - PEU IMPORTE ")
        demander_genre = (input("..."))
    return demander_genre


"""Une fonction qui demande  l'âge de l'utilisateur"""

def demander_age():
    print("Quel est votre âge ? ","\n"," Tapez le numéro 1 ou 2 ou 3 pour saisir votre âge ")
    print("1 - <= 18 ans")
    print("2 - Entre 18 ans et 25 ans")
    print('3 - > 25 ans ')
    age = (input("..."))
    while (age != '1' and age != '2' and age != '3' ) :
        print(" Quellez votre genre ? ", "\n", "Tapez les numéro qui vous correspond")
        print("1 - <= 18 ans")
        print("2 - Entre 18 ans et 25 ans")
        print('3 - > 25 ans ')
        age = (input("..."))
    return age


"""Une fonction qui permet de savoir le style de lecture"""


def demander_style_de_lecture():
    print("Quel est votre style de lecture ? ","\n","Tapez le numéro qui vous correspond")
    from listes import liste_style_de_lecture
    for style in range(0,len(liste_style_de_lecture)):
        print(style + 1,' - ',liste_style_de_lecture[style])
    style_lecture = input("Saisir votre style de lecture : ")
    while ( style_lecture < '1' or style_lecture > '7' or style_lecture != str(style_lecture)):
        style_lecture =input("...")

    return str(style_lecture)

""""Une fonction qui donne le menu qui proposer par ce programme """

def menu_principal():
    print("Tapez le numéro qui vous correspond")
    print("1 - Profils des lecteurs")
    print("2 - Visiter le dépôt des livres")
    print("3 - Recommandation")
    choix_menu = (input(" ... "))
    while ( choix_menu !='1' and choix_menu !='3' and choix_menu != '2'):
        choix_menu = (input("Saissez à nouveau le numéro : "))
    return int(choix_menu)

"""" une fonction qui permet .................."""

def demander_option_profile():
    print("Tapez le numéro qui vous correspond")
    print("1 - Ajouter un lecteur")
    print("2 - Afficher un lecteur")
    print("3 - Modifier un lecteur")
    print("4 - Supprimer un lecteur")
    profil_menu = input(" ... ")
    while (profil_menu != '1' and profil_menu  !='2' and profil_menu != '3'and profil_menu != '4'):
        profil_menu = input(" Saisisez à nouveau le numéro : ")
    return int(profil_menu)

def demander_option_depot_livre():
    print("Tapez le numéro qui vous correspond ")
    print(" 1 - Afficher la liste des livres dans le dépôt  \n 2 - Ajouter un livre au dépôt \n 3 - Modifier le titre d’un livre dans le dépôt \n 4 - Supprimer un livre du dépôt ")
    dépot_menu = input(" ... ")
    while (dépot_menu != '1' and dépot_menu !='2'and dépot_menu != '3'and dépot_menu != '4' ):
        dépot_menu = input(" Saisisez à nouveau le numéro ")
    return int(dépot_menu)

"""une fonction qui recommande des livres ......"""

def demander_option_recommandation_livre():
    print("Tapez le numéro qui vous correspond")
    print("1 - Noter un livre")
    print("2 - Suggére des livres")
    livrereco_menu = input(" ...  ")
    while (livrereco_menu !='1' and livrereco_menu != '2'):
        livrereco_menu = input(" Saisissez à nouveau le numéro ")
    return int(livrereco_menu)

""" -----------------------------------------------------------------------------------------------------"""
""""Ube fonction qui vérifie si un lecteur existe déja"""

def verifier_un_lecteur(nom_utilisateur):
    with open('readers.txt' , 'r',encoding='utf-8') as profile_checkers:
        profile_checker = profile_checkers.readlines()
        for profile_data_number in range(len(profile_checker)):
            profile_ind_data = profile_checker[profile_data_number]
            profile_ind_data_value = profile_ind_data.split(",")
            if profile_ind_data_value[0]== nom_utilisateur:
                return True
    return False



"""une fonction qui ajoute un lecteur"""

def ajouter_un_lecteur():

    nom_pseudo = demander_un_pseudonyme()
    nom_pseudo_verifier = verifier_un_lecteur(nom_pseudo)
    while nom_pseudo_verifier == True:
        print("Ce lecteur existe déjà, veuillez saisir un nom different ")
        nom_pseudo = demander_un_pseudonyme()
        nom_pseudo_verifier = verifier_un_lecteur(nom_pseudo)
    numero_genre = demander_genre()
    numero_age = demander_age()
    numero_style_lecture = demander_style_de_lecture()
    with open("readers.txt", "a",encoding='utf-8') as readers_db:
        readers_db.write(nom_pseudo +"," + numero_genre + ','+ numero_age +','+ numero_style_lecture+ '\n')
    books_read = ask_user_books_read()
    books_read_str = [str(i) for i in books_read]
    books_read_to_file = ','.join(books_read_str)
    with open("booksread.txt", "a", encoding='utf-8') as books_read_db:
        books_read_db.write(nom_pseudo + ','+ books_read_to_file + '\n')



""""Une fonction qui supprime un lecteur"""
def supprimer_un_lecteur():
    nom_a_sup = demander_un_pseudonyme()
    nom_a_sup_verifier = verifier_un_lecteur(nom_a_sup)
    while nom_a_sup_verifier == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        nom_a_sup = demander_un_pseudonyme()
        nom_a_sup_verifie = verifier_un_lecteur(nom_a_sup)
    with open("readers.txt", "r",encoding='utf-8') as readers_db:
        sup_lecteur= readers_db.readlines()
        i=0
        trouve = False
        while( i<len(sup_lecteur) and not trouve):
            l= sup_lecteur[i].split(",")
            if nom_a_sup in l :
                 sup_lecteur.remove(sup_lecteur[i])
                 print('lecteur {} deleted'.format(nom_a_sup))
                 trouve=True
            i+=1
        if not trouve:
            print("Ce lecteur n'existe pas")
        else:
            with open("readers.txt", "w",encoding='utf-8') as readers_db:
                for lecteur_restant in sup_lecteur:
                    readers_db.write(lecteur_restant)
    with open("booksread.txt","r",encoding='utf-8') as booksread_db:
        sup_lecteur_booksread_list = booksread_db.readlines()
    i = 0
    trouve = False
    while (i < len(sup_lecteur_booksread_list) and not trouve):
            sup_lecteur_booksread_list3 = sup_lecteur_booksread_list[i].split(",")
            if nom_a_sup == sup_lecteur_booksread_list3[0]:
                del sup_lecteur_booksread_list[i]
            i+=1


""""la fonction afficher_un_lecteur peut afficher le profil d’un lecteur donné """

def afficher_un_lecteur():
     af_lecteur = demander_un_pseudonyme()
     af_lecteur_verifier = verifier_un_lecteur( af_lecteur)
     while af_lecteur_verifier == False:
         af_lecteur = demander_un_pseudonyme()
         af_lecteur_verifier = verifier_un_lecteur( af_lecteur)
     with open("readers.txt","r",encoding='utf-8') as affichier_db :
            affichier_lecteur = affichier_db.readlines()
     for lines in affichier_lecteur:
         if  af_lecteur in lines:
              lines = lines.replace(","," ").split()
              lines[1] = liste_genre[int(lines[1])-1]
              lines[2] = liste_age[int(lines[2]) - 1]
              lines[3] = liste_style_de_lecture[int(lines[3])-1]
              print("Le lecteur s'est inscrit sous le pseudonyme {}, c'est un {}, âgé {} et qui aime lire des livres {}.".format(lines[0],lines[1],lines[2],lines[3]),end=" ")
     with open("booksread.txt","r",encoding='utf-8') as bookread_db :
         afficher_lecteur = bookread_db.readlines()
     i = 0
     trouve = False
     while (i < len(affichier_lecteur) + 1 and trouve==False):
         afficher_lecteur1= afficher_lecteur[i].split(",")
         if  af_lecteur == afficher_lecteur1[0]:
             livres_lue_index = afficher_lecteur1[1:]
             for d in range(0,len(livres_lue_index)):
                 livres_lue_index[d] = int(livres_lue_index[d])
             with open("books.txt","r",encoding='utf-8') as books_db:
                 livres = books_db.readlines()
                 for z in range(0,len(livres_lue_index)):
                     print(livres[livres_lue_index[z]],end='-')


             trouve = True
         i+=1




""" la fonction modifier_un_lecteur peut modifier les informations du profil d’un lecteur donné."""




def modifier_un_lecteur():
    nom_modif = demander_un_pseudonyme()
    nom_modif_verifier = verifier_un_lecteur(nom_modif)
    index_profile = catch_index('readers.txt', nom_modif)
    while nom_modif_verifier == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        nom_modif = demander_un_pseudonyme()
        nom_modif_verifier = verifier_un_lecteur(nom_modif)

    modifi_options = input("Veuillez espacer les chiffres : ")
    modifi_options = modifi_options.split()

    modifi_options_error = not_number_input(modifi_options)
    if modifi_options_error == False:
        modifi_options = [int(i) for i in modifi_options]
        for number_mod in modifi_options:
            if number_mod < 1 or number_mod > 5:
                modifi_options_error = True
    while modifi_options_error == True or modifi_options == []:
        modifi_options = input("Veuillez espacer les chiffres : ")
        modifi_options = modifi_options.split()
        modifi_options_error = not_number_input(modifi_options)
        if modifi_options_error == False:
            modifi_options = [int(i) for i in modifi_options]
            for number_mod in modifi_options:
                if number_mod < 1 or number_mod > 5:
                    modifi_options_error = True

    for options in modifi_options:
        if options == 1:
            new_pseudo_mod = demander_un_pseudonyme()
            new_pseudo_verf = verifier_un_lecteur(new_pseudo_mod)
            while (new_pseudo_verf == True):
                print('Ce lecteur existe déja. \n veuillez saisir un autre pseudsonyme')
                new_pseudo_mod = demander_un_pseudonyme()
                new_pseudo_verf = verifier_un_lecteur(new_pseudo_mod)
            with open('readers.txt', 'r', encoding='utf-8') as r_pmod:
                r_pmod_list = r_pmod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_p_apply:
                    for lines in range(len(r_pmod_list)):
                        lines_modp = r_pmod_list[lines].split(',')
                        if lines_modp[0] == nom_modif:
                            r_pmod_list[lines] = new_pseudo_mod + ',' + ','.join(lines_modp[1:])
                            mod_p_apply.write(r_pmod_list[lines])
                        else:
                            mod_p_apply.write(r_pmod_list[lines])

        elif options == 2:
            new_genre_mod = demander_genre()
            while (new_genre_mod != '1' and new_genre_mod != '2' and new_genre_mod != '3'):
                new_genre_mod = demander_genre()
            with open('readers.txt', 'r', encoding='utf-8') as r_gmod:
                r_gmod_list = r_gmod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_g_apply:
                    for lines in range(0, len(r_gmod_list)):
                        lines_modg = r_gmod_list[lines].split(',')
                        if lines == index_profile:
                            lines_modg[1] = new_genre_mod
                            r_gmod_list[lines] = ','.join(lines_modg)
                            mod_g_apply.write(r_gmod_list[lines])
                        else:
                            mod_g_apply.write(r_gmod_list[lines])

        elif options == 3:
            new_age_mod = demander_age()
            while (new_age_mod != '1' and new_age_mod != '2' and new_age_mod != '3'):
                new_age_mod = demander_age()
            with open('readers.txt', 'r', encoding='utf-8') as r_amod:
                r_amod_list = r_amod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_a_apply:
                    for lines in range(0, len(r_amod_list)):
                        lines_modg = r_amod_list[lines].split(',')
                        if lines == index_profile:
                            lines_modg[2] = new_age_mod
                            r_amod_list[lines] = ','.join(lines_modg)
                            mod_a_apply.write(r_amod_list[lines])
                        else:
                            mod_a_apply.write(r_amod_list[lines])
        elif options == 4:
            new_style_lecture_mod = demander_style_de_lecture()
            number_input_style_de_lecture = new_style_lecture_mod in ['{}'.format(i) for i in range(1, 8)]
            while (number_input_style_de_lecture == False):
                new_style_lecture_mod_mod = demander_style_de_lecture()
                number_input_style_de_lecture = new_style_lecture_mod in ['{}'.format(i) for i in range(1, 8)]
            with open('readers.txt', 'r', encoding='utf-8') as r_slmod:
                r_slmod_list = r_slmod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_sl_apply:
                    for lines in range(0, len(r_slmod_list)):
                        lines_modsl = r_slmod_list[lines].split(',')
                        if lines == index_profile:
                            lines_modsl[3] = new_style_lecture_mod
                            r_slmod_list[lines] = ','.join(lines_modsl)
                            mod_sl_apply.write(r_slmod_list[lines])
                        else:
                            mod_sl_apply.write(r_slmod_list[lines])
        elif options == 5:
            new_books_read_mod = ask_user_books_read()

""""Fin de la 1er parti"""





"""Partie II : Visiter le dépôt des livres"""

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






""" A mettre dans ajouter un lecteur après le premier WITH
    books_read = ask_books_read()
    books_read_str = [str(i) for i in books_read]
    books_read_to_file = ','.join(books_read_str)
    with open("booksread.txt", "a",encoding='utf-8') as books_read_db:
        books_read_db.write(nom_pseudo+','books_read_to_file + '\n')

    """






# securiser ask style de lecture et  copier modify_user
# check profile remplacer le nom de la variable en paramètre

"""fonction utilisé dans plusieur parti"""


def modify_user_books_read(my_user_pseudo_to_modify):
    books_read_2 = ask_user_books_read()
    with open("booksread.txt", "r", encoding='utf-8') as books_read_modif_db:
        books_read_modif_db_list = books_read_modif_db.readlines()
        with open("booksread.txt", "w", encoding='utf-8') as books_read_modif_db2:
            for index_info in range(len(books_read_modif_db_list)):
                infos_split = books_read_modif_db_list[index_info].split(',')
                if infos_split[0] == my_user_pseudo_to_modify:
                    books_read_modif_db_list[index_info] = [my_user_pseudo_to_modify] + [str(i) for i in books_read_2]
                    books_read_modif_db_list[index_info] = ','.join(books_read_modif_db_list[index_info])
                    books_read_modif_db2.write(books_read_modif_db_list[index_info] + '\n')
                else:
                    books_read_modif_db2.write(books_read_modif_db_list[index_info])







def ask_user_books_read():
    print("quels sont les livres que vous avez déjà lu ? : ")
    time.sleep(3)
    display_books()
    time.sleep(3)
    print('Veuillez espacer les chiffres des lettres des livres que vous avez lu')
    books_read = input('Veuillez saisir les chiffres :').split()
    while (books_read == []):
        print('Veuillez espacer les chiffres des lettres des livres que vous avez lu')
        books_read = input('Veuillez saisir les chiffres :').split()
    error_in_books_read = not_number_input(books_read)
    if error_in_books_read == False:
        books_read = [int(b_values) for b_values in books_read]
        books_read_in_books = listnumber_in_list_books_number(books_read)
        if books_read_in_books == False:
            print("un des numéro saisi ne se trouve pas dans les numéro attribués aux livres.")
    else:
        books_read_in_books = False
        print("veuillez ne pas écrire de lettre ou utiliser d'autres caractères mis a part les chiffres. ")

    while (books_read_in_books == False or error_in_books_read == True):
        print('Veuillez espacer les chiffres des livres que vous avez lu')
        books_read = input('Veuillez saisir les chiffres : ').split()
        while (books_read == []):
            print('Veuillez espacer les chiffres des lettres des livres que vous avez lu')
            books_read = input('Veuillez saisir les chiffres : ').split()
        error_in_books_read = not_number_input(books_read)
        if error_in_books_read == False:
            books_read = [int(b_values) for b_values in books_read]
            books_read_in_books = listnumber_in_list_books_number(books_read)
            if (books_read_in_books == False):
                print('un des numéro saisi ne se trouve pas dans les numéro attribués aux livres.')
        else:
            books_read_in_books = False
            print("veuillez ne pas écrire de lettre ou utiliser d'autres caractères mis a part les chiffres. ")
    return books_read


def catch_index(file_name, name_to_catch_index):
    with open(file_name, 'r', encoding='utf-8') as catch_index_var:
        list_content = catch_index_var.readlines()
    for content in range(len(list_content)):
        list_content[content] = list_content[content].split(',')
        if name_to_catch_index == list_content[content][0]:
            return content


def not_number_input(mylist):
    for i in range(0, len(mylist)):
        for element in error_element:
            if element in mylist[i]:
                return True
    return False


def listnumber_in_list_books_number(nlist):
    with open('books.txt', 'r', encoding='utf-8') as books_info_file:
        number_book = len(books_info_file.readlines())
    for elemen_ind in nlist:
        if elemen_ind < 1 or number_book < elemen_ind:
            return False
    return True





    """def supprimer_un_livre():
        nom_livre_sup = ask_book_name()
        nom_livresup_verifier = check_book_name(nom_livre_sup)
        while (nom_livresup_verifier == False):
            print("Ce livre existe n'existe pas \n veuillez saisir un autre nom")
            nom_livre = ask_book_name()
            nom_livresup_verifier= check_book_name(nom_livre_sup)
        n_livre_sup = input('Saisir le nom du nouveau livre : ')
        with open("books.txt","r",encoding='utf-8') as supl_db:
            sup_livre = supl_db.readlines(nom_livre_sup)
            i = 0
            trouve = False
            while ( i < len(sup_livre) and not trouve):
                l = sup_livre[i].split(",")
                if nom_livre_sup in l :
                    sup_livre.remove(sup_livre[i])
                    print("Le livre {} est supprimé ".format(nom_livre_sup))
                    trouve = True
                    i += 1
                if not trouve:
                    print("Le livre n'existe pas")
                else:
                    with open("books.txt","w",encoding='utf-8') as sup2_livre_db:"""














""""Partie III : Recommandation"""





