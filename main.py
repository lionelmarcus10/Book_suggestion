from founctions import *
#appeler le menu de lancement
menu = ask_menu()
if menu ==1:
    menu_profile_asked = ask_menu_profil()
    if menu_profile_asked == 1:
        ajouter_un_lecteur()
    elif menu_profile_asked == 2:
        afficher_un_lecteur()
    elif menu_profile_asked == 3:
        modifier_un_utilisateur()
    elif menu_profile_asked == 4:
        supprimer_un_lecteur()

elif menu == 2:
    ask_menu_dépot_livres()
elif menu == 3:
    ask_recommandation_livre()

