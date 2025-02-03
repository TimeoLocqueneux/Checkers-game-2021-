import pygame
from copy import deepcopy
import time

screen = pygame.display.set_mode((1920,1080))
run = True
dam = pygame.image.load("damier.jpg")
N = pygame.image.load("pionN.png")
B = pygame.image.load("pionB.png")    #déclaration de toutes les variables ainsi qu'importation de bibliothèques et des images.
Nselec = pygame.image.load("pionNselec.png")
Bselec = pygame.image.load("pionBselec.png")
Ndame = pygame.image.load("pionNdame.png")
Bdame = pygame.image.load("pionBdame.png")
Nselecdame = pygame.image.load("pionNselecdame.png")
Bselecdame = pygame.image.load("pionBselecdame.png")
screen.fill((100,100,70))
screen.blit(dam,(480,60))
global H
global tab
H=0
n=0
a=0
deplacement = False
Tour = 0


""" A lire avant:
Pour bien comprendre la suite, il faut savoir que le jeu de dame est représenté, pour l'ordinateur, comme une série de 8 matrices contenant chacune 8 cases. A chacune de ses 8 cases peut être associée une valeur allant de 0 à 8, d'aucun pion à la damenoir sélectionnée. On repère grâce à pygame la position de la souris quand il y a un clic pour une certaine valeur de i et de j(calcul fait à l'avance avec des tests). Il associe après une variable qu'on appelle couleur et qui décide des mouvement possibles ou non du pion ou de la dame. L'image est rafraichie tout le temps, il n'y a donc pas d'animation des pions.

Au niveau du mouvement des pions, il faut se représenter le jeu de dame comme en ligne la valeur de yd et en colonne la valeur de xd avec xd et yd allant de 0 à 7. Par exemple, la case tout en haut à gauche est: tab[0][0]
et tout en bas à droite : tab[7][7]"""



#création du tableau représentant le jeu de dame grâce à des matrices.
tab=[]
for i in range(8):
    tab=tab+[[0,0,0,0,0,0,0,0]]

#pour voir à quoi ressemble la matrice
"""print(tab)"""

tabres=[]
for i in range(8):
    tabres=tabres+[[0,0,0,0,0,0,0,0]]

#association de valeurs à chaque case d'une matrice.
tab[2][7]=1
tab[4][7]=1
tab[6][7]=1
tab[0][7]=1
tab[2][5]=1
tab[4][5]=1
tab[6][5]=1
tab[0][5]=1
tab[1][6]=1
tab[3][6]=1
tab[5][6]=1
tab[7][6]=1


tab[1][0]=2
tab[3][0]=2
tab[5][0]=2
tab[7][0]=2
tab[1][2]=2
tab[3][2]=2
tab[5][2]=2
tab[7][2]=2
tab[2][1]=2
tab[4][1]=2
tab[6][1]=2
tab[0][1]=2


def go (P,tabA):
    p1,p2=P[0],P[1]
    x = p1[0]
    y = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    z=y-y2
    b=tabA[x][y]
    if tabA[x][y]==1 and y2==7:
        tabA[x2][y2]=6
        tabA[x][y]=0
        return()
    if tabA[x][y]==2 and y2==0:
        tabA[x2][y2]=5
        tabA[x][y]=0
        return()


    if (x2,y2)== (x+z,y+z):
        for j in range(abs(z)):
            tabA[x+j][y+j]=0

    if (x2,y2)== (x-z,y+z):
        for j in range(abs(z)):
            tabA[x-j][y+j]=0

    if (x2,y2)== (x+z,y-z):
        for j in range(abs(z)):
            tabA[x-j][y+j]=0

    if (x2,y2)== (x-z,y-z):
        for j in range(abs(z)):
            tabA[x+j][y+j]=0

    tabA[x2][y2]=b
    tabA[x][y]=0
'''trouver pour les quatres directions à quel x-z,y+z coorespond x2,y2'''





