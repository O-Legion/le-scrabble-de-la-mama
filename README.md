# le-scrabble-de-la-mama
Projet Scrabble inf

# Partie 2

#init_pioche_aléa() 
est la première version de la fonction qui gère la construction aléatoire de la pioche du scrabble.

#piocher(x,sac)
prmet au joueur de piocher un nombre x de jetons dans le sac

#completer_main(main, sac)
permet au joueur de completer sa main une fois certains de sess jetons poser

#echanger(jetons, main, sac)
permet au joueur d'echanger certain jetons qu'il a en main

#sim_partie()
sim partie simuler un bout de partie de scabble dans laquelle les joueurs oobtienne une pioche et font des échanges

# Partie 3

#select_mot_initiale(motsfr,let)
crée une liste vide puis regarde dans motsfr et ajoute a la liste créer les mots commençant par let.

#select_mot_longueur(motsfr,lgr)
crée une liste vide puis regarde dans motsfr et ajoute a la liste créer les mots de longueur lgr.

#mot_jouable(mot,ll,lp)
renvoie un booléen indiquant si oui le mot est jouable ou non en fonction de la main ll et des lettres presente lp.

#mot_jouables(motsfr,ll,lp)
renvoie une liste de mot jouables determinés avec mot_jouable(mot,ll,lp)

#init_pioche(dico)
version final de la fonction qui gère la construction de la pioche du scrabble a l'aide d'un dico.

#mot_jouable2(mot,main)
version final de mot_jouable utiliser dans lle programme principal

#mot_jouable2s(mot,main)
version final de mot_jouables utiliser dans lle programme principal

# Partie 4

#valeur_mot(mot,dico)
calcul la valeur des mot grace au dico.

meilleur_mot(motsfr, ll, dico, lp)
renvoie une liste des mot jouable valent le plus de points 

# Partie 5

#tour_joueur(main,lp='')
première version de la fonction qui gère le tour des joueurs (échanger/passer/proposer)

#detecte_fin_partie2(sac)
première version de la fonction qui gère la fin d'une partie cette version verifie seulement l'etat du sac

#detecte_fin_partie(sac, joueurs, dico)
version final de detecte_fin_partie qui gere aussi le compte des point et des malus

#partie()
simule une partie un peut plus avancer que simule partie avec la gestion des tour via tour_joueur

# Partie 6

#lire_coords(plat)
renvoie les coorée des cases vides d'unplateau

#tester_placement(plat, i, j, direction, mot)
vérifie a partir d'une coordonnée si le mot est plaçable en parcourant les case verticalement ou horizontalement

#placer_mot(plat, main, i, j, direction, mot, bonus_plateau)
place le mot sur les coordonnée libre verifier a l'avance

#valeur_mot2(plat, main, i, j, direction, mot, dico, bonus_plateau)
version final de la fonction qui calcul la valeur des mot grace au dico, prend en compte les bonus appliquer sur les mot et les lettres

# Partie 7

#tour_joueur2(plat, main,)
version final de tour_joueur(plat, main,) qui cette fois popose ttoute les options et leur conséquence repiocher si on pose un mot...




