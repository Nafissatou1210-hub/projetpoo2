# from tse.tri import lesrectangles
from genieCivileOvrage2D import *

"""==================================================================================================
------------------------------------------------LES FONCTIONS-----------------------------------------
======================================================================================================"""

# cette fonction nous permet de faire les 4 fenetre carree coller en blanc
def fenetreCarre(x,y):
    up()
    goto(x,y)
    pendown()
    for i in range(4):
        begin_fill
        up()
        pendown()
        dessinerCarre(50,"white")
        left(90)    
        end_fill

# cette fonction permet de dessiner les portes en rectangle qui sont en bas des 4rectangles blanc
def porteRectangle(x,y,largeur,longueur,couleur):
    up()
    goto(x,y)
    pendown()
    fillcolor(couleur)
    begin_fill
    dessinerRectangle(x,y,largeur,longueur,couleur)
    right(90)
    dessinerRectangle(x,y,longueur,largeur,couleur)
    left(90)
    forward(largeur)
    end_fill



"""==================================================================================================
-------------------------------------------------LE PROGRAMME PRINCIPAL-------------------------------
======================================================================================================="""

# cette fonction permet de creer la facaade du batiment 

def facadeBatiment():
    dessinerRectangle(-500,-300,1020,390,"")
    dessinerRectangle(-500,-300,1020,10,"")
    dessinerTrapeze(520,90,1020,1142,70,30,150,"")
    dessinerRectangle(-340,125,200,50,"")
    dessinerRectangle(-140,125,300,50,"")
    dessinerRectangle(160,125,200,50,"")

# cette fonction permet de dessiner les fenetres du toit
def fenetre_toit():
    begin_fill
    dessinerRectangle(-310,125,10,40,"")
    dessinerRectangle(-300,125,10,40,"")

    dessinerRectangle(-250,125,10,40,"")
    dessinerRectangle(-240,125,10,40,"")

    dessinerRectangle(-190,125,10,40,"")
    dessinerRectangle(-180,125,10,40,"")

    dessinerRectangle(-120,125,10,40,"")
    dessinerRectangle(-110,125,10,40,"")

    dessinerRectangle(-76,125,10,40,"")
    dessinerRectangle(-66,125,10,40,"")

    dessinerRectangle(-40,125,10,40,"")
    dessinerRectangle(-30,125,10,40,"")

    dessinerRectangle(-0,125,10,40,"")
    dessinerRectangle(10,125,10,40,"")

    dessinerRectangle(50,125,10,40,"")
    dessinerRectangle(40,125,10,40,"")

    dessinerRectangle(75,125,10,40,"")
    dessinerRectangle(85,125,10,40,"")

    dessinerRectangle(120,125,10,40,"")
    dessinerRectangle(130,125,10,40,"")

    dessinerRectangle(190,125,10,40,"")
    dessinerRectangle(200,125,10,40,"")

    dessinerRectangle(250,125,10,40,"")
    dessinerRectangle(260,125,10,40,"")

    dessinerRectangle(300,125,10,40,"")
    dessinerRectangle(310,125,10,40,"")
    end_fill


# cette foction permet de creer le davanture de la maison avec toute les fonctions necessaires
def devantureBatimant():
    begin_fill
    dessinerRectangle(-480,-280,120,350,"gray")
    fenetreCarre(-419,10)
    porteRectangle(-470,-170,50,100,"white")
    porteRectangle(-420,-170,50,100,"white")
    dessinerRectangle(-340,-280,120,350,"gray")
    fenetreCarre(-279,10)
    porteRectangle(-330,-170,50,100,"white")
    porteRectangle(-280,-170,50,100,"white")
    dessinerRectangle(-200,-280,120,350,"gray")
    fenetreCarre(-139,10)
    porteRectangle(-190,-170,50,100,"white")
    porteRectangle(-140,-170,50,100,"white")
    dessinerRectangle(100,-280,120,350,"gray")
    fenetreCarre(161,10)
    porteRectangle(110,-170,50,100,"white")
    porteRectangle(160,-170,50,100,"white")
    dessinerRectangle(240,-280,120,350,"gray")
    fenetreCarre(301,10)
    porteRectangle(250,-170,50,100,"white")
    porteRectangle(300,-170,50,100,"white")
    dessinerRectangle(380,-280,120,350,"gray")
    fenetreCarre(441,10)
    porteRectangle(390,-170,50,100,"white")
    porteRectangle(440,-170,50,100,"white")
    end_fill

# cette fonction permet de creer la porte avec toute le fonctions neccesssaires
def portaille():
    begin_fill
    dessinerRectangle(-75,75,170,50,"white")
    dessinerRectangle(-60,-225,10,300,"")
    dessinerRectangle(-50,-225,10,300,"")
    dessinerRectangle(-40,-225,100,300,"silver")
    dessinerRectangle(60,-225,10,300,"")
    dessinerRectangle(70,-225,10,300,"")
    dessinerRectangle(-60,-235,140,10,"")
    porteRectangle(-25,-150,35,75,"white")
    porteRectangle(10,-150,35,75,"white")
    demiCercle(45,-78,35,"")
    cercle(-10,-15,17)
    porteRectangle(7,65,45,25,"white")
    end_fill

# cette fonction permet de creer les escaliers du portail
def escaliers():
    begin_fill
    dessinerRectangle(-60,-235,55,10,"")
    dessinerRectangle(70,-235,55,10,"")
    dessinerRectangle(-45,-280,10,110,"")
    dessinerRectangle(-40,-270,10,100,"")
    dessinerRectangle(-35,-260,10,90,"")
    dessinerRectangle(-30,-250,10,80,"")
    dessinerRectangle(-25,-240,10,70,"")
    dessinerRectangle(-20,-225,10,60,"")
    end_fill


def  case_toit(couleur):
    color('green')
    fillcolor(couleur)
    begin_fill
    color("green")
    left(90)
    dessinerTrapeze(160,175,300,510,120,30,150,"green")
    forward(200)
    left(148)
    forward(113)
    up()
    goto(-340,175)
    pendown()
    right(115)
    forward(110)
    end_fill

"""==================================================================================================
-------------------------------------------------APPEL DES FONCTIONS----------------------------------
======================================================================================================="""

facadeBatiment()   
fenetre_toit()
devantureBatimant()
portaille()
escaliers()
case_toit("lightgreen")



done()
    