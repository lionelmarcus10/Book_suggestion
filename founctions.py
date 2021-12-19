from listes import *
import time
import timeit
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
    h = input("Voulez-vous noter un livre ? Tapez Oui ou Non :")
    while(h!='Oui' and h !='Non'):
        h = input("Voulez-vous noter un livre ? Tapez Oui ou Non :")
    if h == 'Oui':
        noter_un_livre(nompseudo)

    retour_menu(1)



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

    # prendre son index
    with open('matrice.txt','r') as m1:
        matrice = m1.readlines()
    matrice.remove(matrice[indexlecteur])
    with open('matrice.txt', 'w') as m1:
        for v in range(0,len(matrice)):
            m1.write(matrice[v])

    retour_menu(1)



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

                         print("-",livres1[i-1])
     retour_menu(1)



""" la fonction modifier_un_lecteur peut modifier les informations du profil d’un lecteur donné."""




def modifier_un_lecteur():
    nommodif = demander_un_pseudonyme()
    nommodifverifier = verifier_un_lecteur(nommodif)
    index_profile = trouver_index('readers.txt', nommodif)
    while nommodifverifier == False:
        print("Ce lecteur n'existe pas, veuillez saisir un nom de lecteur correcte ")
        nommodif = demander_un_pseudonyme()
        nommodifverifier = verifier_un_lecteur(nommodif)
    print("Tapez: \n1-Pour modifier votre Pseudonym\n2-Pour modifier votre genre\n3-Pour modifier votre age\n4-Pour modifier votre style de lecture\n5-Pour modifier les livres lu")
    modifioptions = input("Veuillez espacer les chiffres : ")
    modifioptions = modifioptions.split()

    modiffioptionerror = pas_entier(modifioptions)
    if modiffioptionerror == False:
        modifioptions = [int(i) for i in modifioptions]
        for number_mod in modifioptions:
            if number_mod < 1 or number_mod > 5:
                modiffioptionerror = True
    while modiffioptionerror == True or modifioptions == []:
        modifioptions = input("Veuillez espacer les chiffres : ")
        modifioptions = modifioptions.split()
        modiffioptionerror = pas_entier(modifioptions)
        if modiffioptionerror == False:
            modifioptions = [int(i) for i in modifioptions]
            for number_mod in modifioptions:
                if int(number_mod) < 1 or int(number_mod) > 5:
                    modiffioptionerror = True

    for options in modifioptions:
        if options == 1:
            npseudomod = input('Entrez votre nouveau pseudonyme :')
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
            nstylelecturemod = demander_style_de_lecture()
            number_input_style_de_lecture = nstylelecturemod in ['{}'.format(i) for i in range(1, 8)]
            while (number_input_style_de_lecture == False):
                nstylelecturemod = demander_style_de_lecture()
                number_input_style_de_lecture = nstylelecturemod in ['{}'.format(i) for i in range(1, 8)]

            with open('readers.txt', 'r', encoding='utf-8') as r_slmod:
                rslmodlist = r_slmod.readlines()
                with open('readers.txt', 'w', encoding='utf-8') as mod_sl_apply:
                    for lines in range(0, len(rslmodlist)):
                        lines_modsl = rslmodlist[lines].split(',')
                        if lines == index_profile:
                            lines_modsl[3] = str(nstylelecturemod)+'\n'
                            rslmodlist[lines] = ','.join(lines_modsl)
                            mod_sl_apply.write(rslmodlist[lines])
                        else:
                            mod_sl_apply.write(rslmodlist[lines])

        elif options == 5:
            if 1 not in modifioptions:
                modifier_livre_lu(nommodif)
            else:
                if modifioptions.index(5)<modifioptions.index(1):
                    modifier_livre_lu(nommodif)
                else:
                        x = input('Entrez une nouvelle fois votre pseudo :')
                        y = verifier_un_lecteur(x)
                        if y == False:
                            print("Le pseudonyme saisi est incorrecte la modification n'a pas pu etre réalisé")
                        else:
                            modifier_livre_lu(x)


    retour_menu(1)

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
    with open('books.txt','r',encoding='utf-8') as afficherunlivre:
        books_names_index = 1
        for books_names in afficherunlivre:
            print('{} - {}'.format(books_names_index,books_names))
            time.sleep(0.2)
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

    with open('matrice.txt','r') as m1:
        matrice = m1.readlines()
    with open('matrice.txt', 'w') as m1:
        for a in range(0,len(matrice)):
            matrice[a] = matrice[a].split()
            for b in range(0,len(matrice[a])):
                matrice[a][b] = int(matrice[a][b])
            matrice[a].append('0\n')
            for c in range(0,len(matrice[a])-1):
                matrice[a][c] = str(matrice[a][c])
            matrice[a] = ' '.join(matrice[a])
            m1.write(matrice[a])
    retour_menu(2)


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
    retour_menu(2)



    """                     fonction utilisé dans plusieur parti                    """


