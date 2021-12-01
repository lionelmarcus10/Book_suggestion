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
        modifier_un_lecteur()
    elif menu_profile_asked == 4:
        supprimer_un_lecteur()


elif menu == 2:
    menu_dépot_asked= ask_menu_dépot_livres()
    if menu_dépot_asked == 1:
        display_books()
    elif menu_dépot_asked == 2 :
        add_books()
    elif menu_dépot_asked == 3 :
        modify_book_title()


elif menu == 3:
    ask_recommandation_livre()


