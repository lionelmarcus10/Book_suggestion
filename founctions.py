from listes import *
import time
from math import sqrt


"""Partie I : Profils des lecteurs"""

""""Une fonction qui permet de demander le pseudonyme"""

def demander_un_pseudonyme():
    pseudonyme = str(input("Entrez votre pseudonyme : "))
    return pseudonyme


"""Une fonction qui demande le sexe de l'utilisateur """

def demander_genre():
    print("Quel est votre genre ? ","\n","Tapez le numéro qui vous correspondent : ")
    print("1 - HOMME ")
    print("2 - FEMME ")
    print("3 - PEU IMPORTE ")
    genre=(input("..."))
    while (genre != '1' and genre != '2' and genre != '3' ) :
        print("Quel est votre genre ? ", "\n", "Tapez le numéro qui vous correspondent : ")
        print("1 - HOMME ")
        print("2 - FEMME ")
        print("3 - PEU IMPORTE ")
        genre = (input("..."))
    return genre


"""Une fonction qui demande  l'âge de l'utilisateur"""

def demander_age():
    print("Quel est votre âge ? ","\n"," Tapez le numéro 1 ou 2 ou 3 pour saisir votre âge ")
    print("1 - <= 18 ans")
    print("2 - Entre 18 ans et 25 ans")
    print('3 - > 25 ans ')
    age = (input("..."))
    while (age != '1' and age != '2' and age != '3' ) :
        print(" Quel est votre genre ? ", "\n", "Tapez le numéro qui vous correspond")
        print("1 - <= 18 ans")
        print("2 - Entre 18 ans et 25 ans")
        print('3 - > 25 ans ')
        age = (input("..."))
    return age


"""Une fonction qui permet de savoir le style de lecture"""


def demander_style_de_lecture():
    print("Quel est votre style de lecture ? ","\n","Tapez le numéro qui vous correspond")

    for k in range(0,len(liste_style_de_lecture)):
        print(k+ 1,' - ',liste_style_de_lecture[k])
    style = input("Saisir le numéro corrospondant à votre style de lecture : ")
    while ( style < '1' or style > '7' or style != str(style)):
        style =input("Saisir le numéro corrospondant à votre style de lecture :")

    return str(style)

""""Une fonction qui donne le menu qui proposer par ce programme """

def menu_principal():
    print("Tapez le numéro qui vous correspond : ")
    print("1 - Profils des lecteurs")
    print("2 - Visiter le dépôt des livres")
    print("3 - Recommandation")
    choix = (input(" ... "))
    while ( choix !='1' and choix !='3' and choix!= '2'):
        choix = (input("Saissez à nouveau le numéro : "))
    return int(choix)

"""" une fonction qui permet .................."""

def demander_option_profile():
    print("Tapez le numéro qui vous correspond :")
    print("1 - Ajouter un lecteur")
    print("2 - Afficher un lecteur")
    print("3 - Modifier un lecteur")
    print("4 - Supprimer un lecteur")
    profilmenu = input(" Saisisez le numéro : ")
    while (profilmenu  != '1' and profilmenu  !='2' and profilmenu  != '3'and profilmenu  != '4'):
        profilmenu  = input(" Saisisez à nouveau le numéro : ")
    return int(profilmenu)

def demander_option_depot_livre():
    print("Tapez le numéro qui vous correspond ")
    print(" 1 - Afficher la liste des livres dans le dépôt  \n 2 - Ajouter un livre au dépôt \n 3 - Modifier le titre d’un livre dans le dépôt \n 4 - Supprimer un livre du dépôt ")
    depotmenu = input(" ... ")
    while (depotmenu != '1' and depotmenu !='2'and depotmenu != '3'and depotmenu != '4' ):
        depotmenu = input(" Saisisez à nouveau le numéro ")
    return int(depotmenu)

"""une fonction qui affiche le menu de recommandation des livres......"""

def demander_option_recommandation_livre():
    print("Tapez le numéro qui vous correspond")
    print("1 - Noter un livre")
    print("2 - Suggére des livres")
    livrerecomenu = input("Saisissez le numéro ")
    while (livrerecomenu !='1' and livrerecomenu != '2'):
        livrerecomenu = input(" Saisissez à nouveau le numéro ")
    return int(livrerecomenu)

""" -----------------------------------------------------------------------------------------------------"""
""""Une fonction qui vérifie si un lecteur existe déja"""

def verifier_un_lecteur(nom_utilisateur):
    with open('readers.txt' , 'r',encoding='utf-8') as verifierprofil:
        verifierprofillist = verifierprofil.readlines()
        for i in range(len(verifierprofillist)):
            profilindi = verifierprofillist[i]
            valeur = profilindi.split(",")
            if valeur[0]== nom_utilisateur:
                return True
    return False



