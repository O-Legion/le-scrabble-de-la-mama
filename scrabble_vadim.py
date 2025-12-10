#!/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
i11_XXXX_YYYY_projet.py : CR projet « srabble », groupe ZZZ

XXXX <vadim.hackert@etu-univ-grenoble-alpes.fr>
YYYY <bruno.ngoma@univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""

# IMPORTS ######################################################################

from pathlib import Path  # gestion fichiers
import random  # simuler l'aléatoire

# CONSTANTES ###################################################################

TAILLE_PLATEAU = 15  # taille du plateau de jeu

TAILLE_MARGE = 4  # taille marge gauche (qui contient les numéros de ligne)

JOKER = '?'  # jeton joker

# /!\ pas de variables globales, sauf cas exceptionnel


# PARTIE 1 : LE PLATEAU ########################################################

def symetrise_liste(lst) :
    """
    Auxilliaire pour Q1 : symétrise en place la liste lst.
    EB : modification de lst.

    >>> essai = [1,2] ; symetrise_liste(essai) ; essai
    [1, 2, 1]
    >>> essai = [1,2,3] ; symetrise_liste(essai) ; essai
    [1, 2, 3, 2, 1]
    """
    copie_lst = list(lst)
    for i in range(2, len(copie_lst)+1): lst.append(copie_lst[-i])


def init_bonus() :
    """
    Q1) Initialise le plateau des bonus.
    """
    # Compte-tenu  de  la  double   symétrie  axiale  du  plateau,  on
    # a  7  demi-lignes  dans  le  quart  supérieur  gauche,  puis  la
    # (demi-)ligne centrale,  et finalement  le centre. Tout  le reste
    # s'en déduit par symétrie.
    plt_bonus = [  # quart-supérieur gauche + ligne et colonne centrales
        ['MT', ''  , ''  , 'LD', ''  , ''  , ''  , 'MT'],
        [''  , 'MD', ''  , ''  , ''  , 'LT', ''  , ''],
        [''  , ''  , 'MD', ''  , ''  , ''  , 'LD', ''],
        ['LD', ''  , ''  , 'MD', ''  , ''  , ''  , 'LD'],
        [''  , ''  , ''  , ''  , 'MD', ''  , ''  , ''],
        [''  , 'LT', ''  , ''  , ''  , 'LT', ''  , ''],
        [''  , ''  , 'LD', ''  , ''  , ''  , 'LD', ''],
        ['MT', ''  , ''  , 'LD', ''  , ''  , ''  , 'MD']
    ]
    # On transforme les demi-lignes du plateau en lignes :
    for ligne in plt_bonus: symetrise_liste(ligne)
    # On transforme le demi-plateau en plateau :
    symetrise_liste(plt_bonus)

    return plt_bonus


def init_jetons():
    j = []
    for z in range(TAILLE_PLATEAU):
        ligne = []
        for x in range(TAILLE_PLATEAU):
            ligne.append('')
        j.append(ligne)
    return j

    # ecrit sous la forme d'une compréhension de liste
    # return [['' for x in range(TAILLE_PLATEAU)] for z in range(TAILLE_PLATEAU)]


def init_pioche_alea():
    # On s'assure que chaque lettre est presente au moins une fois
    # et que deux jokers sont bien dans la liste.
    li = [chr(ord("A")+i) for i in range(26)] + [JOKER, JOKER]
    for i in range(100-len(li)):
        # Puis, on complete avec des lettres choisies au hasard jusqu'a 100 elements.
        lettre = chr(random.randint(ord('A'), ord('Z')))
        li.append(lettre)
    return li


