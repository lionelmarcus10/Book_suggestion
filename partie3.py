# Ce fichier contient toute les fonctions de la troisème partie.
# C'est à dire les fonctions liés a la notation de livre par un lecteur et à la suggestion de livre à un lecteur.

# Importer les différents modules necessaire

from math import sqrt

from autres_fonctions import demander_un_pseudonyme, trouver_index, verifier_livre, verifier_un_lecteur


# Fonction pour noter un livre

def noter_livre(livrenom, index_lecteur):
    index_livre = trouver_index("books.txt", livrenom)
    note = input("Attribuez une note sur 5 au livre : ")
    while (note > '5' or note < '1'):
        note = input("Attribuez une note (un entier) entre 1 et 5 au livre : ")

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

def evaluer_ses_livres(pseudo):
    index_lecteur = trouver_index('readers.txt', pseudo)
    print()

    with open('booksread.txt','r',encoding='utf-8') as livrelu3:
        livrelu2= livrelu3.readlines()[index_lecteur].split(',')[1:]
        for n in range(0,len(livrelu2)):
            livrelu2[n] = int(livrelu2[n])
    if livrelu2 ==[0]:
        print("Vous n'avez lu aucun livre par conséquent, vous ne pouvez pas noter de livre\n")
    else:

        with open('books.txt','r',encoding='utf-8') as livrelulist:
                livrelist = livrelulist.readlines()
                livrelulist2=[]
                for i in range(0,len(livrelu2)):
                    livrelulist2.append(livrelist[livrelu2[i]-1])
        print("Voici les livres que vous avez lu :\n")
        for cpt in range(0, len(livrelu2)):
            print('-',livrelulist2[cpt])


        livrenom = input("Entrez le nom du livre que vous voulez noter : ")
        y = verifier_livre(livrenom)
        y2 = False
        for x in range(0,len(livrelu2)):
            if livrenom+'\n'==livrelulist2[x]:
                y2=True

        while(y == False or y2==False):
            print("Vous n'avez pas lu ce livre, veuillez saisir un autre nom de livre\n ou un bon nom")
            livrenom = input("Entrez le nom du livre (lu) que vous voulez noter : ")
            y = verifier_livre(livrenom)
            y2 = False
            for x in range(0, len(livrelu2)):
                if livrenom + '\n' == livrelulist2[x]:
                    y2 = True

        noter_livre(livrenom, index_lecteur)

# Fonction pour Calculer la similarité entre deux lecteurs

def calcul_matrice(a, b, matrice):
    s1 = 0
    s2 = 0
    produit = 0
    for k in range(0, len(matrice[a])):
        produit = produit + matrice[a][k] * matrice[b][k]
        s1 = s1 + matrice[a][k] ** 2
        s2 = s2 + matrice[b][k] ** 2
    if s1 == 0 or s2 == 0 or produit == 0:
        return 0.0
    else:
        return round((produit / (sqrt(s1) * sqrt(s2))), 2)

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
    for i in range(0, len(matrice)):
        x = []
        for k in range(0, len(matrice)):
            if i == k:
                x.append(1.0)
            else:
                x.append(0)
        matricesimil.append(x)

    # remplir la matrice de similarité
    for h in range(0, len(matrice)):
        for j in range(0, len(matrice)):
            if h < j:
                matricesimil[h][j] = calcul_matrice(h, j, matrice)
            elif h > j:
                matricesimil[h][j] = matricesimil[j][h]
    return matricesimil


# Fonction pour suggerer un livre au lecteur

def suggerer_un_livre():
    # récuperer et verifier le nom du lecteur
    nom = demander_un_pseudonyme()
    x = verifier_un_lecteur(nom)
    while x == False:
        nom = demander_un_pseudonyme()
        x = verifier_un_lecteur(nom)

    # calculer la matrice de similarité du lecteur
    index1 = trouver_index('booksread.txt', nom)
    matricesimilarite1 = matrice_recommandation()[index1]
    # recuperer l'index de la personne ayant la plus grande similitude avec le lecteur
    maximum = 0
    index2 = 0
    for z in range(0, len(matricesimilarite1)):
        if matricesimilarite1[z] > maximum and matricesimilarite1[z] < 1:
            maximum = matricesimilarite1[z]
            index2 = z

    # recuperer les livres lu par les deux lecteurs
    with open('booksread.txt', 'r', encoding="utf-8") as booksread:
        livreslu = booksread.readlines()
    l1 = livreslu[index1].split(',')
    l1 = l1[1:]
    l2 = livreslu[index2].split(',')
    l2 = l2[1:]
    for q in range(0, len(l1)):
        l1[q] = int(l1[q])
    for s in range(0, len(l2)):
        l2[s] = int(l2[s])

    # recuperer le livre à suggerer au lecteur
    l3 = []
    for h in l2:
        if h not in l1:
            l3.append(h)

    # suggerer le livre à l'utilisateur
    with open('books.txt', 'r', encoding='utf-8') as livresdb:
        livres = livresdb.readlines()
    print("\n Les livres que nous vous recommandons de lire sont : \n")
    for i in range(0, len(l3)):
        print(i + 1, '-', livres[l3[i] - 1])

    nlivre = input("\nVoulez-vous selectioner un livre ? \n Tapez Oui ou Non : ")
    while nlivre != "Oui" and nlivre != "Non":
        nlivre = input("\nVoulez-vous selectioner un livre ? \n Tapez Oui ou Non : ")

    if nlivre == "Oui":
        for i in range(0, len(l3)):
            print(l3[i], '-', livres[l3[i] - 1])
        for j in range(0, len(l3)):
            l3[j] = str(l3[j])
        livrenumero = input("Veuillez saisir le numéro du livre que vous avez choisi : ")
        while (livrenumero not in l3):
            livrenumero = input("Veuillez saisir un numéro valide : ")
        with open('booksread.txt', 'r', encoding='utf-8') as booksread2:
            x = booksread2.readlines()
        with open('booksread.txt', 'w', encoding='utf-8') as booksread2:
            for w in range(0, len(x)):
                v = x[w].split(',')
                if v[0] == nom:
                    for cpt in range(1, len(v)):
                        v[cpt] = int(v[cpt])
                    v.append('{}\n'.format(livrenumero))
                    for cpt2 in range(1, len(v) - 1):
                        v[cpt2] = str(v[cpt2])
                    v = ','.join(v)
                    booksread2.write(v)
                else:
                    booksread2.write(x[w])
        choix_noter = input("\nVoulez-vous noter un livre ? \n Tapez Oui ou Non : ")
        while choix_noter != "Oui" and choix_noter != "Non":
            choix_noter = input("\nVoulez-vous noter un livre ? \n Tapez Oui ou Non : ")
        
        if choix_noter == "Oui":
            noter_livre(livres[int(livrenumero)-1][:-1], index1)
        

    else:
        print("N'oubliez pas de noter un de ces livres après leur lecture !")



""" Fin de la troisième partie"""