"""une fonction qui ajoute un lecteur"""

def ajouter_un_lecteur():

    nompseudo = demander_un_pseudonyme()
    nompseudoverifier = verifier_un_lecteur(nompseudo)
    while nompseudoverifier == True:
        print("Ce lecteur existe déjà, veuillez saisir un nom different ")
        nompseudo = demander_un_pseudonyme()
        nompseudoverifier = verifier_un_lecteur(nompseudo)
    numerogenre = demander_genre()
    numeroage = demander_age()
    numero_style_lecture = demander_style_de_lecture()
    with open("readers.txt", "a",encoding='utf-8') as readers_db:
        readers_db.write(nompseudo +"," + numerogenre + ','+ numeroage +','+ numero_style_lecture+ '\n')
    booksread = demander_livre_lu()
    booksreadstr = [str(i) for i in booksread]
    books_read_to_file = ','.join(booksreadstr)
    with open("booksread.txt", "a", encoding='utf-8') as booksreaddb:
        booksreaddb.write(nompseudo + ','+ books_read_to_file + '\n')



""""Une fonction qui supprime un lecteur"""
def supprimer_un_lecteur():
    nomsup = demander_un_pseudonyme()
    nomsupverifier = verifier_un_lecteur(nomsup)
    if nomsupverifier == True :
        indexlecteur= trouver_index('booksread.txt',nomsup)
    while nomsupverifier == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        nomsup = demander_un_pseudonyme()
        nomsupverifier = verifier_un_lecteur(nomsup)
        if nomsupverifier == True:
            indexlecteur = trouver_index('booksread.txt', nomsup)
    with open("readers.txt", "r",encoding='utf-8') as readers_db:
        suplecteur= readers_db.readlines()
        i=0
        trouve = False
        while( i<len(suplecteur) and not trouve):
            l= suplecteur[i].split(",")
            if nomsup in l :
                 suplecteur.remove(suplecteur[i])
                 print('lecteur {} deleted'.format(nomsup))
                 trouve=True
            i+=1
        if not trouve:
            print("Ce lecteur n'existe pas")
        else:
            with open("readers.txt", "w",encoding='utf-8') as readersdb:
                for lecteurrestant in suplecteur:
                    readersdb.write(lecteurrestant)


    with open("booksread.txt","r",encoding='utf-8') as booksreaddb:
        suplecteurbooksreadlist = booksreaddb.readlines()

        del suplecteurbooksreadlist[indexlecteur]
        with open("booksread.txt","w",encoding='utf-8') as booksreddb2:
            for l in suplecteurbooksreadlist:
                booksreddb2.write(l)



""""la fonction afficher_un_lecteur peut afficher le profil d’un lecteur donné """

def afficher_un_lecteur():
     aflecteur = demander_un_pseudonyme()
     aflecteurverifier = verifier_un_lecteur( aflecteur)
     while aflecteurverifier == False:
         aflecteur = demander_un_pseudonyme()
         aflecteurverifier = verifier_un_lecteur( aflecteur)
     with open("readers.txt","r",encoding='utf-8') as affichier_db:
            affichier_lecteur = affichier_db.readlines()
     for lines in affichier_lecteur:
         if aflecteur in lines:
              lines = lines.replace(","," ").split()
              lines[1] = liste_genre[int(lines[1])-1]
              lines[2] = liste_age[int(lines[2]) - 1]
              lines[3] = liste_style_de_lecture[int(lines[3])-1]
              print("Le lecteur s'est inscrit sous le pseudonyme {}, c'est un {}, âgé {} et qui aime lire des livres {} ".format(lines[0],lines[1],lines[2],lines[3]))



     with open("booksread.txt","r",encoding='utf-8') as bookread_db :
         lecteurs = bookread_db.readlines()
         livreluindex = trouver_index("booksread.txt",aflecteur)
         lecteur= lecteurs[livreluindex].split(",")
         for z in range(1,len(lecteur)):
             lecteur[z]=int(lecteur[z])

         if aflecteur == lecteur[0]:
             livreslu = lecteur[1:]

             with open("books.txt","r",encoding='utf-8') as books_db:
                 livres1= books_db.readlines()
                 if livreslu == ["0"]:
                     print("{} n'a lu auccun livre".format(aflecteur))
                 else:
                     print("{} a lu : ".format(aflecteur),"\n")
                     for i in livreslu:
                        print("-",livres1[i])