def affiche_jetons(j, bonus_plateau=None):
    if bonus_plateau is None:
        bonus = init_bonus()
    else:
        bonus = bonus_plateau

    marge = " " * TAILLE_MARGE
    nb_chiffres_max = len(str(TAILLE_PLATEAU))

    dic_affichage_bonus = {
                            'LD': '°',
                            'LT': '^',
                            'MD': '²',
                            'MT': '*',
                          }


    print(marge, end= " " * nb_chiffres_max + "  ")
    # On numerote les colonnes.
    for x in range(1, TAILLE_PLATEAU):
        nb_chiffres = len(str(x))
        print("0" * (nb_chiffres_max - nb_chiffres) + str(x), end="  ")

    # On numerote la derniere colonne et on revient a la ligne.
    print(str(TAILLE_PLATEAU))


    print(marge, end= " " * nb_chiffres_max + " ")
    print("|---" * (TAILLE_PLATEAU-1) + "|---|")

    indice_ligne = 0
    for z in range(2*TAILLE_PLATEAU):
        # Une iteration sur deux, on numerote la ligne et on affiche le jeton pour chaque case.
        if z % 2 == 0:
            nb_chiffres = len(str(indice_ligne+1))
            print(marge + "0"*(nb_chiffres_max - nb_chiffres) + str(indice_ligne+1), end=" ")

            for x in range(TAILLE_PLATEAU-1):
                jeton = j[indice_ligne][x]
                bonus = bonus_plateau[indice_ligne][x]
                if jeton == "":
                    affichage_case = " "
                    if bonus in dic_affichage_bonus:
                        affichage_case = dic_affichage_bonus[bonus]
                else:
                    affichage_case = jeton
                    if bonus in dic_affichage_bonus:
                        affichage_case += "*"
                print("| " + affichage_case, end=" ")

            jeton = j[indice_ligne][TAILLE_PLATEAU-1]
            bonus = bonus_plateau[indice_ligne][TAILLE_PLATEAU-1]
            if jeton == "":
                affichage_case = " "
                if bonus in dic_affichage_bonus:
                    affichage_case = dic_affichage_bonus[bonus]
            else:
                affichage_case = jeton
                if bonus in dic_affichage_bonus:
                    affichage_case += "*"
            print("| " + affichage_case + " |")

            indice_ligne += 1
        else:
            print(marge, end= " " * nb_chiffres_max + " ")
            print("|---" * (TAILLE_PLATEAU-1) + "|---|")

def plateau():  # Question 5
    j = init_jetons()
    return j


def piocher(x, sac):
    """
    Q8)
    """
    jetons = []
    for i in range(x):
        j = random.randint(0, len(sac)-1)
        jetons.append(sac[j])
        sac.pop(j)  # On retire le jeton du sac afin qu'il ne puisse plus etre tire a nouveau
    return jetons


def completer_main(main, sac):
    """
    Q9)
    """
    cm = 7-len(main)  # Nombre de jetons manquants
    if len(sac) < cm:
        cm = len(sac)
    main.extend(piocher(cm, sac))


def echanger(jetons, main, sac):
    """
    Q10)
    """
    l = []
    for jeton in jetons:
        if jeton in main:
            l.append(jeton)
            main.remove(jeton)

    completer_main(main, sac)
    sac.extend(l)

    return not len(main)<7


def partie_test():
    nom_j1 = input("Nom du joueur 1 : ")
    nom_j2 = input("Nom du joueur 2 : ")
    
    table_jetons = init_jetons()
    table_bonus = init_bonus()
    affiche_jetons(table_jetons, table_bonus)
    sac = init_pioche_alea()

    main_j1 = piocher(7, sac)
    main_j2 = piocher(7, sac)
    print("Sac :\n", sac)

    print("Main de", nom_j1, ":\n", main_j1)
    echanger_j1 = input(nom_j1 + ", souhaitez-vous echanger vos jetons ? (O/N) ")
    while echanger_j1 != "O" and echanger_j1 != "N":
        echanger_j1 = input(nom_j1 + ", souhaitez-vous echanger vos jetons ? (O/N) ")

    if echanger_j1 == "O":
        jetons_echange = []
        jeton = input("Echanger jeton : ")
        jetons_echange.append(jeton)
        i = 0
        while jeton != "!" and i<7:
            jeton = input("Echanger jeton : ")
            jetons_echange.append(jeton)
            i = i + 1
        echanger(jetons_echange, main_j1, sac)
        print("Main de", nom_j1, ":\n", main_j1)
        print("Sac :\n", sac)


    # meme approche pour le joueur 2
    print("Main de", nom_j2, ":\n", main_j2)
    echanger_j2 = input(nom_j2 + ", souhaitez-vous echanger vos jetons ? (O/N) ")
    while echanger_j2 != "O" and echanger_j2 != "N":
        echanger_j2 = input(nom_j2 + ", souhaitez-vous echanger vos jetons ? (O/N) ")

    if echanger_j2 == "O":
        jetons_echange = []
        jeton = input("Echanger jeton : ")
        jetons_echange.append(jeton)
        i = 0
        while jeton != "!" and i<7:
            jeton = input("Echanger jeton : ")
            jetons_echange.append(jeton)
            i = i + 1
        echanger(jetons_echange, main_j2, sac)
        print("Main de", nom_j2, ":\n", main_j2)
        print("Sac :\n", sac)