def points(tabA):
    PN = 0
    PB = 0
    for i in range(8):
        for j in range(8):
            if tabA[j][i]==1:
                PB+=1

            elif tabA[j][i]==2:
                PN+=1

            elif tabA[j][i]==5:
                PB+=7

            elif tabA[j][i]==6:
                PN+=7

    return(PN-PB)


def trouve (P,c):
    p1,p2=P[0],P[1]
    x = p1[0]
    y = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    h=y2-y
    d=x2-x








def evaB(tabA):
    compte=0
    C = []
    T=deepcopy(tabA[0])
    for i in range (8):
        for j in range (8):
            if T[i][j]==1:

                if i+2<=7 and j+2<=7 and T[i+1][j+1]==1 and T[i+2][j+2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+2,j+2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i-2<=0 and j+2<=7 and T[i-1][j+1]==1 and T[i-2][j+2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-2,j+2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i+2<=7 and j-2>=0 and T[i+1][j-1]==1 and T[i+2][j-2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+2,j-2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i-2<=0 and j-2>=0 and T[i-1][j-1]==1 and T[i-2][j-2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-2,j-2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i-1>=0 and T[i-1][j-1]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-1,j-1)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i+1<=7 and T[i+1][j-1]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+1,j-1)),Ts)
                    C = C + [[Ts,tabA[1]]]
            else:
                compte+=1

    if compte == 64 :
        return([[T,tabA[1]]])
    return (C)



def evaN0(tabA):
    C = []
    T=deepcopy(tabA)
    for i in range (8):
        for j in range (8):
            if T[i][j]==2:
                if i+2<=7 and j+2<=7 and T[i+1][j+1]==1 and T[i+2][j+2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+2,j+2)),Ts)
                    C = C + [[Ts,((i,j),(i+2,j+2))]]
                if i-2<=0 and j+2<=7 and T[i-1][j+1]==1 and T[i-2][j+2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-2,j+2)),Ts)
                    C = C + [[Ts,((i,j),(i-2,j+2))]]
                if i+2<=7 and j-2>=0 and T[i+1][j-1]==1 and T[i+2][j-2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+2,j-2)),Ts)
                    C = C + [[Ts,((i,j),(i+2,j-2))]]
                if i-2<=0 and j-2>=0 and T[i-1][j-1]==1 and T[i-2][j-2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-2,j-2)),Ts)
                    C = C + [[Ts,((i,j),(i-2,j-2))]]
                if i-1>=0 and T[i-1][j+1]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-1,j+1)),Ts)
                    C = C + [[Ts,((i,j),(i-1,j+1))]]
                if i+1<=7 and T[i+1][j+1]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+1,j+1)),Ts)
                    C = C + [[Ts,((i,j),(i+1,j+1))]]






            #if T[i][j]==6:




    return(C)   #C est la liste des nouveaux tableaux'''

















def evaN(tabA):
    compte=0
    C = []
    T=deepcopy(tabA[0])
    for i in range (8):
        for j in range (8):
            if T[i][j]==2:

                if i+2<=7 and j+2<=7 and T[i+1][j+1]==1 and T[i+2][j+2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+2,j+2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i-2<=0 and j+2<=7 and T[i-1][j+1]==1 and T[i-2][j+2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-2,j+2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i+2<=7 and j-2>=0 and T[i+1][j-1]==1 and T[i+2][j-2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+2,j-2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i-2<=0 and j-2>=0 and T[i-1][j-1]==1 and T[i-2][j-2]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-2,j-2)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i-1>=0 and j+1<=7 and T[i-1][j+1]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i-1,j+1)),Ts)
                    C = C + [[Ts,tabA[1]]]
                if i+1<=7 and j+1<=7 and T[i+1][j+1]==0 :
                    Ts = deepcopy(T)
                    go (((i,j),(i+1,j+1)),Ts)
                    C = C + [[Ts,tabA[1]]]



            #if T[i][j]==6:

            else:
                compte+=1

    if compte == 64 :
        return([[T,tabA[1]]])

    return(C)   #C est la liste des nouveaux tableaux'''

'''evaluation des coups pour chaque pion regarde si un coup est possible et le joue et rajoute le nouveau tableau dans C et reset tabA'''


