"""   for d in range(0,len(livres_lue_index)):
     livres_lue_index[d] = int(livres_lue_index[d])
 with open("books.txt","r",encoding='utf-8') as books_db:
     livres = books_db.readlines()
     for z in range(0,len(livres_lue_index)):
         print(livres[livres_lue_index[z]],end='-')


trouve = True
i+=1"""




""" la fonction modifier_un_lecteur peut modifier les informations du profil d’un lecteur donné."""




def modifier_un_lecteur():
    nommodif = demander_un_pseudonyme()
    nommodifverifier = verifier_un_lecteur(nommodif)
    index_profile = trouver_index('readers.txt', nommodif)
    while nommodifverifier == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        nommodif = demander_un_pseudonyme()
        nommodifverifier = verifier_un_lecteur(nommodif)

    modifioptions = input("Veuillez espacer les chiffres : ")
    modifioptions = modifioptions.split()

    modiffioptionerror = pas_entier(modifioptions)
    if modiffioptionerror == False:
        modifi_options = [int(i) for i in modifioptions]
        for number_mod in modifi_options:
            if number_mod < 1 or number_mod > 5:
                modiffioptionerror = True
    while modiffioptionerror == True or modifioptions == []:
        modifioptions = input("Veuillez espacer les chiffres : ")
        modifioptions = modifioptions.split()
        modiffioptionerror = pas_entier(modifioptions)
        if modiffioptionerror == False:
            modifi_options = [int(i) for i in modifioptions]
            for number_mod in modifioptions:
                if number_mod < 1 or number_mod > 5:
                    modiffioptionerror = True

    for options in modifioptions:
        if options == 1:
            npseudomod = demander_un_pseudonyme()
            npseudoverfif = verifier_un_lecteur(npseudomod)
            while (npseudoverfif == True):
                print('Ce lecteur existe déja. \n veuillez saisir un autre pseudsonyme')
                npseudomod = demander_un_pseudonyme()
                npseudoverfif = verifier_un_lecteur(npseudomod)
            with open('readers.txt', 'r', encoding='utf-8') as r_pmod:
                rpmodlist = r_pmod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_p_apply:
                    for lines in range(len(rpmodlist)):
                        linesmodp = rpmodlist[lines].split(',')
                        if linesmodp[0] == nommodif:
                            rpmodlist[lines] = npseudomod + ',' + ','.join(linesmodp[1:])
                            mod_p_apply.write(rpmodlist[lines])
                        else:
                            mod_p_apply.write(rpmodlist[lines])

        elif options == 2:
            ngenremod = demander_genre()
            while (ngenremod != '1' and ngenremod != '2' and ngenremod != '3'):
                ngenremod = demander_genre()
            with open('readers.txt', 'r', encoding='utf-8') as r_gmod:
                r_gmod_list = r_gmod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_g_apply:
                    for lines in range(0, len(r_gmod_list)):
                        lines_modg = r_gmod_list[lines].split(',')
                        if lines == index_profile:
                            lines_modg[1] = ngenremod
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
            modifier_livre_lu(nommodif)

""""Fin de la 1er parti"""






"""Partie II : Visiter le dépôt des livres"""

def demander_le_nom_livre():
    book_name = input('Saisir le nom du livre : ')
    return book_name


def verifier_livre(nom_livre):
    with open('books.txt' , 'r',encoding='utf-8') as books_checkers:
        list_books_checker = books_checkers.readlines()
        for index_books in range(len(list_books_checker)):
            books_ind_data = list_books_checker[index_books]
            if books_ind_data == nom_livre + '\n':
                return True
    return False


def afficher_un_livre():
    with open('books.txt','r',encoding='utf-8') as afficher_un_livre:
        books_names_index = 1
        for books_names in afficher_un_livre:
            print('{} - {}'.format(books_names_index,books_names), end='')
            books_names_index+=1


def ajouter_un_livre():
    book_name = demander_le_nom_livre()
    book_name_verified = verifier_livre(book_name)
    while (book_name_verified == True):
        print('Ce livre existe déjà \n veuillez saisir un autre nom')
        book_name = demander_le_nom_livre()
        book_name_verified = verifier_livre(book_name)
    with open("books.txt", "a",encoding='utf-8') as books_db:
        books_db.write(book_name + '\n')


def modifier_un_livre():
    book_title = demander_le_nom_livre()
    book_title_verified = verifier_livre(book_title)
    while (book_title_verified == False):
        print("Ce livre existe n'existe pas \n veuillez saisir un autre nom")
        book_title = demander_le_nom_livre()
        book_title_verified = verifier_livre(book_title)
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




"""fonction utilisé dans plusieur parti"""


def modifier_livre_lu(my_user_pseudo_to_modify):
    books_read_2 = demander_livre_lu()
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







