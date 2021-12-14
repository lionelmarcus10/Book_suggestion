from founctions import *
#appeler le menu de lancement
menu = menu_principal()
if menu ==1:
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
    option_depot_livre= demander_option_depot_livre()
    if option_depot_livre == 1:
        display_books()
    elif option_depot_livre == 2 :
        add_books()
    elif option_depot_livre == 3 :
        modify_book_title()


elif menu == 3:
    demander_option_recommandation_livre()