def IA (profondeur):
    tabA=deepcopy(tab)

    global L

    L = evaN0(tabA)
    if profondeur > 1 :
        for j in range (profondeur-1):
            L2 = []
            L3 = []
            for i in L :
                L2 = L2 + evaB(i)
            for h in L2 :
                L3 = L3 + evaN(h)
            L = L3
    maxpoints = points(L[0][0])
    meilleur_coup = L[0][1]

    for k in L :
        #print(k)
        #print('                   ',points(k[0]))
        if points(k[0])>=maxpoints:
            maxpoints=points(k[0])#k[0] est le tableau final correspondant au plus gros score
            meilleur_coup = k[1]#k[1] est le premier coup joué sur le premier tableau
    print(len(L))



    return(meilleur_coup)


def reload ():
    """création d'une fonction permettant de 'reload' l'image du jeu de dame.
    Cette fonction permet d'associer une image d'un pion à une valeur donnée.
    Par exemple si la case tab[3][5] vaut 1 cette case sera un pion blanc.
    Si une case vaut 0 elle ne sera pas prise en compte et il n'y aura plus de pion à cet endroit là."""
    screen.blit(dam,(480,60))
    for i in range(8):
        for j in range(8):
            if tab[i][j]==1:
                screen.blit(B,(490+i*120,70+j*120))
            if tab[i][j]==2:
                screen.blit(N,(490+i*120,70+j*120))
            if tab[i][j]==3:
                screen.blit(Nselec,(490+i*120,70+j*120))
            if tab[i][j]==4:
                screen.blit(Bselec,(490+i*120,70+j*120))
            if tab[i][j]==5:
                screen.blit(Bdame,(490+i*120,70+j*120))
            if tab[i][j]==6:
                screen.blit(Ndame,(490+i*120,70+j*120))
            if tab[i][j]==7:
                screen.blit(Nselecdame,(490+i*120,70+j*120))
            if tab[i][j]==8:
                screen.blit(Bselecdame,(490+i*120,70+j*120))
    pygame.display.flip()

def interdiction_dame():
    """création d'une fonction qui scanne à la verticale et à l'horizontal si la
    case où l'on a cliqué est dedans.
    Si elle ne détecte pas la case que l'utilisateur a cliqué, elle fait appel à la fonction 'dame()'
    Si elle est détectée dans la verticale ou l'horizontal, le déplacement est annulé."""
    global Xd
    global Yd
    global n
    xd=Xd
    yd=Yd
    xd=xd
    yd=yd-7
    while i != xd and  j!= yd and n<=14:
        if -1 > yd < 8:
            xd=xd
            yd=yd+1
            n+=1
        else:
            xd=xd
            yd=yd+1
            n+=1

    if i== xd and j ==yd:
        if couleur == Bdame:
            tab[Xd][Yd]=5
            deplacement = False
        elif couleur == Ndame:
            tab[Xd][Yd]=6
            deplacement = False

    else:
        xd=Xd
        yd=Yd
        a=0
        n=0
        xd=xd-7
        yd=yd
        while i != xd and  j!= yd and n<=14:
            if -1 > xd < 8:
                xd=xd+1
                yd=yd
                n+=1
            else:
                xd=xd+1
                yd=yd
                n+=1

        if i== xd and j ==yd:
            if couleur == Bdame:
                tab[Xd][Yd]=5
                deplacement = False
            elif couleur == Ndame:
                tab[Xd][Yd]=6
                deplacement = False
        else:
            Dame()

