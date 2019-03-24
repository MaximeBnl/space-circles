from tkinter import *
import tkinter.font as tkFont

#############################
#       MENU PRINCIPAL      #
#############################

#FEN_MAIN
dimensions = '900x700'
titre = "SHOOT THEM'UP"
main = Tk()


#IMAGES
file1="etoiles.gif"
file2="Ecran_aide.gif"
file3="game_over.gif"
file4="ship.gif"

img1 = PhotoImage(file=file1)
img2 = PhotoImage(file=file2)
img3 = PhotoImage(file=file3)
img4 = PhotoImage(file=file4)
img1 = img1.zoom(2,2)

    
#CANVAS
can_w = 900
can_h = 700
can = Canvas(main, width=can_w, height=can_h)


#BOUTONS
#bordure des boutons
bouton_bd = 5
#position x des boutons
boutonMenu_x = 350
boutonOk_x = 600
boutonRetour_x = 600
#position y des boutons
bouton1_y = 100
bouton2_y = 300
bouton3_y = 500
boutonOk_y = 275
boutonRetour_y = 600
#dimensions des boutons
boutonMenu_padx = 85
boutonMenu_pady = 50
boutonOk_padx = 20
boutonOk_pady = 1
boutonRetour_padx = 40
boutonRetour_pady = 10
#texte des boutons
font = 'System'
boutonMenu_size = 10
bouton1_text = "  JOUER  "
bouton2_text = "    AIDE    "
bouton3_text = "QUITTER"
boutonRetour_text = "Retour"
boutonOk_text = "  OK  "
#couleur des boutons
bouton1_couleur = 'green'
bouton2_couleur = 'blue'
bouton3_couleur = 'red'


#TEXTE
texte_font = tkFont.Font(family=font, size=16)
titre_accueil = "SHOOT THEM'UP"
texte_retour = "Retour"
texte_saisie = "Entrez votre nom : "

saisie_x = 275
saisie_y = 275
labelSaisie_x = 275
labelSaisie_y = 225


#############################
#           JEU             #
#############################

#VARIABLES
touches = set()
tirs = []
temps = {}
ennemis = []
r = 25
e_move = 1
vie = 3
score = 0
pseudo = StringVar()


#AFFICHAGE
compteur_xy = 0

label_pady = 4

points_x = 50
points_y = 0

pause_x = 100
pause_y = 60
pause_relief = 'ridge'
pause_bd = 5


#BOUTONS
#couleur des boutons
boutonQuitter_couleur = 'red'
boutonRetry_couleur = 'green'
boutonScore_couleur = 'yellow'
#position x des boutons
boutonScore_x = 325
boutonRetry_x = 100
boutonQuitter_x = 550
#position y des boutons
boutonScore_y = 525
boutonRetry_y = 350
boutonQuitter_y = 350
#texte des boutons
boutonQuitter_texte = ' QUITTER '
boutonRetry_texte = 'REESSAYER'
boutonScore_texte = '  SCORE  '


#TEXTE
texte_pause = "PAUSE \n ECHAP pour reprendre \n Q pour quitter"