def demander_livre_lu():
    print("quels sont les livres que vous avez déjà lu ? : ")
    time.sleep(3)
    afficher_un_livre()
    time.sleep(3)
    print('Veuillez espacer les chiffres des lettres des livres que vous avez lu')
    books_read = input('Veuillez saisir les chiffres :').split()
    while (books_read == []):
        print('Veuillez espacer les chiffres des lettres des livres que vous avez lu')
        books_read = input('Veuillez saisir les chiffres :').split()
    error_in_books_read = pas_entier(books_read)
    if error_in_books_read == False:
        books_read = [int(b_values) for b_values in books_read]
        books_read_in_books = numero_de_livre_validation(books_read)
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
        error_in_books_read = pas_entier(books_read)
        if error_in_books_read == False:
            books_read = [int(b_values) for b_values in books_read]
            books_read_in_books = numero_de_livre_validation(books_read)
            if (books_read_in_books == False):
                print('un des numéro saisi ne se trouve pas dans les numéro attribués aux livres.')
        else:
            books_read_in_books = False
            print("veuillez ne pas écrire de lettre ou utiliser d'autres caractères mis a part les chiffres. ")
    return books_read

# Fonction qui affiche des consignes / conseils a l'utilisateur
def explication_processus():
    time.sleep(1)
    print('Bienvenu \n')
    time.sleep(2)
    print("Nous vous prions de bien vouloir suivre les consignes \n")
    time.sleep(3)
    print("Tout au long de ce programme, vous allez devoir lire attentivement ce qui est écrit \n")
    time.sleep(2)


def trouver_index(file_name, name_to_trouver_index):
    if file_name =='books.txt':
        with open(file_name, 'r', encoding='utf-8') as trouver_index_var:
            list_content = trouver_index_var.readlines()
        for content in range(len(list_content)):
            if name_to_trouver_index + '\n' == list_content[content]:
                return content
    else:
        with open(file_name, 'r', encoding='utf-8') as trouver_index_var:
            list_content = trouver_index_var.readlines()
        for content in range(len(list_content)):
            list_content[content] = list_content[content].split(',')
            if name_to_trouver_index == list_content[content][0]:
                return content


def pas_entier(mylist):
    for i in range(0, len(mylist)):
        for element in error_element:
            if element in mylist[i]:
                return True
    return False


def numero_de_livre_validation(nlist):
    with open('books.txt', 'r', encoding='utf-8') as books_info_file:
        number_book = len(books_info_file.readlines())
    for elemen_ind in nlist:
        if elemen_ind < 0 or number_book < elemen_ind:
            return False
    return True


def supprimer_un_livre():
    nomlivresup = demander_le_nom_livre()
    nomlivresupverifier = verifier_livre(nomlivresup)
    if nomlivresupverifier == True:
        indexlivre = trouver_index("books.txt",nomlivresup)
    while (nomlivresupverifier == False):
        print("Ce livre existe n'existe pas \n veuillez saisir un autre nom")
        nomlivresup = demander_le_nom_livre()
        nomlivresupverifier = verifier_livre(nomlivresup)
        if nomlivresupverifier == True:
            indexlivre = trouver_index("books.txt",nomlivresup)
    with open("books.txt","r",encoding='utf-8') as supldb:
        suplivre = supldb.readlines()
    del suplivre[indexlivre]
    """with open("books.txt","w",encoding='utf-8') as sup2livredb:
        for h in suplivre:
            sup2livredb.write(h)"""
    indexlivre+=1
    with open("booksread.txt","r",encoding='utf-8') as sup3livredb:
        sup3livre= sup3livredb.readlines()
    #with open("booksread.txt","w",encoding='utf-8')as sup3livredb:
    for z in range(0,len(sup3livre)):
        sup3livre[z]= sup3livre[z].split(',')
        for o in range(1,len(sup3livre[z])):
            sup3livre[z][o] = int(sup3livre[z][o])
            if sup3livre[z][o] == indexlivre:
                sup3livre[z][o] = 0
            elif sup3livre[z][o] > indexlivre:
                sup3livre[z][o] -= 1
            sup3livre[z][o] = str(sup3livre[z][o])
        ",".join(sup3livre[z])
        print(sup3livre)






""" for i in range(0,len(sup3livre)):
sup3livre[i]=sup3livre[i].split(",")
for j in range(1,len(sup3livre[i])):
sup3livre[i][j]=int(sup3livre[i][j])
if indexlivre == sup3livre[i][j]:
#del sup3livre[i][j]
elif indexlivre < sup3livre[i][j]:
sup3livre[i][j]= sup3livre[i][j]-1"""















