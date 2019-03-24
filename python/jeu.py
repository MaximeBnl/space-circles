from tkinter import *
from constantes import *
from time import time
from random import*

####################################################
#                       JEU                        #
####################################################

##### DEFINITION DES FONCTIONS #####

def nettoyer() :
    try :
        can.delete("all")
        ennemis.clear()
        tirs.clear()
        boutonRetry.place_forget()
        boutonQuitter.place_forget()
        boutonScore.place_forget()
        boutonRetour.place_forget()
        tabscore.place_forget()
        boutonFermer.place_forget()
        
    except NameError :
        pass

		
def ecran_jeu():
    """Mise en place de l'écran de jeu :
    création de 'ship'
    appelle la fonction 'boucle_principale()' """
    global can, ship , tirs, ecran_pause
    global temps, vie, score, g, p
    global img1

    nettoyer()
    
    fond_etoiles = can.create_image(0,0, image=img1 ,anchor='nw')
    
    #remet les variables-compteurs à zéro
    score = 0
    vie = 3
    g = False
    p = False 

    ship=can.create_image(386,572, image=img4 ,anchor='nw')
    temps={"cdProjectile" : time(),"cdRepopEnnemis" : time()}
    main.bind("<KeyPress>", enfoncer)
    main.bind("<KeyRelease>", relacher)
       
    compteur.place(x=compteur_xy, y=compteur_xy)

    life.place(x=100,y=0)
    boucle_principale()

	
def enfoncer(event):
    """Introduit le nom de la touche dans le set "touches"
    après sa pression"""
    touches.add (event.keysym)
    
	
def relacher(event):
    """Supprime le nom de la touche dans le set
    après qu'on l'ait relaché"""
    touches.remove(event.keysym)


		
def boucle_principale():
    """Noyau des mécanismes du jeu :
    définie les mouvements du joueur selon les touches sélectionnées
    définie les tirs du joueur
    définie les ennemis
    définie les limites de l'écran de jeu"""
    global can, ship, tirs, pause, ecran_pause
    global r, p,g, temps, score, e_move, vie, compteur, life 
    
    if "p" in touches :
        p = True
        ecran_pause.place(x=250, y=250)      
        
    if "Escape" in touches and p == True :
        p = False
        ecran_pause.place_forget()

    if "q" in touches and p == True :
        main.destroy()

    if p == False and g == False:
        
        if "Right" in touches :
            if can.coords(ship)[0] <= 790:
                can.move(ship,8,0)
            
        if "Left" in touches :
            if can.coords(ship)[0] >= 0:
                can.move(ship,-8,0)

        if "space" in touches :
            #création et délai entre chaque tirs
            if ms(time() - temps["cdProjectile"]) > 500 :
                temps["cdProjectile"] = time()
                calcul_centre()
                x = calcul_centre()[0]
                y = calcul_centre()[1]
                tirs.append(can.create_rectangle(x-3,y-10,x+3,y+10, fill='green'))
    
        #création et délai d'apparition des ennemis
        if ms(time() - temps["cdRepopEnnemis"]) > 900 :
            if len(ennemis) < 8 :        
                temps["cdRepopEnnemis"] = time()
                x = randint(64, (can_w-64))
                y = -r
                ennemis.append(can.create_oval(x-r, y-r, x+r, y+r, fill='red'))
                
    
        #mouvement et contrôle des ennemis 
        for e in ennemis :
            can.move(e,0,e_move)
            
            if score == 15 and e_move == 1 :
                e_move = e_move + 0.5

            if score == 25 and e_move == 1.5 :
                e_move = e_move + 0.5

            if score == 30 and e_move == 2 :
                e_move = e_move + 0.5
                
            
            if can.coords(e)[3] > can_h :
                can.delete(e)
                ennemis.remove(e)
                vie = vie - 1
                #hitbox (supprimer les éléments)
            else :   
                xe = (can.coords(e)[0]+can.coords(e)[2])/2.0
                ye = (can.coords(e)[1]+can.coords(e)[3])/2.0
                for t in tirs :
                    x1t = can.coords(t)[0]          
                    x2t = x1t + 3
                    yt = can.coords(t)[1]
                    if ((x1t-xe)**2 + (yt-ye)**2)**0.5 < r or ((x2t-xe)**2 + (yt-ye)**2)**0.5 < r :
                        ennemis.remove(e)
                        can.delete(e)
                        tirs.remove(t)
                        can.delete(t)
                        score = score + 1

                
            
        for t in tirs :
            can.move(t,0,-5)
            if can.coords(t)[1] < 0 :
                tirs.remove(t)
                can.delete(t)

        if vie == 0 :
            tab_scoreMaj()
            compteur.place_forget()
            life.place_forget()
            g = True
            game_over()

    compteur["text"] = "Score ♣ = " + str(score)      
    life["text"] = "Vie ♥ = " + str(vie)

    
    if g == False :
        main.after(12,boucle_principale)
    
	
def calcul_centre():
    """Trouve les coordonnées
    du sommet de 'ship' """
    global can, ship
    lstCoordShip = can.coords(ship)
    x = lstCoordShip[0] + 64
    y = lstCoordShip[1]
    return (x, y)

	
def ms(valeur):
    """Convertit les secondes en millisecondes"""
    return valeur *1000
  
  