def modifier_livre_lu(pseudo):
    books_read_2 = demander_livre_lu()
    with open("booksread.txt", "r", encoding='utf-8') as booksreadmodifdb:
        livrelumodiflist = booksreadmodifdb.readlines()
        ancienlivrematrice = livrelumodiflist

        # recuperer ancien livres => ancienlivrematrice + chercher sa ligne et append pour trouver indices
        indexnom = trouver_index('booksread.txt', pseudo)
        ancienlivres = ancienlivrematrice[indexnom].split(',')[1:]
        for a in range(0, len(ancienlivres)):
            ancienlivres[a] = int(ancienlivres[a])

        with open("booksread.txt", "w", encoding='utf-8') as booksreadmodifdb2:
            for index_info in range(len(livrelumodiflist)):
                infos_split = livrelumodiflist[index_info].split(',')
                if infos_split[0] == pseudo:
                    livrelumodiflist[index_info] = [pseudo] + [str(i) for i in books_read_2]
                    livrelumodiflist[index_info] = ','.join(livrelumodiflist[index_info])
                    booksreadmodifdb2.write(livrelumodiflist[index_info] + '\n')
                else:
                    booksreadmodifdb2.write(livrelumodiflist[index_info])

    # ancien  2 3 4 5 6
    # new     2 3 0 5 0
    # recuperer new livres => books_read_2 index

    # prendre dans une liste les elements des anciens livres qui ne sont pas dans les nouveaux
    l = []
    for b in range(0,len(ancienlivres)):
        if ancienlivres[b] not in books_read_2:
            l.append(ancienlivres[b])

    # comparer indexes pour trouver les livres non qui ne sont dans la liste des nouveaux livres et les remplacer par 0

    with open('matrice.txt','r') as m1:
        matrice = m1.readlines()
    with open('matrice.txt','w') as m1:
        for c in range(0,len(matrice)):
            if c != indexnom:
                m1.write(matrice[c])
            elif c == indexnom:
                matrice[c]= matrice[c].split()
                for d in range(0,len(matrice[c])):
                    matrice[c][d] = int(matrice[c][d])

                for e in l:
                    matrice[c][e-1] = 0
                for f in range(0,len(matrice[c])):
                    matrice[c][f]= str(matrice[c][f])
                matrice[c] = ' '.join(matrice[c]) + '\n'
                m1.write(matrice[c])




def demander_livre_lu():
    print("quels sont les livres que vous avez déjà lu ? : \n")
    afficher_un_livre()
    print('\nVeuillez espacer les chiffres des lettres des livres que vous avez lu')
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
    print('Bienvenu \n')
    time.sleep(1)
    print("Nous vous prions de bien vouloir suivre les consignes \n")
    time.sleep(2)
    print("Tout au long de ce programme, vous allez devoir lire attentivement ce qui est écrit \n")
    time.sleep(1)


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


def pas_entier(malist):
    for i in range(0, len(malist)):
        for element in error_element:
            if element in malist[i]:
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
    with open("books.txt","w",encoding='utf-8') as sup2livredb:
        for h in suplivre:
            sup2livredb.write(h)

    with open("matrice.txt",'r') as m1:
        matrice = m1.readlines()
    with open("matrice.txt", 'w') as m1:
        for lignes in range(0,len(matrice)):
            matrice[lignes] = matrice[lignes].split()
            del matrice[lignes][indexlivre]
            matrice[lignes][-1] = str(int(matrice[lignes][-1]))+'\n'
            matrice[lignes] = ' '.join(matrice[lignes])
            m1.write(matrice[lignes])

    indexlivre+=1

    with open("booksread.txt","r",encoding='utf-8') as sup3livredb:
        sup3livre= sup3livredb.readlines()

    with open("booksread.txt","w",encoding='utf-8')as sup3livredb:
        for z in range(0,len(sup3livre)):
            sup3livre[z]= sup3livre[z].split(',')
            for o in range(1,len(sup3livre[z])):
                sup3livre[z][o] = int(sup3livre[z][o])
            if indexlivre in sup3livre[z]:
                sup3livre[z].remove(indexlivre)
            for w in range(1,len(sup3livre[z])):
                if sup3livre[z][w] > indexlivre:
                    sup3livre[z][w] -= 1
                    sup3livre[z][w] = str(sup3livre[z][w])
            for cpt in range(0,len(sup3livre[z])):
                sup3livre[z][cpt] = str(sup3livre[z][cpt])
            sup3livre[z] = ','.join(sup3livre[z]) + '\n'
            sup3livredb.write(sup3livre[z])

    retour_menu(2)





