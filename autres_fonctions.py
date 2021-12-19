import time
#import timeit



# Une fonction qui permet de demander le pseudonyme

def demander_un_pseudonyme():
    pseudonyme = str(input("Entrez votre pseudonyme : "))
    return pseudonyme

# une fonction qui permet d'afficher les options disponible pour un utilisateur et lui demander son choix

def demander_option_profile():
    print("Tapez le numéro qui vous correspond :")
    print("1 - Ajouter un lecteur")
    print("2 - Afficher un lecteur")
    print("3 - Modifier un lecteur")
    print("4 - Supprimer un lecteur")
    profilmenu = input(" Saisisez un numéro : ")
    while (profilmenu  != '1' and profilmenu  !='2' and profilmenu  != '3'and profilmenu  != '4'):
        profilmenu  = input(" Saisisez à nouveau un numéro : ")
    return int(profilmenu)

# une fonction qui permet d'afficher les options disponible pour un livre et lui demander son choix

def demander_option_depot_livre():
    print("Tapez le numéro qui vous correspond ")
    print(" 1 - Afficher la liste des livres dans le dépôt  \n 2 - Ajouter un livre au dépôt \n 3 - Modifier le titre d’un livre dans le dépôt \n 4 - Supprimer un livre du dépôt ")
    depotmenu = input("Saisir un numéro : ")
    while (depotmenu != '1' and depotmenu !='2'and depotmenu != '3'and depotmenu != '4' ):
        depotmenu = input(" Saisisez à nouveau un numéro : ")
    return int(depotmenu)

"""une fonction qui affiche le menu de recommandation des livres"""
def demander_option_recommandation_livre():
    print("Tapez le numéro qui vous correspond")
    print("1 - Noter un livre")
    print("2 - Suggére des livres")
    livrerecomenu = input("Saisissez un numéro : ")
    while (livrerecomenu !='1' and livrerecomenu != '2'):
        livrerecomenu = input(" Saisissez à nouveau un numéro ")
    return int(livrerecomenu)


"""Une fonction qui vérifie si un lecteur existe déja"""

def verifier_un_lecteur(nom_utilisateur):
    with open('readers.txt' , 'r',encoding='utf-8') as verifierprofil:
        verifierprofillist = verifierprofil.readlines()
        for i in range(len(verifierprofillist)):
            profilindi = verifierprofillist[i]
            valeur = profilindi.split(",")
            if valeur[0]== nom_utilisateur:
                return True
    return False


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



def modifier_livre_lu(pseudo):
    books_read_2 = demander_livre_lu()
    with open("booksread.txt", "r", encoding='utf-8') as booksreadmodifdb:
        livrelumodiflist = booksreadmodifdb.readlines()
        ancienlivrematrice = livrelumodiflist

        # recuperer ancien livres => ancienlivrematrice + chercher sa ligne et append pour trouver indices
        indexnom = trouver_index('booksread.txt', pseudo)
        print(indexnom)
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


# Une fonction qui affiche les livre présents dans le dépot

def afficher_un_livre():
    with open('books.txt','r',encoding='utf-8') as afficherunlivre:
        books_names_index = 1
        for books_names in afficherunlivre:
            print('{} - {}'.format(books_names_index,books_names))
            time.sleep(0.2)
            books_names_index+=1

def demander_livre_lu():
    print("quels sont les livres que vous avez déjà lu ? : \n")
    afficher_un_livre()
    print("Saisir 0 si vous n'avez lu aucun livre")
    print('\nVeuillez espacer les chiffres des lettres des livres que vous avez lu ')
    books_read = input('Veuillez saisir les chiffres :').split()
    while (books_read == []):
        print('Veuillez espacer les chiffres des lettres des livres que vous avez lu ')
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
    if (len(books_read)>1 ) and (0 in books_read):
        print("Etant donné que vous avez saisir d'autre nombre que le 0, nous ne prendrons pas en compte le 0")
        books_read.remove(0)
    return books_read

# Fonction qui affiche des consignes / conseils a l'utilisateur
def explication_processus():
    print('Bienvenue !\n')
    time.sleep(1)
    print("Nous vous prions de bien vouloir suivre les consignes\n")
    time.sleep(1)
    print("Tout au long de ce programme, vous allez devoir lire attentivement ce qui est écrit\n")
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
    numbers = '0123456789'
    for chaine in malist:
        for char in chaine:
            if char not in numbers:
                return True
    return False


def numero_de_livre_validation(nlist):
    with open('books.txt', 'r', encoding='utf-8') as books_info_file:
        number_book = len(books_info_file.readlines())
    for elemen_ind in nlist:
        if elemen_ind < 0 or number_book < elemen_ind:
            return False
    return True

#print(timeit.timeit("matrice_recommandation()",setup="from __main__ import matrice_recommandation",number=100000))

# Pour 10**5 essaies ( 100 milles essaies ) le temps de calcul est de 55.5902108 s

#Alors que la matrice non optimisé ( non présente dans notre code ) est de : 86.4976687999999 s