def Dame():
    """création d'une fonction permettant de déterminer quelle est la position
    où on souhaite faire aller la dame.
    Si la fonction détecte la position où l'on a cliqué dans une des 4 diagonales,
    celle-ci fait appel à la fonction de la diagonale en question."""
    global xd
    global yd
    global Xd
    global Yd
    a=0
    n=0
    Xd=xd
    Yd=yd
    xd=xd-1
    yd=yd+1
    while i != xd and  j!= yd and n<=7:                                           #Bas gauche
        if xd >-1 and yd < 8:
            xd=xd-1
            yd=yd+1
            n+=1
        else:
            if couleur == Bdame:
                tab[Xd][Yd] = 5
                n+=1
            elif couleur == Ndame:
                tab[Xd][Yd] = 6
                n+=1

    if i == xd and j == yd:
        Bas_gauche()
    else:
        xd=Xd
        yd=Yd
        a=0
        n=0
        xd=xd+1
        yd=yd+1
        while i != xd and  j!= yd and n<=7:                                       #Bas droite
            if xd <8 and yd < 8:
                xd=xd+1
                yd=yd+1
                n+=1
            else:
                if couleur == Bdame:
                    tab[Xd][Yd] = 5
                    n+=1
                elif couleur == Ndame:
                    tab[Xd][Yd] = 6
                    n+=1

        if i == xd and j == yd:
            Bas_droite()
        else:
            xd=Xd
            yd=Yd
            a=0
            n=0
            xd=xd+1
            yd=yd-1
            while i != xd and  j!= yd and n<=7:
                if xd<8 and yd> -1 :                                              #haut droite
                    xd=xd+1
                    yd=yd-1
                    n+=1
                else:
                    if couleur == Bdame:
                        tab[Xd][Yd] = 5
                        n+=1
                    elif couleur == Ndame:
                        tab[Xd][Yd] = 6
                        n+=1

            if i == xd and j == yd:
                Haut_droite()
            else:
                if H==0:
                    xd=Xd
                    yd=Yd
                    a=0
                    n=0
                    xd=xd-1
                    yd=yd-1
                    while i != xd and  j!= yd and n<=7:
                        if xd > -1 and yd > -1:                                   #haut gauche
                            xd=xd-1
                            yd=yd-1
                            n+=1
                        else:
                            if couleur == Bdame:
                                tab[Xd][Yd] = 5
                                n+=1
                            elif couleur == Ndame:
                                tab[Xd][Yd] = 6
                                n+=1
                if i == xd and j == yd:
                    Haut_gauche()

#à noter que toutes ces fonction là sont seulement pour la dame
def Bas_gauche():
    #si la position de la dame est dans la diagonale en bas à gauche
    global Xd
    global Yd
    H=1
    a=0
    n=0
    xd=Xd
    yd=Yd
    xd=xd-1
    yd=yd+1
    #utilisation du while jsuqu'à tant qu'il soit arrivé à la valeur de la position où l'utilisateur a cliqué
    while i != xd and  j!= yd and a<2:

        #si la dame en question est une dame Blanche
        if couleur == Bdame:
                                                              #Bas gauche
            #si la case d'après est une case vide
            if tab[xd][yd]==0:
                xd=xd-1
                yd=yd+1

            #si la case d'après est un pion noir ou une dame noire
            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                #si il y a n'importe quel pion après ce pion la valeur de a devient 2 et le while s'arrête(chemin_1)
                if tab[xd-1][yd+1]==2 or tab[xd-1][yd+1]==5 or tab[xd-1][yd+1]==1 or tab[xd-1][yd+1]==6:
                    a=2

                #si il n'y a rien après le pion noir, celui-ci diparait
                else:
                    tab[xd][yd]=0
                    xd=xd-1
                    yd=yd+1

            #si la case d'après est un pion de la même couleur c'est à dire un pion blanc ou une dame blanche le while s'arrête(chemin_1)
            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                a=2

            """Si la dame est noire, c'est la même chose que juste avant ce sont juste les valeurs des cases qui changent"""
        #si la dame en question est noire
        elif couleur == Ndame:

            #si la case d'après est une case vide
            if tab[xd][yd]==0:
                print(xd)
                print(yd)
                xd=xd-1
                yd=yd+1

            #si la case d'après est un pion blanc ou une dame blanche
            elif tab[xd][yd]==1 or tab[xd][yd]==5:

                #si il y a n'importe quel pion après ce pion la valeur de a devient 2 et le while s'arrête(chemin_1)
                if tab[xd-1][yd+1]==2 or tab[xd-1][yd+1]==5 or tab[xd-1][yd+1]==1 or tab[xd-1][yd+1]==6:
                    a=2

                #si il n'y a rien après le pion blanc, celui-ci diparait
                else:
                    tab[xd][yd]=0
                    xd=xd-1
                    yd=yd+1

            #si la case d'après est un pion de la même couleur c'est à dire un pion blanc ou une dame blanche le while s'arrête(chemin_1)
            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                a=2


    if a ==2:
        #(chemin_1) la case où était la dame redevient une dame
        if couleur == Bdame:
            tab[Xd][Yd]=5
            deplacement= False
        elif couleur == Ndame:
            tab[Xd][Yd]=6
            deplacement= False


    elif i== xd and j ==yd:
        #si on est arrivé à la bonne position à la case apparait la dame et la case où était la dame avant prend la valeur de 0, elle disparait
        if couleur == Bdame:
            tab[i][j]=5
            tab[Xd][Yd]=0
            deplacement = False
        elif couleur == Ndame:
            tab[i][j]=6
            tab[Xd][Yd]=0
            deplacement = False