# PARTIE 3 : CONSTRUCTIONS DE MOTS #############################################

def generer_dictfr(nf='littre.txt') :
    """Liste des mots Français en majuscules sans accent.

    >>> len(generer_dictfr())
    73085
    """
    mots = []
    with Path(nf).open(encoding='utf_8') as fich_mots :
        for line in fich_mots : mots.append(line.strip().upper())
    return mots

mots_fr = generer_dictfr()


def select_mot_initiale(motsfr, let):
    l = []
    for mot in motsfr:
        if mot[0] == let:
            l.append(mot)
    return l


def select_mot_longueur(motsfr, lgr):
    l = []
    for mot in motsfr:
        if len(mot) == lgr:
            l.append(mot)
    return l


def mot_jouable(mot, ll, n_let):
    ll_copie = list(ll)
    jouable = True
    c = 0
    i = 0
    while jouable and i < len(mot):
        if mot[i] in ll_copie:
            ll_copie.remove(mot[i])
        elif JOKER in ll_copie:
            ll_copie.remove(JOKER)
        elif c < n_let:
            c = c + 1
        else:
            jouable = False
        i = i + 1
    return jouable


def mots_jouables(motsfr, ll, n_let=0): 
    l = []
    for mot in motsfr:
        if mot_jouable(mot, ll, n_let):
            l.append(mot)
    return l
def mot_jouable2(mot,main): # Question 15 et 17 et 18
# Cette fonction est la version final de mot_jouable utiliser dans le programme principal
    
    P=True
    jok = main.count(JOKER)   # on regarde le nombre de joker
    lettre = main.copy()  # pour pas modifier ll
    mot = list(mot)
        
    for i in mot:
        if i in lettre:
            lettre.remove(i)  # pour eviter de reutiliser des lettre)
        elif JOKER in lettre:
            lettre.remove(JOKER) # on utilise un joker 
        else:
            P=False
    return P


def mot_jouables2(motsfr,main): # Question 16
# Cette fonction version final de mot_jouables utiliser dans lle programme principal
 
    l=[]
    for i in motsfr:
        m=mot_jouable2(i,main)
        if m :
            l.append(i)
    return l

# PARTIE 4 : VALEUR D'UN MOT ###################################################

def generer_dico() :
    """Dictionnaire des jetons.

    >>> jetons = generer_dico()
    >>> jetons['A'] == {'occ': 9, 'val': 1}
    True
    >>> jetons['B'] == jetons['C']
    True
    >>> jetons['?']['val'] == 0
    True
    >>> jetons['!']
    Traceback (most recent call last):
    KeyError: '!'
    """
    jetons = {}
    with Path('lettres.txt').open(encoding='utf_8') as lettres :
        for ligne in lettres :
            l, v, o = ligne.strip().split(';')
            jetons[l] = {'occ': int(o), 'val': int(v)}
    return jetons

dico = generer_dico()


def init_pioche(dico):
    l = []
    for let in dico:
        occ = dico[let]["occ"]
        for i in range(occ):
            l.append(let)
    return l


def valeur_mot(mot, dico):
    pt = 0
    for let in mot:
        pt += dico[let]["val"]
    if len(mot) == 7:
        pt += 50
    return pt


def meilleur_mot(motsfr, ll, dico):
    mj = mots_jouables(motsfr, ll)

    if len(mj) > 0:
        maxi = valeur_mot(mj[0], dico)
        for i in range(1, len(mj)):
            val_mot = valeur_mot(mj[i], dico)
            if val_mot > maxi:
                maxi = val_mot
                j = i

    return mj[j]


def meilleurs_mots(motsfr, ll, dico):
    m = meilleur_mot(motsfr, ll, dico)
    val_m = valeur_mot(m, dico)
    
    l = []
    mj = mots_jouables(motsfr, ll)
    for mot in mj:
        if valeur_mot(mot, dico) == val_m:
            l.append(mot)
    return l


def tour_joueur(main, lp=''): # Question 25
    print(plateau())
    jetons_e = []
    coup = input("Que voulez vous faire (passer/echanger/proposer )")
    if coup == "echanger":
        j = input("Entrer les jetons a echanger ")
        while j != '!':
            j = input("Entrer les jetons a echanger ")
            jetons_e.append(j)
        main = echanger(jetons_e, main, sac)
        return main
    elif coup == 'proposer':
        valeur = 0
        mot = input('Quel mot proposez vous ? ')
        if mot in mot_jouables(motsfr,main,lp):
            valeur = valeur_mot(mot,dico)
        return [valeur, mot] 
    else:
        print("fin du tour")
    print('Joueur suivant')


