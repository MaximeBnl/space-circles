from tkinter import *
from tkinter.messagebox import *
from constantes import *
from jeu import * 

##################################################
#                MENU PRINCIPAL                  #
##################################################

##### DEFINITION DES FONCTIONS #####

def menu_principal():
    """Mise en place de l'écran d'accueil : 
    place le fond d'écran d'accueil
    place les boutons JOUER, AIDE et QUITTER
    place le titre"""
    nettoyer()
    can.place(x=0,y=0)
    fond_etoiles = can.create_image(0,0, image=img1 ,anchor='nw')
    bouton1.place(x=boutonMenu_x, y=bouton1_y)
    bouton2.place(x=boutonMenu_x, y=bouton2_y)
    bouton3.place(x=boutonMenu_x, y=bouton3_y)
    titre.place(x=430, y=0)


def menu_aide():
    """Mise en place de l'écran d'aide"""
    nettoyer()
    aide = can.create_image(0, 0, image=img2, anchor='nw')
    bouton1.place_forget()
    bouton2.place_forget()
    bouton3.place_forget()
    boutonRetour.place(x=boutonRetour_x, y=boutonRetour_y)
    

def saisie_nom():
    """Mise en place de l'écran de saisie du nom :
    créée la zone de saisie du nom"""
    bouton1.place_forget()
    bouton2.place_forget()
    bouton3.place_forget()
    global zone_saisie
    zone_saisie = can.create_rectangle(200,150,700,450, fill='grey', outline='white')
    label_saisie.place(x=labelSaisie_x, y=labelSaisie_y)
    saisie.place(x=saisie_x, y=saisie_y)
    boutonRetour.place(x=400, y=375)
    boutonOk.place(x=boutonOk_x, y=boutonOk_y)
    

def controle_saisie() :
    """Vérifie qu'un pseudo a été entré et
    lance le jeu"""
    global pseudo
    nettoyer()
    pseudo_texte = Label(main, text=getStrFromStringVar(pseudo), font=texte_font)
    pseudo_texte['pady'] = label_pady
    pseudo_texte.place(x=600, y=0)
    ecran_jeu()

		
def nettoyer() :
    """Fonction de nettoyage :
    supprime ou oublie les éléments de l'écran
    appelle la fonction menu_principale"""
    try :
        boutonRetour.place_forget()
        can.delete(zone_saisie)
        titre.place_forget()
        boutonOk.place_forget()
        saisie.place_forget()
        label_saisie.place_forget()
        pseudo_texte.place_forget()
        
    except NameError :
        pass

    
##### FENETRE #####
main.geometry(dimensions)
main.title(titre)
main.resizable(width=False, height=False)

##### TEXTE #####
titre = Label(main, text=titre_accueil, font=texte_font)
titre['pady'] = label_pady



saisie = Entry(can, textvariable=pseudo)
saisie['bd'] = 5
saisie['width'] = 50

label_saisie = Label(main, text=texte_saisie, font=texte_font)
label_saisie['pady'] = label_pady


##### BOUTONS #####
#bouton JOUER
bouton1 = Button(can, command=saisie_nom)
bouton1['borderwidth'] = bouton_bd
bouton1['padx'] = boutonMenu_padx
bouton1['pady'] = boutonMenu_pady
bouton1['font'] = texte_font
bouton1['text'] = bouton1_text
bouton1['bg'] = bouton1_couleur

#bouton AIDE
bouton2 = Button(can, command=menu_aide)
bouton2['borderwidth'] = bouton_bd
bouton2['padx'] = boutonMenu_padx
bouton2['pady'] = boutonMenu_pady
bouton2['font'] = texte_font
bouton2['text'] = bouton2_text
bouton2['bg'] = bouton2_couleur

#bouton QUITTER
bouton3 = Button(can, command=main.destroy)
bouton3['borderwidth'] = bouton_bd
bouton3['padx'] = boutonMenu_padx
bouton3['pady'] = boutonMenu_pady
bouton3['font'] = texte_font
bouton3['text'] = bouton3_text
bouton3['bg'] = bouton3_couleur

#bouton RETOUR
boutonRetour = Button(main, command=menu_principal)
boutonRetour['padx'] = boutonRetour_padx
boutonRetour['pady'] = boutonRetour_pady
boutonRetour['font'] = texte_font
boutonRetour['text'] = boutonRetour_text

#bouton OK
boutonOk = Button(can, command=controle_saisie)
boutonOk['padx'] = boutonOk_padx
boutonOk['pady'] = boutonOk_pady
boutonOk['font'] = texte_font
boutonOk['text']=boutonOk_text

menu_principal()

main.mainloop()