def Bas_droite():
    """pour voir les explication se rendre à la fonction bas_gauche"""
    global Xd
    global Yd
    H=1
    a=0
    n=0
    xd=Xd
    yd=Yd
    xd=xd+1
    yd=yd+1
    while i != xd and  j!= yd and a<2:
        if couleur == Bdame:
            if tab[xd][yd]==0:
                xd=xd+1
                yd=yd+1

            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                if tab[xd+1][yd+1]==2 or tab[xd+1][yd+1]==5 or tab[xd+1][yd+1]==1 or tab[xd+1][yd+1]==6:
                    a=2

                else:
                    tab[xd][yd]=0
                    xd=xd+1
                    yd=yd+1


            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                a=2
        elif couleur == Ndame:
            if tab[xd][yd]==0:
                xd=xd+1
                yd=yd+1

            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                if tab[xd+1][yd+1]==2 or tab[xd+1][yd+1]==5 or tab[xd+1][yd+1]==1 or tab[xd+1][yd+1]==6:
                    a=2

                else:
                    tab[xd][yd]=0
                    xd=xd+1
                    yd=yd+1

            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                a=2


    if a ==2:
        if couleur == Bdame:
            tab[Xd][Yd]=5
            deplacement= False
        elif couleur == Ndame:
            tab[Xd][Yd]=6
            deplacement= False


    elif i== xd and j ==yd:
        if couleur == Bdame:
            tab[i][j]=5
            tab[Xd][Yd]=0
            deplacement = False
        elif couleur == Ndame:
            tab[i][j]=6
            tab[Xd][Yd]=0
            deplacement = False


def Haut_gauche():
    """pour voir les explication se rendre à la fonction bas_gauche"""
    global Xd
    global Yd
    a=0
    n=0
    xd=Xd
    yd=Yd
    xd=xd-1
    yd=yd-1
    while i != xd and  j!= yd and a<2:
        if couleur == Bdame:                                           #Bas gauche
            if tab[xd][yd]==0:
                xd=xd-1
                yd=yd-1



            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                if tab[xd-1][yd-1]==2 or tab[xd-1][yd-1]==5 or tab[xd-1][yd-1]==1 or tab[xd-1][yd-1]==6:
                    a=2

                else:
                    tab[xd][yd]=0
                    xd=xd-1
                    yd=yd-1



            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                a=2
        if couleur == Ndame:
            if tab[xd][yd]==0:
                xd=xd-1
                yd=yd-1

            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                if tab[xd-1][yd-1]==2 or tab[xd-1][yd-1]==5 or tab[xd-1][yd-1]==1 or tab[xd-1][yd-1]==6:
                    a=2

                else:
                    tab[xd][yd]=0
                    xd=xd-1
                    yd=yd-1

            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                a=2


    if a ==2:
        if couleur == Bdame:
            tab[Xd][Yd]=5
            deplacement= False
        elif couleur == Ndame:
            tab[Xd][Yd]=6
            deplacement= False


    elif i== xd and j ==yd:
        if couleur == Bdame:
            tab[i][j]=5
            tab[Xd][Yd]=0
            deplacement = False
        elif couleur == Ndame:
            tab[i][j]=6
            tab[Xd][Yd]=0
            deplacement = False