def detecte_fin_partie2(sac): # Question 26
    if len(sac) == 0:
        print('Fin de partie')

def malus(liste_j, dico):
    pt = 0
    for lettre in liste_j:
        val = dico[lettre]['val']
        pt = pt + val
    return pt

def detecte_fin_partie(sac, joueurs, dico): # Question 26
    
    # On s'assure que la partie soit terminee
    if len(sac) == 0:
        print('Fin de partie')

        # on calcule les malus
        liste_malus = []
        pt = 0
        for nom in joueurs:
            pt = 0
            for lettre in joueurs[nom]:
                val = dico[lettre]['val']
                pt = pt + val
                liste_malus = [].append(pt)
        
        # On calcule les vrais scores
        for nom in joueurs:
            for i in liste_malus:
                joueurs[nom]['score'] = joueurs[nom]['score']-i
        
        # Presentation des resultats et du gagnant
        liste_score = []
        print(nom, 'a', joueurs[nom]['score'], 'points')
        for nom in joueurs:
            print(nom, 'a', joueurs[nom]['score'], 'points')
            liste_score.append(joueurs[nom]['score'], dico)
        for nom in joueurs:
            if joueurs[nom]['score'] == max(liste_score):
                Gagnant = nom
        print('Le gagnant est', Gagnant, 'avec', joueurs[Gagnant]['score'], 'points !!!')

def partie(): # Quetion 28
    
    # on cree les joueurs
    nb_joueur = int(input('Nombre de joueur : '))
    joueurs = {}
    for i in range(nb_joueur): 
        J = input('Saisissez les noms des joueurs :  ')
        joueurs[J] = {"main": [], "score": 0}

     # on crée la pioche
    sac = init_pioche(dico)
    
    # debut de partie
    for nom in joueurs:
        joueurs[nom]["main"].extend(piocher(7, sac))
        print('Voila votre main', joueurs[nom]["main"])
    print()
    # on cree le plateau
    plat = init_jetons()
    while len(sac) > 0:
        for nom in joueurs:
            print('Au tour de', nom, 'de jouer')
            T = tour_joueur(joueurs[nom]["main"], lp='')
            
            # On verifie que le joueur ai choisi de proposer un mot
            if len(T) == 2: 
                joueurs[nom]["score"] += T[0]
                n_main = joueurs[nom]["main"].copy() # Pour s'assurer de pas retirer plusieurs fois la lettre
                for lettre in T[1]:
                    if lettre in n_main:
                        n_main.remove(lettre)
                n_main = completer_main(n_main, sac)
                joueurs[nom]["main"] = n_main
                print(joueurs[nom], joueurs[nom]["main"], joueurs[nom]["score"])
            
            # Cas ou le joueur a choisi echanger
            elif T != None and T != 2:
                print('Voila ta nouvelle pioche', T)
    detecte_fin_partie2(sac)

    # Fin de partie le sac est vide
    liste_score = []
    print(nom, 'a', joueurs[nom]['score'], 'points')
    for nom in joueurs:
        liste_score.append(joueurs[nom]['score']-malus(joueurs[nom]['main'], dico))
    for nom in joueurs:
        if joueurs[nom]['score']-malus(joueurs[nom]['main'], dico) == max(liste_score):
            Gagnant=nom
    print('Le gagnant est', Gagnant, 'avec', joueurs[Gagnant]['score'], 'points !!!')

# PARTIE 6

def lire_coords(plat): # Question 29
    i = int(input('Entrer une coordonnée ligne (1..15) : ')) - 1
    j = int(input('Entrer une coordonnée colonne (1..15) : ')) - 1
    while not (0 <= i < TAILLE_PLATEAU and 0 <= j < TAILLE_PLATEAU) or (plat[i][j] != '' and plat[i][j] not in '²*°^'):
        i = int(input('Entrer une coordonnée ligne valide (1..15) : ')) - 1
        j = int(input('Entrer une coordonnée colonne valide (1..15) : ')) - 1
    return i, j