# appel de la fonction qui crée la matrice




# Fonction pour noter un livre
def noter_un_livre(pseudo):

    x = verifier_un_lecteur(pseudo)
    while x == False:
        pseudo = input("Veuillez saisir un nom:")
        x = verifier_un_lecteur(pseudo)

    index_lecteur = trouver_index('readers.txt', pseudo)
    print()

    with open('booksread.txt','r',encoding='utf-8') as livrelu3:
        livrelu2= livrelu3.readlines()[index_lecteur].split(',')[1:]
        for n in range(0,len(livrelu2)):
            livrelu2[n] = int(livrelu2[n])
    with open('books.txt','r',encoding='utf-8') as livrelulist:
            livrelist = livrelulist.readlines()
            livrelulist2=[]
            for i in range(0,len(livrelu2)):
                livrelulist2.append(livrelist[livrelu2[i]-1])
    print("Voici les livres que vous avez lu:\n")
    for cpt in range(0, len(livrelu2)):
        print('-',livrelulist2[cpt])


    livrenom = input("Entrez le nom du livre que vous voulez noter : ")
    y = verifier_livre(livrenom)
    y2 = False
    for x in range(0,len(livrelu2)):
        if livrenom+'\n'==livrelulist2[x]:
            y2=True

    while(y == False or y2==False):
        print("Vous n'avez pas lu ce livre, veuillez saisir un autre nom de livre\nou un bon nom")
        livrenom = input("Entrez le nom du livre (lu) que vous voulez noter : ")
        y = verifier_livre(livrenom)
        y2 = False
        for x in range(0, len(livrelu2)):
            if livrenom + '\n' == livrelulist2[x]:
                y2 = True

    index_livre = trouver_index("books.txt", livrenom)
    note = input("Attribuez une note sur 5 au livre : ")
    while (note > '5' or note < '1'):
        note = input("Attribuez une note (un entier ) entre 1 et 5 au livre : ")

    with open("matrice.txt","r",encoding='utf-8') as misejourmatrice:
        matrice1 = misejourmatrice.readlines()

    if index_lecteur < len(matrice1):
        for i in range(0,len(matrice1)):
            matrice1[i] = matrice1[i].split(" ")
            for z in range(0,len(matrice1[i])):
                matrice1[i][z] = int(matrice1[i][z])
        matrice1[index_lecteur][index_livre] = note
        for a in range(0,len(matrice1)):
            for k in range(0,len(matrice1[a])):
                matrice1[a][k] = str(matrice1[a][k])
            matrice1[a] = ' '.join(matrice1[a])
        for b in range(0,len(matrice1)):
            matrice1[b] = matrice1[b] + '\n'

    else:
        l1= matrice1[0].replace(' ','')
        m=[]
        for col in range(0,len(l1)-1):
            if col == index_livre:
                m.append(str(note))
            else:
                m.append(str(0))
        m=' '.join(m)
        m=m+'\n'
        matrice1.append(m)

    with open("matrice.txt",'w',encoding='utf-8') as matrice2:
        for r in matrice1:
            matrice2.write(r)

    retour_menu(3)




# fonction pour retourner en arrière ou au menu principal après une action

def retour_menu(y):
    x = input("Saisir 1 pour retourner en arrière et 2 pour retourner au menu principal : ")
    while (x != '1' and x != '2'):
        x = input("Saisir 1 pour retourner en arrière et 2 pour retourner au menu principal : ")
    if x=='1':
        menu_de_lancement(y)
    else:
        menu_de_lancement()

# utilisation du paramètre *args autorisé par la prof ASMA GABIS
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
            retour_menu(2)
        elif option_depot_livre == 2:
            ajouter_un_livre()
        elif option_depot_livre == 3:
            modifier_un_livre()
        elif option_depot_livre == 4:
            supprimer_un_livre()

    elif menu == 3:
        option_recommandation = demander_option_recommandation_livre()
        if option_recommandation == 1:
            x=input('Votre pseudonyme : ')
            noter_un_livre(x)
        elif option_recommandation == 2:
            suggerer_un_livre()






""""Partie III : Recommandation"""