def Haut_droite():
    """pour voir les explication se rendre à la fonction bas_gauche"""
    global Xd
    global Yd
    H=1
    a=0
    n=0
    xd=Xd
    yd=Yd
    xd=xd+1
    yd=yd-1
    print(tab[5][2])
    while i != xd and  j!= yd and a<2:
        if couleur == Bdame:
            if tab[xd][yd]==0:
                xd=xd+1
                yd=yd-1


            elif tab[xd][yd]==2 or tab[xd][yd]==6:

                if tab[xd+1][yd-1]==2 or tab[xd+1][yd-1]==5 or tab[xd+1][yd-1]==1 or tab[xd+1][yd-1]==6:
                    a=2


                else:
                    tab[xd][yd]=0
                    xd=xd+1
                    yd=yd-1

            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                a=2

        elif couleur == Ndame:
            if tab[xd][yd]==0:
                xd=xd+1
                yd=yd-1



            elif tab[xd][yd]==1 or tab[xd][yd]==5:
                if tab[xd+1][yd-1]==2 or tab[xd+1][yd-1]==5 or tab[xd+1][yd-1]==1 or tab[xd+1][yd-1]==6:
                    a=2

                else:
                    tab[xd][yd]=0
                    xd=xd+1
                    yd=yd-1

            elif tab[xd][yd]==2 or tab[xd][yd]==6:
                a=2


    if a ==2:
        if couleur == Bdame:
            tab[Xd][Yd]=5
            deplacement = False

        elif couleur == Ndame:
            tab[Xd][Yd]=6
            deplacement= False

    elif i== xd and j ==yd:
        if couleur == Bdame:
            tab[i][j]=5
            tab[Xd][Yd]=0
            deplacement = False
        elif couleur == Ndame:
            tab[i][j]=6
            tab[Xd][Yd]=0
            deplacement = False