def tester_placement(plat, i, j, direction, mot):  # Question 30
    lettres = []

    if direction == 'horizontal':
        for k, c in enumerate(mot):
            # vérification bornes
            if not (0 <= j+k < TAILLE_PLATEAU):
                return []
            case = plat[i][j+k]
            if case == '':
                lettres.append(c)
            elif case == c:
                lettres.append(c + '!')   # On marque que la lettre est déjà présente
            else:
                return []                 

    elif direction == 'vertical':
        for k, c in enumerate(mot):
            # vérification bornes
            if not (0 <= i+k < TAILLE_PLATEAU):
                return []
            case = plat[i+k][j]
            if case == '':
                lettres.append(c)
            elif case == c:
                lettres.append(c + '!')   
            else:
                return []                 

    return lettres



def placer_mot(plat, main, i, j, direction, mot, bonus_plateau):  # Question 31
# Cette fonction place le mot sur les coordonnée libre verifier a l'avance   
    
    lettres = tester_placement(plat, i, j, direction, mot)

    if lettres != []:
        if direction == 'horizontal':
            for k, l in enumerate(lettres):
                if '!' in l:    # On regarde si la lettre est deja presente grace a la marque
                    plat[i][j+k] = plat[i][j+k]+l[0]   # on place la lettre sans la case 
                elif l in main:
                    plat[i][j+k] = plat[i][j+k]+l
                    main.remove(l)
                elif JOKER in main:
                    # le joker prend la valeur de la lettre (on place la lettre en minuscule pour marquer le joker)
                    plat[i][j+k] = plat[i][j+k]+l.lower() # On place le joker en minuscule au cas ou quelqu'un forme un mot a partir de ce joker
                    main.remove(JOKER)
                P = True

        elif direction == 'vertical':
            for k, l in enumerate(lettres):
                if '!' in l:    
                    plat[i+k][j] = plat[i+k][j]+l[0]
                elif l in main:
                    plat[i+k][j] = plat[i+k][j]+l
                    main.remove(l)
                elif JOKER in main:
                    plat[i+k][j] = plat[i+k][j]+l.lower() 
                    main.remove(JOKER)
                P = True    
    else:
        P = False
    return P


def valeur_mot2(plat, main, i, j, direction, mot, dico, bonus_plateau):  # Question 32
    
    BMD = False
    BMT = False

    pt = 0

    # On regarde si le joueur utilise tous ses jetons 
    if len(main) == 0:
        pt = pt + 50

    if direction == 'horizontal':

        for k, l in enumerate(mot):
            
            # si la lettre a été placée via un joker, elle est en minuscule sur le plateau
            lettre_plateau = plat[i][j+k]
            if 'a'<=lettre_plateau<='z' and lettre_plateau != '':
                lettre_val = '?'
            else:
                lettre_val = l
            val = dico[lettre_val]['val']
            bonus_case = bonus_plateau[i][j+k] # On teste la case pour voir si c'est un bonus ou non

            # Bonus lettre
            if bonus_case == 'LD':
                val = val*2
                bonus_plateau[i][j+k] = ''
            elif bonus_case == 'LT':
                val = val*3
                bonus_plateau[i][j+k] = ''

            # Bonus mot
            elif bonus_case == 'MD':
                BMD = True
                bonus_plateau[i][j+k] = ''
            elif bonus_case == 'MT':
                BMT = True
                bonus_plateau[i][j+k] = ''
            pt = pt + val

        if BMD:
            pt = pt*2
        if BMT:
            pt = pt*3

    elif direction == 'vertical':

        for k, l in enumerate(mot):
            lettre_plateau = plat[i+k][j]
            if 'a'<=lettre_plateau<='z' and lettre_plateau != '':
                lettre_val = '?'
            else:
                lettre_val = l
            val = dico[lettre_val]['val']
            bonus_case = bonus_plateau[i+k][j]

            if bonus_case == 'LD':
                val = val*2
                bonus_plateau[i+k][j] = ''
            elif bonus_case == 'LT':
                val = val*3
                bonus_plateau[i+k][j] = ''
            elif bonus_case == 'MD':
                BMD = True
                bonus_plateau[i+k][j] = ''
            elif bonus_case == 'MT':
                BMT = True
                bonus_plateau[i+k][j] = ''
            pt = pt + val

        if BMD:
            pt = pt*2
        if BMT:
            pt = pt*3

    return pt


# PARTIE 7