def game_over():
    nettoyer()
    ecran_gameover = can.create_image(0,0, image=img3 ,anchor='nw')
    boutonScore.place(x=boutonScore_x, y=boutonScore_y)
    boutonRetry.place(x=boutonRetry_x, y=boutonRetry_y)
    boutonQuitter.place(x=boutonQuitter_x, y=boutonRetry_y)

def getStrFromStringVar(sv):
    """enleve les bug d'espaces des stringvar"""
    str=""
    for c in sv.get():
        if c!=" ":
            str+=c
    return str

def tab_scoreMaj():
    """défini les 5 meilleurs scores"""
    global pseudo, score
    bestScoreDico = read_score()
    strAEcrire = ""
    cmp = 0
    scoreEcrit=False
    for i in range(0,5):
        if  bestScoreDico[cmp][1] >= score or scoreEcrit:
            strAEcrire += (bestScoreDico[cmp][0] + " " + str(bestScoreDico[cmp][1]) + " ")
            cmp += 1
        elif not(scoreEcrit) :
            scoreEcrit=True
            strAEcrire += (getStrFromStringVar(pseudo) + " " + str(score) + " ")
    best_score = open('score.txt','w')
    best_score.write(strAEcrire)
    best_score.close()    

def tab_score() :
    """créé le tableau des scores et le rempli  avec les 5 meilleurs"""
    bestScoreDico = read_score()
    strLabel = ""
    for i in range(0,5) :
        strLabel += str(i+1) + " - " + bestScoreDico[i][0] + " : " + str(bestScoreDico[i][1]) + "\n" 
    tabscore["text"]=strLabel
    tabscore.place(x=325,y=200)
    boutonFermerTabScore.place(x=425, y=350)

def killTabScore():
    """ferme l'écran de score"""
    tabscore.place_forget()
    boutonFermerTabScore.place_forget()

def read_score():
    """lit et associe les scores et les pseudo entre eux"""
    best_score = open('score.txt','r')
    best_scoretxt = best_score.read()
    best_score.close()
    bestScoreDico = []
    if len(best_scoretxt) != 0:
        bestScoreDico.append(["",0])
        num = 0
        lectPseudoEnCours = True
        for i in range(0,len(best_scoretxt)):
            c=best_scoretxt[i]
            if c != " " and lectPseudoEnCours :         #associe les lettres du pseudo
                bestScoreDico[num][0] += c
            elif c != " " and not(lectPseudoEnCours) :  #associe les chiffres du score
                bestScoreDico[num][1] = bestScoreDico[num][1] * 10 + int(c)
            elif not(lectPseudoEnCours) and c == " " :  #délimite le score, change de paire et passe à la lecture d'un pseudo
                lectPseudoEnCours = not(lectPseudoEnCours)
                bestScoreDico.append(["",0])
                num += 1 
            elif lectPseudoEnCours and c == " ":        #délimite le pseudo et passe à la lecture d'un score
                lectPseudoEnCours = not(lectPseudoEnCours)
    for i in range(len(bestScoreDico),5):
        bestScoreDico.append(["-",0])
    return  bestScoreDico

#AUTRES :
compteur = Label(main, text="Score ♣ = " + str(score), font=texte_font)           
compteur['pady'] = label_pady
life = Label(main, text="Vie ♥ = " + str(vie), font=texte_font)
life['pady'] = label_pady

#Label Resultat
tabscore= Label(main,font=texte_font)
tabscore['padx'] = pause_x
tabscore['pady'] = pause_y
tabscore['bd'] = pause_bd
tabscore['relief'] = pause_relief
boutonFermerTabScore = Button(main, command=killTabScore)
boutonFermerTabScore['padx'] = boutonRetour_padx
boutonFermerTabScore['pady'] = boutonRetour_pady
boutonFermerTabScore['font'] = texte_font
boutonFermerTabScore['text'] = "Fermer"
#Ecran de pause
ecran_pause = Label(main, text=texte_pause, font=texte_font)
ecran_pause['padx'] = pause_x
ecran_pause['pady'] = pause_y
ecran_pause['bd'] = pause_bd
ecran_pause['relief'] = pause_relief

#Bouton "REESAYER"
boutonRetry = Button(can, command=ecran_jeu)
boutonRetry['borderwidth'] = bouton_bd
boutonRetry['padx'] = boutonMenu_padx
boutonRetry['pady'] = boutonMenu_pady
boutonRetry['font'] = texte_font
boutonRetry['text'] = boutonRetry_texte
boutonRetry['bg'] = boutonRetry_couleur

#Bouton "QUITTER"
boutonQuitter = Button(can, command=main.destroy)
boutonQuitter['borderwidth'] = bouton_bd
boutonQuitter['padx'] = boutonMenu_padx
boutonQuitter['pady'] = boutonMenu_pady
boutonQuitter['font'] = texte_font
boutonQuitter['text'] = boutonQuitter_texte
boutonQuitter['bg'] = boutonQuitter_couleur

#Bouton "SCORE"
boutonScore = Button (can, command=tab_score)
boutonScore['borderwidth'] = bouton_bd
boutonScore['padx'] = boutonMenu_padx
boutonScore['pady'] = boutonMenu_pady
boutonScore['font'] = texte_font
boutonScore['text'] = boutonScore_texte
boutonScore['bg'] = boutonScore_couleur



