# Ce fichier contient toute les fonctions de la deuxième partie.
# C'est à dire les fonctions liés au dépôt de livre.


# Importer les différents modules necessaire
import time

from autres_fonctions import demander_le_nom_livre, trouver_index, verifier_livre


# Une fonction qui ajoute un livre dans le dépot

def ajouter_un_livre():
    book_name = demander_le_nom_livre()
    book_name_verified = verifier_livre(book_name)
    while (book_name_verified == True):
        print('Ce livre existe déjà \n Veuillez saisir un autre nom ')
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


# Une fonction qui modifie le nom d'un livre

def modifier_un_livre():
    book_title = demander_le_nom_livre()
    book_title_verified = verifier_livre(book_title)
    while (book_title_verified == False):
        print("Ce livre existe n'existe pas \n Veuillez saisir un autre nom ")
        book_title = demander_le_nom_livre()
        book_title_verified = verifier_livre(book_title)
    new_title_of_book = input('Saisir le nom du nouveau livre : ')
    with open("books.txt", "r", encoding='utf-8') as books_db:
        list_books_db = books_db.readlines()
        with open('books.txt','w', encoding='utf-8') as books_modification_part:
            for books in list_books_db:
                if book_title + '\n' == books:
                    books_modification_part.write(new_title_of_book + '\n')
                    print(book_title,'modifié en ', new_title_of_book)
                else:
                    books_modification_part.write(books)


# Une fonction qui supprime un livre dans le dépôt de livre

def supprimer_un_livre():
    nomlivresup = demander_le_nom_livre()
    nomlivresupverifier = verifier_livre(nomlivresup)
    if nomlivresupverifier == True:
        indexlivre = trouver_index("books.txt",nomlivresup)
    while (nomlivresupverifier == False):
        print("Ce livre existe n'existe pas \n Veuillez saisir un autre nom ")
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



""" Fin de la deuxième partie"""