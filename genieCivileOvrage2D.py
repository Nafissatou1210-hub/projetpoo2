from math import *
import math
from turtle import *
speed(50)
width(2)

"""------------------------------------------------
Commentaire de specification: FONCTION RECTANGLE
----------------------------------------------------
ENTREE: longueur,largeur, coordonnees(x,y), couleur(facultatif)
SORTIE: RECTANGLE
METHODE: boucle for
CONNU: l'angle 90°
----------------------------------------------------
cette fonction permet de creer un rectangle """
def dessinerRectangle(x,y,longueur,largeur,couleur):
    up()
    goto(x,y)
    pendown()
    fillcolor(couleur)
    begin_fill()
    for i in range(2) :
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
    end_fill()
    
"""------------------------------------------------
Commentaire de specification: FONCTION TRAPEZE
----------------------------------------------------
ENTREE:mesure(petit base et grande base respectivement pbase,gbase),mesure-cote(lcote),
        les angles(petit et grand respectivement p_angle,g_angle),les coordonnées(x,y)
SORTIE: TRAPEZE
METHODE:module turtle
CONNU:_
-------------------------------------------------------------------------------------------
cette fonction permet de dessiner le trapeze"""
def dessinerTrapeze(x,y,pbase,gbase,lcote,p_angle,g_angle,couleur):
    up()
    goto(x,y)
    down()
    fillcolor(couleur)
    begin_fill
    left(p_angle)
    forward(lcote)
    left(g_angle)
    forward(gbase)
    left(g_angle)
    forward(lcote)
    left(p_angle)
    forward(pbase)
    end_fill

"""------------------------------------------------
Commentaire de specification: FONCTION CARREE
----------------------------------------------------
ENTREE:longueur coté du carre
SORTIE: CARRE
METHODE: boucle for
CONNU:angle droit de 90°
---------------------------------------------------
cette fonction permet de dessiner un carre"""
def dessinerCarre(longueur_cote,couleur):
    fillcolor(couleur)
    begin_fill()
    cote=4
    for i in range(cote) :
            forward(longueur_cote)
            left(360/cote)
    end_fill()

"""------------------------------------------------
Commentaire de specification: FONCTION CERCLE
----------------------------------------------------
ENTREE:les coordonnées(x,y), le rayon du cercle
SORTIE: CERCLE
METHODE:module turtle
CONNU: angle 360°
--------------------------------------------------------
cette fonction permet de dessiner un cercle"""
def cercle(x,y,radius):
    up()
    goto(x,y)
    down()
    color('black')
    begin_fill()
    circle(radius, 360)
    end_fill()

"""------------------------------------------------
Commentaire de specification: FONCTION DEMI-CERCLE
----------------------------------------------------
ENTREE: les coordonnees(x,y), le rayon couleur(facultatif)
SORTIE:DEMI-CERCLE
METHODE:methode turtle et fonction cercle
CONNU: angle 180°
-----------------------------------------------------------
fonction qui permet de creer  un demi-cercle
"""
def demiCercle(x,y,radius,couleur):
    left(90)
    up()
    goto(x,y)
    pendown()
    fillcolor(couleur)
    begin_fill
    circle(radius,180)
    end_fill

"""------------------------------------------------
Commentaire de specification: FONCTION TRIANGLE
----------------------------------------------------
ENTREE: les cordonnées(x,y),les angles(angle1,angle2) longueur d'un coté du triangle(longueur) couleur
SORTIE:TRIANGLE
METHODE:module turtle et math
CONNU:
-----------------------------------------------------------------------------------------------------
cette fonction permet de dessiner un triangle"""
def triangle(x,y,angle1,angle2,longueur,couleur):
    fillcolor(couleur)
    up()
    goto(x,y)
    pendown()
    begin_fill
    forward(longueur)
    left(angle1)
    forward(longueur/math.sqrt(2))
    left(angle2)
    forward(longueur/math.sqrt(2))
    end_fill

"""------------------------------------------------
Commentaire de specification: FONCTION ELLIPESE
----------------------------------------------------
ENTREE: coordonnees(x,y), a et b
SORTIE: ELLIPSE
METHODE: boucle while
CONNU: pi et le point(0.1) et t
----------------------------------------------------
cette fonction permet de creer une ellipse """
def ellipse(x1,y1,a,b):
    pencolor("blue")
    width(5)
    reset()
    t=0
    up()
    goto(x1+a,y1)
    down()
    while t<3.14:
        xM=x1+a*cos(t)
        yM=y1+b*sin(t)
        goto(xM,yM-2)
        t=t+0.1
        