def calcul_matrice(a,b,matrice):
        s1 = 0
        s2 = 0
        produit = 0
        for k in range(0,len(matrice[a])):
            produit = produit + matrice[a][k] * matrice[b][k]
            s1 = s1 + matrice[a][k]**2
            s2 = s2 + matrice[b][k]**2
        return round(( produit / ( sqrt(s1) * sqrt(s2) ) ),2)

def matrice_recommandation():
    # recuperer les notes dans matrice.txt dans une variable nommé matrice
    with open('matrice.txt', 'r') as m1:
        matrice = m1.readlines()
    for z in range(0, len(matrice)):
        matrice[z] = matrice[z].split()
        for k in range(0, len(matrice[z])):
            matrice[z][k] = int(matrice[z][k])

    # création de la matrice de similarité et remplissage de la diagonale
    matricesimil = []
    for i in range(0,len(matrice)):
        x = []
        for k in range(0,len(matrice)):
            if i == k:
                x.append(1.0)
            else:
                x.append(0)
        matricesimil.append(x)

    # remplir la matrice de similarité
    for h in range(0,len(matrice)):
        for j in range(0,len(matrice)):
            if h < j:
                matricesimil[h][j] = calcul_matrice(h,j,matrice)
            elif h>j :
                matricesimil[h][j] = matricesimil[j][h]
    return matricesimil

# matrice pour suggerer un livre au lecteur

def suggerer_un_livre():
    # récuperer et verifier le nom du lecteur
    nom = demander_un_pseudonyme()
    x = verifier_un_lecteur(nom)
    while x == False:
        nom = demander_un_pseudonyme()
        x = verifier_un_lecteur(nom)

    #calculer la matrice de similarité du lecteur
    index1 = trouver_index('booksread.txt',nom)
    matricesimilarite1 = matrice_recommandation()[index1]

    # recuperer l'index de la personne ayant la plus grande similitude avec le lecteur
    maximum = 0
    index2 = 0
    for z in range(0,len(matricesimilarite1)):
        if matricesimilarite1[z] > maximum and matricesimilarite1[z] < 1:
            maximum = matricesimilarite1[z]
            index2 = z

    # recuperer les livres lu par les deux lecteurs
    with open('booksread.txt','r',encoding="utf-8") as booksread:
        livreslu = booksread.readlines()
    l1 = livreslu[index1].split(',')
    l1 = l1[1:]
    l2 = livreslu[index2].split(',')
    l2 = l2[1:]
    for q in range(0,len(l1)):
        l1[q] = int(l1[q])
    for s in range(0,len(l2)):
        l2[s] = int(l2[s])

    # recuperer le livre à suggerer au lecteur
    l3 = []
    for h in l2:
        if h not in l1:
            l3.append(h)


    # suggerer le livre à l'utilisateur
    with open('books.txt','r',encoding='utf-8') as livresdb:
        livres = livresdb.readlines()
    print("les livres que nous vous recommandons de lire sont : \n")
    for i in range(0,len(l3)):
        print(i+1,'-',livres[l3[i]-1])

    nlivre=input("\nVoulez-vous selectioner un livre ? Tapez Oui ou Non :")
    while nlivre!="Oui" and nlivre !="Non":
        nlivre = input("\nVoulez-vous selectioner un livre ? Tapez Oui ou Non :")

    if nlivre=="Oui":
        for i in range(0, len(l3)):
            print(l3[i],'-', livres[l3[i] - 1])
        for j in range(0, len(l3)):
            l3[j] = str(l3[j])
        livrenumero=input("Veuillez saisir le numéro du livre que vous avez choisi :")
        while(livrenumero not in l3):
            livrenumero = input("Veuillez saisir un numéro valide :")
        with open('booksread.txt','r',encoding='utf-8') as booksread2:
            x = booksread2.readlines()
        with open('booksread.txt','w',encoding='utf-8') as booksread2:
            for w in range(0,len(x)):
                v =  x[w].split(',')
                if v[0]== nom:
                    for cpt in range(1,len(v)):
                        v[cpt] = int(v[cpt])
                    v.append('{}\n'.format(livrenumero))
                    for cpt2 in range(1,len(v)-1):
                        v[cpt2] = str(v[cpt2])
                    v = ','.join(v)
                    booksread2.write(v)
                else:
                    booksread2.write(x[w])

    else:
        print("N'oubliez pas de noter un de ces livres après leur lecture")
    retour_menu(3)



#print(timeit.timeit("matrice_recommandation()",setup="from __main__ import matrice_recommandation",number=100000))

# 0.0009906291961669922
# 0.0009894371032714844

