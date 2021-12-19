"""Une fonction qui donne le menu qui proposer par ce programme """

from autres_fonctions import afficher_un_livre, demander_option_depot_livre, demander_option_profile, demander_un_pseudonyme, demander_option_recommandation_livre, verifier_un_lecteur
from partie1 import afficher_un_lecteur, ajouter_un_lecteur, modifier_un_lecteur, supprimer_un_lecteur
from partie2 import ajouter_un_livre, modifier_un_livre, supprimer_un_livre
from partie3 import evaluer_ses_livres, suggerer_un_livre

# Fonction qui affiche le menu principal
def menu_principal():
    print("Tapez le numéro qui vous correspond : ")
    print("1 - Profils des lecteurs")
    print("2 - Visiter le dépôt des livres")
    print("3 - Recommandation")
    choix = (input("Saisir le numéro : "))
    while ( choix !='1' and choix !='3' and choix!= '2'):
        choix = (input("Saissez à nouveau le numéro : "))
    return int(choix)


# fonction pour le menu de lancement
def menu_de_lancement():
    x = None
    demande_chaine = "Saisir M pour continuer sur le menu principal ou Q pour quitter :  "
    while (x != 'Q'):
        x = input(demande_chaine)
        while (x != 'M' and x != 'Q'):
            x = input("Veuillez entrer 'M' ou 'Q'. " + demande_chaine)
        
        if (x == 'M'):
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
                    pseudo = demander_un_pseudonyme()
                    while verifier_un_lecteur(pseudo) == False:
                        pseudo = demander_un_pseudonyme()

                    evaluer_ses_livres(pseudo)
                elif option_recommandation == 2:
                    suggerer_un_livre()

