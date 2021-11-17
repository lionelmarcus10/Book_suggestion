from founctions import *
#appeler le menu de lancement
menu = ask_menu()
if menu ==1:
    ask_menu_profil()
elif menu == 2:
    ask_menu_dépot_livres()
elif menu == 3:
    ask_recommandation_livre()