go(((1,2),(0,3)),tab)
while run :


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h :
                print(tab)
        if event.type == pygame.MOUSEBUTTONDOWN:




            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x,y = pos[0],pos[1]
                for i in range (8):
                    for j in range (8):
                        if x>480+i*120 and x<480+(i+1)*120 :
                            if y>60+j*120 and y<60+(j+1)*120 :
                                if tab[i][j]!=0:
                                    """Si la case vaut 1, cele-ci est considérée comme un pion blanc, 2 comme un pion noir etc.
                                    une fois qu'on a déterminé la couleur du pion, on remplace le pion par son image 'select' associée( voir début du programme et image dans le fichier) pour le mettre en surbrillance."""
                                    if Tour%2==0:

                                        if tab[i][j]==1:
                                            couleur=B
                                            tab[i][j]=4
                                            #On active le déplacement
                                            deplacement=True
                                            xd = i
                                            yd = j
                                            Xd = i
                                            Yd = j
                                            Tour+=1
                                        elif tab[i][j]==2:
                                            Tour+=0
                                        elif tab[i][j]==5:
                                            couleur=Bdame
                                            tab[i][j]=8
                                            #On active le déplacement
                                            deplacement=True
                                            xd = i
                                            yd = j
                                            Xd = i
                                            Yd = j
                                            Tour+=1
                                        elif tab[i][j]==6:
                                            Tour+=0


                                    else:
                                        if tab[i][j]==1:
                                            Tour+=0
                                        elif tab[i][j]==2:
                                            couleur=N
                                            tab[i][j]=3
                                            #On active le déplacement
                                            deplacement=True
                                            xd = i
                                            yd = j
                                            Xd = i
                                            Yd = j
                                            Tour+=1
                                        elif tab[i][j]==5:
                                            Tour+=0
                                        elif tab[i][j]==6:
                                            couleur=Ndame
                                            tab[i][j]=7
                                            #On active le déplacement
                                            deplacement=True
                                            xd = i
                                            yd = j
                                            Xd = i
                                            Yd = j
                                            Tour+=1
                                    print(Tour)




        if event.type == pygame.KEYDOWN :
            #Si la touche c est appuyée durant la partie, la fenêtre se ferme.
            if event.key == pygame.K_c :
                run = False
            #Si la touche r est appuyée durant la partie, le jeu se réinitialise pour lancer une nouvelle partie.
            if event.key == pygame.K_r :
                tabres[2][7]=1
                tabres[4][7]=1
                tabres[6][7]=1
                tabres[0][7]=1
                tabres[2][5]=1
                tabres[4][5]=1
                tabres[6][5]=1
                tabres[0][5]=1
                tabres[1][6]=1
                tabres[3][6]=1
                tabres[5][6]=1
                tabres[7][6]=1
                tabres[0][3]=0
                tabres[2][3]=0
                tabres[4][3]=0
                tabres[6][3]=0
                tabres[1][4]=0
                tabres[3][4]=0
                tabres[5][4]=0
                tabres[7][4]=0
                tabres[1][0]=2
                tabres[3][0]=2
                tabres[5][0]=2
                tabres[7][0]=2
                tabres[1][2]=2
                tabres[3][2]=2
                tabres[5][2]=2
                tabres[7][2]=2
                tabres[2][1]=2
                tabres[4][1]=2
                tabres[6][1]=2
                tabres[0][1]=2
                tab = tabres
                Tour=0
            if event.key == pygame.K_i :
                go(IA(1),tab)
            if event.key == pygame.K_m :
                go(((int(input('x')),int(input('y'))),(int(input('x2')),int(input('y2')))),tab)


    while deplacement :
        #On a ici le deuxième clic de la souris pour savoir où le pion va.
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x,y = pos[0],pos[1]
                for i in range (8):
                    for j in range (8):
                        if x>480+i*120 and x<480+(i+1)*120 and y>60+j*120 and y<60+(j+1)*120 :

                            if couleur == B:
                             #si le pion est de couleur blanche                                                #PION BLANC
                                if tab[i][j]==0:
                        #on réalise ici le cas où le pion blanc est à la dernière ligne et va donc se tranformer en dame
                                    if j == 0:
                                        if i==xd+1 and j==yd-1 :
                                            tab[xd][yd]=0
                                            tab[i][j]=5


                                        elif i==xd+2 and j==yd-2 :
                                            if tab[xd+1][yd-1] ==2 or tab[xd+1][yd-1]==6:
                                                tab[xd+1][yd-1]=0
                                                tab[xd][yd]=0
                                                tab[i][j]=5



                                        elif i==xd-1 and j==yd-1 :

                                            if tab[i][j]==0:
                                                tab[xd][yd]=0
                                                tab[i][j]=5




                                        elif i==xd-2 and j==yd-2 :
                                            if tab[xd-1][yd-1]==2 or tab[xd-1][yd-1] ==6:
                                                tab[xd-1][yd-1]=0
                                                tab[xd][yd]=0
                                                tab[i][j]=5


                                        else:
                                            tab[xd][yd]=1
                                            Tour+=1
                                            deplacement = False


                                    #si le déplacement est de 1 case
                                    elif i==xd+1 and j==yd-1 :
                                        tab[xd][yd]=0
                                        tab[i][j]=1


                                #Si le déplacement est de 2 cases et qu'il y a une dame noire ou un pion noire entre les deux
                                    elif i==xd+2 and j==yd-2 :
                                        if tab[xd+1][yd-1] ==2 or tab[xd+1][yd-1] ==6:
                                            tab[xd+1][yd-1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=1


                                    #Si le déplacement et de 1 case
                                    elif i==xd-1 and j==yd-1 :

                                        if tab[i][j]==0:
                                            tab[xd][yd]=0
                                            tab[i][j]=1



                                #Si le déplacement est de 2 cases et qu'il y a une dame noire ou un pion noire entre les deux
                                    elif i==xd-2 and j==yd-2 :
                                        if tab[xd-1][yd-1]==2 or tab[xd-1][yd-1] ==6:
                                            tab[xd-1][yd-1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=1

                                #Si le déplacement est de 2 cases mais en arrière et qu'il y a une dame noire ou un pion noire entre les deux
                                    elif i == xd+2 and j == yd+2:
                                        if tab[xd+1][yd+1]==2 or tab[xd+1][yd+1] ==6:
                                            tab[xd+1][yd+1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=1

                                    #Si le déplacement est de 2 cases en arrière et qu'il y a une dame noire ou un pion noire entre les deux
                                    elif i == xd-2 and j == yd+2:
                                        if tab[xd-1][yd+1]==2 or tab[xd-1][yd+1] ==6:
                                            tab[xd-1][yd+1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=1

                                    else:
                                        tab[xd][yd]=1
                                        Tour+=1
                                        deplacement = False

                                else:
                                    tab[xd][yd]=1
                                    Tour+=1
                                    deplacement = False




                            #C'est la même chose qu'avec les blancs mais avec des valeurs différentes.
                            elif couleur == N:                                        #PION NOIR
                                if tab[i][j]==0:
                                    if j == 7:
                                        if i==xd+1 and j==yd+1 :
                                            tab[xd][yd]=0
                                            tab[i][j]=6


                                        elif i==xd+2 and j==yd+2 :
                                            if tab[xd+1][yd+1] ==1 or tab[xd+1][yd+1] ==5:
                                                tab[xd+1][yd+1]=0
                                                tab[xd][yd]=0
                                                tab[i][j]=6



                                        elif i==xd-1 and j==yd+1 :

                                            if tab[i][j]==0:
                                                tab[xd][yd]=0
                                                tab[i][j]=6


                                        elif tab[i][j]==0:
                                            if i==xd-2 and j==yd+2 :
                                                if tab[xd-1][yd+1] ==1 or tab[xd-1][yd+1] ==5:
                                                    tab[xd-1][yd+1]=0
                                                    tab[xd][yd]=0
                                                    tab[i][j]=6


                                        else:
                                            tab[xd][yd]=2
                                            Tour+=1
                                            deplacement = False


                                    elif i==xd+1 and j==yd+1 :
                                        tab[xd][yd]=0
                                        tab[i][j]=2


                                    elif i==xd-1 and j==yd+1 :
                                        if tab[i][j]==0:
                                            tab[xd][yd]=0
                                            tab[i][j]=2


                                    elif i==xd+2 and j==yd+2 :
                                        if tab[xd+1][yd+1]==1 or tab[xd+1][yd+1] ==5:
                                            tab[xd+1][yd+1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=2


                                    elif i==xd-2 and j==yd+2 :
                                        if tab[xd-1][yd+1]==1 or tab[xd-1][yd+1] ==5:
                                            tab[xd-1][yd+1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=2

                                    elif i==xd-2 and j==yd-2 :
                                        if tab[xd-1][yd-1]==1 or tab[xd-1][yd-1] ==5:
                                            tab[xd-1][yd-1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=2


                                    elif i==xd+2 and j==yd-2:
                                        if tab[xd+1][yd-1]==1 or tab[xd+1][yd-1] ==5:
                                            tab[xd+1][yd-1]=0
                                            tab[xd][yd]=0
                                            tab[i][j]=2

                                    else:
                                        tab[xd][yd]=2
                                        Tour+=1
                                        deplacement = False


                                else:
                                    tab[xd][yd]=2
                                    Tour+=1
                                    deplacement = False


                            #Si c'est un dame blanche, on fait appel à la fonction interdiction_dame()
                            elif couleur == Bdame:                                #Dame BLANCHE
                                if tab[i][j]==0:
                                    interdiction_dame()


                                else:
                                    tab[Xd][Yd]=5
                                    Tour+=1
                                    deplacement = False


                            #Si c'est une dame noire, on fait appel à la fonction interdiction_dame()
                            elif couleur == Ndame:
                                if tab[i][j]==0:
                                    interdiction_dame()


                                else:
                                    tab[xd][yd]=6
                                    Tour+=1
                                    deplacement = False


                            deplacement = False

                            #evaluation_blanc()


            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_c :
                    deplacement  = False


        reload()

    reload()


pygame.quit()