""""Partie III : Recommandation"""


# -----------------------------------------------------------------------------------------------------------------------------

"""def matrice_init():
    with open('books.txt', 'r') as nombre_de_livre:
        nombre_de_livre = len(nombre_de_livre.readlines())
    with open('readers.txt', 'r') as nombre_de_lecteur:
        nombre_de_lecteur = len(nombre_de_lecteur.readlines())
    L = []
    for i in range(0, nombre_de_lecteur):
        L1 = []
        for j in range(0, nombre_de_livre):
            L1.append(str(0))
        L.append(L1)

    for z in range(0, len(L)):
        L[z] = ','.join(L[z])
    with open('matrice.txt', 'w') as matrice_initiation:
        for k in L:
            matrice_initiation.write(k + '\n')


matrice_init()"""


# matrice refresh ---> supression , ajout, modifier

# appel de la fonction qui crée la matrice




# Fonction pour noter un livre
def noter_un_livre(pseudo):
    x = verifier_un_lecteur(pseudo)
    while x == False:
        print("Cet utilisateur n'existe pas veuillez saisir un autre nom")
        x = verifier_un_lecteur(pseudo)
    index_lecteur = trouver_index('readers.txt', pseudo)
    print("Entrez le nom du livre que vous voulez noter : ")
    livre_note = demander_le_nom_livre()
    y = verifier_livre(livre_note)
    while y == False:
        print("Ce livre n'existe pas, veuillez saisir un autre nom de livre")
        livre_note = demander_le_nom_livre()
        y = verifier_livre(livre_note)
    index_livre = trouver_index("books.txt", livre_note)
    note = input("Attribuez une note sur 5 au livre : ")
    while (note > '5' and note < '1'):
        note = input("Attribuez une note (un entier ) entre 1 et 5 au livre : ")

    with open("matrice.txt","r",encoding='utf-8') as mise_a_jour_matrice:
        matrice1 = mise_a_jour_matrice.readlines()
    for i in range(0,len(matrice1)):
        matrice1[i] = matrice1[i].split(",")
        for z in range(0,len(matrice1[i])):
            matrice1[i][z] = int(matrice1[i][z])
    matrice1[index_lecteur][index_livre] = note
    for a in range(0,len(matrice1)):
        for k in range(0,len(matrice1[a])):
            matrice1[a][k] = str(matrice1[a][k])
        matrice1[a] = ','.join(matrice1[a])
    for b in range(0,len(matrice1)):
        matrice1[b] = matrice1 + '\n'

    with open("matrice.txt",'w',encoding='utf-8') as matrice2:
        for m in matrice1:
            matrice2.write(m)


# utilisation du paramètre *args autorisé par la prof ASMA GABIS
# fonction pour retourner en arrière ou au menu principal après une action
def retour_menu():
    x = input("Saisir 1 pour retourner en arrière et 2 pour retourner au menu principal : ")
    while (x != '1' and x != '2'):
        x = input("Saisir 1 pour retourner en arrière et 2 pour retourner au menu principal : ")
    menu_de_lancement(x)


# fonction pour le menu de lancement
def menu_de_lancement(*arg):
    if arg:
        menu = arg[0]
    else:
        menu = menu_principal()

    if menu == 1:
        option_utilisateur_profile = demander_option_profile()
        if option_utilisateur_profile == 1:
            ajouter_un_lecteur()
        elif option_utilisateur_profile == 2:
            afficher_un_lecteur()
        elif option_utilisateur_profile == 3:
            modifier_un_lecteur()
        elif option_utilisateur_profile == 4:
            supprimer_un_lecteur()

    elif menu == 2:
        option_depot_livre = demander_option_depot_livre()
        if option_depot_livre == 1:
            afficher_un_livre()
        elif option_depot_livre == 2:
            ajouter_un_livre()
        elif option_depot_livre == 3:
            modifier_un_livre()
        elif option_depot_livre == 4:
            supprimer_un_livre()

    elif menu == 3:
        option_recommandation = demander_option_recommandation_livre()
        if option_recommandation == 1:
            pass
        elif option_recommandation == 2:
            pass

if __name__ == '__main__':

    def matrice_recommandation():
        with open("matrice.txt",'r',encoding='utf-8') as matrice1:
            matrice2 = matrice1.readlines()
        for z in range(0,len(matrice2)):
            matrice2[z] = matrice2[z].split(' ')
            for i in range(0,len(matrice2[z])):
                matrice2[z][i] = int(matrice2[z][i])


        # matrice 2
        """for j in range(0,len(matrice2)):"""



    """matrice_recommandation()"""