def tour_joueur2(plat, main,): #Question 34 
# Cette fonction est la version final de tour_joueur(plat, main,) 
# qui cette fois popose ttoute les options et leur conséquence repiocher si on pose un mot...
    
    affiche_jetons(plat, bonus_plateau)
    coup = input("que voulez vous faire (passer/echanger/proposer )")
    while not coup in ['passer','echanger','proposer']:
        coup=input("que voulez vous faire (passer/echanger/proposer )")
    
    if coup=="echanger":
        jetons_e=[]
        j=input("Entrer les jetons a échanger  ('!' pour arreter) ")
        while j!='!':
            j=input("Entrer les jetons a échanger ('!' pour arreter)  ")
            jetons_e.append(j)
        main=echanger (jetons_e, main, sac)
        return main

    elif coup=='proposer':
        valeur=0
        i=int(input('entrer les coordonnées de la ligne : ')) 
        j=int(input('entrer les coordonnées de la colonne : '))
        while not 0<=i<=14 and not 0<=j<=14:
            i=int(input('entrer les coordonnées de la ligne : ')) 
            j=int(input('entrer les coordonnées de la colonne : '))
        
        direction=input('Entrer une direction (vertical/horizontal) : ')
        while not direction in ['vertical','horizontal']:
            direction=input('Entrer une direction (vertical/horizontal) : ')
        print(mot_jouables2(motsfr,main))
        mot=input('Quelle mot proposer vous ? :  ')

        # on vérifie d'abord que le mot est jouable avec la main puis on tente le placement
        while not (mot in mot_jouables2(motsfr,main) and tester_placement(plat, i, j, direction, mot) and placer_mot(plat,main, i, j, direction, mot, bonus_plateau)):
           if not tester_placement(plat, i, j, direction, mot):
            # si le mot ne se place pas a cause d'un probleme de placement on redemande des coordonnées et une direction au joueur  
                print('Changer de coordonnées')  
                i=int(input('entrer les coordonnées de la ligne : ')) 
                j=int(input('entrer les coordonnées de la colonne : '))
                while not 0<=i<=14 and not 0<=j<=14:
                    i=int(input('entrer les coordonnées de la ligne : ')) 
                    j=int(input('entrer les coordonnées de la colonne : '))
                direction=input('Entrer une direction (vertical/horizontal) : ')
                while not direction in ['vertical','horizontal']:
                    direction=input('Entrer une direction (vertical/horizontal) : ')
                    print(mot_jouables2(motsfr,main))
                mot=input('Quelle mot proposer vous ? :  ')
        valeur=valeur_mot2(plat,main, i, j, direction, mot, dico, bonus_plateau) 
        return [valeur,mot] 
    
    else:
        print("fin du tour")
    print('Joueur suivant')



if __name__ == '__main__':
    dico = generer_dico()
    motsfr = generer_dictfr()
    sac = init_pioche(dico)
    
    # Question 35 PROGRAMME PRINCIPAL
    
    # on crée les joueurs
    nb_joueur = int(input('Nombre de joueurs : '))
    while type(nb_joueur) != int and 2 <= nb_joueur <= 14:
        nb_joueur = int(input('Nombre de joueurs : '))
    
    joueurs = {}
    for i in range(nb_joueur):
        J = input('Saisissez les noms des joueurs : ')
        joueurs[J] = {"main": [], "score": 0}
    
    # On crée la pioche
    sac = init_pioche(dico)
    random.shuffle(sac)
        
    # début de partie
    for nom in joueurs:
        joueurs[nom]["main"].extend(piocher(7, sac))
        print('Voila votre main', nom, joueurs[nom]["main"])
    print()
    
    # on crée le plateau
    bonus_plateau = init_bonus()
    plat = init_jetons() 
    while len(sac) > 0:
        for nom in joueurs:
            print('Au tour de', nom, 'de jouer')
            T = tour_joueur2(plat, joueurs[nom]["main"])
                
            # On vérifie que le joueur a choisie de proposer un mot
            if len(T) == 2: 
                joueurs[nom]["score"] += T[0]
                joueurs[nom]["main"] = completer_main(joueurs[nom]["main"], sac)
                print(joueurs[nom], joueurs[nom]["main"], joueurs[nom]["score"])
                affiche_jetons(plat, bonus_plateau)
                
            # Cas ou le joueur a choisie échanger
            elif T != None and T != 2:
                print('Voila ta nouvelle pioche', T)
    
    # Fin de partie le sac est vide
    detecte_fin_partie(sac, joueurs, dico)
