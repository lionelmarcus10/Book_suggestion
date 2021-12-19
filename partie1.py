# Ce fichier contient toute les fonctions de la première partie.
# C'est à dire les fonctions liés au profil d'un lecteur.

# Importer les différents modules necessaire

from autres_fonctions import demander_livre_lu, demander_un_pseudonyme, modifier_livre_lu, pas_entier, trouver_index, verifier_un_lecteur
from listes import liste_style_de_lecture,liste_genre,liste_age
from partie3 import evaluer_ses_livres
import time

# Une fonction qui demande le sexe du lecteur

def demander_genre():
    print("Quel est votre genre ? ","\n","Tapez le numéro qui vous correspondent : ")
    print("1 - HOMME ")
    print("2 - FEMME ")
    print("3 - PEU IMPORTE ")
    genre=(input("Saisir un numéro : "))
    while (genre != '1' and genre != '2' and genre != '3' ) :
        print("Quel est votre genre ? ", "\n", "Tapez le numéro qui vous correspondent : ")
        print("1 - HOMME ")
        print("2 - FEMME ")
        print("3 - PEU IMPORTE ")
        genre = (input("Saisir un numéro : "))
    return genre



# Une fonction qui demande  l'âge du lecteur

def demander_age():
    print("Quel est votre âge ? ","\n"," Tapez le numéro 1 ou 2 ou 3 pour saisir votre âge ")
    print("1 - <= 18 ans")
    print("2 - Entre 18 ans et 25 ans")
    print('3 - > 25 ans ')
    age = (input("Saisir un numéro : "))
    while (age != '1' and age != '2' and age != '3' ) :
        print(" Quel est votre genre ? ", "\n", "Tapez le numéro qui vous correspond")
        print("1 - <= 18 ans")
        print("2 - Entre 18 ans et 25 ans")
        print('3 - > 25 ans ')
        age = (input("Saisir un numéro : "))
    return age



# Une fonction qui permet de savoir le style de lecture du lecteur

def demander_style_de_lecture():
    print("Quel est votre style de lecture ? ","\n","Tapez le numéro qui vous correspond")

    for k in range(0,len(liste_style_de_lecture)):
        print(k+ 1,' - ',liste_style_de_lecture[k])
    style = input("Saisir le numéro corrospondant à votre style de lecture : ")
    while ( style < '1' or style > '7' or style != str(style)):
        style =input("Saisir le numéro corrospondant à votre style de lecture : ")

    return str(style)




# Une fonction qui ajoute un lecteur

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
    h = input("Voulez-vous noter un livre ? Tapez Oui ou Non :  ")
    while(h!='Oui' and h !='Non'):
        h = input("Voulez-vous noter un livre ?\n Tapez Oui ou Non :  ")
    if h == 'Oui':
        evaluer_ses_livres(nompseudo)


# Une fonction qui supprime un lecteur
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
                 print('lecteur {} supprimé'.format(nomsup))
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




# la fonction afficher_un_lecteur peut afficher le profil d’un lecteur donné

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

         if len(lecteur)>1 and lecteur[1]!='\n':
             for z in range(1, len(lecteur)):
                    lecteur[z]=int(lecteur[z])

         if aflecteur == lecteur[0]:
             livreslu = lecteur[1:]

             with open("books.txt","r",encoding='utf-8') as books_db:
                 livres1= books_db.readlines()
                 if livreslu == [0] :
                     print("{} n'a lu auccun livre".format(aflecteur))
                 else:
                     print("{} a lu : ".format(aflecteur),"\n")
                     for i in livreslu:

                         print("-",livres1[i-1])



# la fonction modifier_un_lecteur peut modifier les informations du profil d’un lecteur donné."""

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
            npseudomod = input('Entrez votre nouveau pseudonyme : ')
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
                        x = input('Entrez une nouvelle fois votre pseudo : ')
                        y = verifier_un_lecteur(x)
                        if y == False:
                            print("Le pseudonyme saisi est incorrecte la modification n'a pas pu etre réalisée.")
                        else:
                            modifier_livre_lu(x)


""""Fin de la 1ère partie"""