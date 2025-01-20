from tkinter import *

"""
NB:Pour des raisons de performances, plus le tableau est grand, plus l'exécution du code est lente! Ainsi, privilégiez une taille de:
    ¤400x400 pour une éxecution extremement rapide
    ¤500x500 pour une éxecution très rapide
    ¤600x600 pour une éxecution rapide
    ¤800x800 pour une éxecution lente (environ 3 actualisations par seconde)
"""

#Définition d'une partie de jeu de la vie
class Jeudelavie:

#Constructeur de la classe Jeudelavie
#Attribut hauteur: nombre de lignes du tableau
#Attribut largeur: nombre de colonnes
#Attribut dico_tv: dictionnaire contenant  les coordonées d'une cellule et le nombre de cellules vivantes autour d'elle
#Attribut dico_co: dictionnaire contenant les coordonées d'une cellule et son état (vivante ou morte)
#Attribut couleur: couleur des cellules vivantes

    def __init__(self, hauteur=500, largeur=500, couleur='black'):
        self.hauteur=hauteur
        self.largeur=largeur
        self.couleur=couleur
        self.dico_tv={}
        self.dico_co={}
        i=0
        while i!= self.largeur/c: 
            j=0
            while j!= self.hauteur/c:
                x=i*c
                y=j*c
                self.dico_co[x,y]=0
                j+=1
            i+=1
            
#Méthode créant le plateau de jeu
            
    def plateau(self):
        t_x=0
        while t_x!=self.largeur:
            tab.create_line(t_x,0,t_x,self.hauteur,width=1,fill='black')
            t_x+=c
        t_y=0
        while t_y!=self.hauteur:
            tab.create_line(0,t_y,self.largeur,t_y,width=1,fill='black')
            t_y+=c
            
#Méthode donnant la vie à une cellule
            
    def vie(self, event):
        x=event.x -(event.x%c)
        y=event.y -(event.y%c)
        tab.create_rectangle(x, y, x+c, y+c, fill=self.couleur)
        self.dico_co[x,y]=1

#Méthode tuant une cellule
        
    def mort(self, event):
        x=event.x -(event.x%c)
        y=event.y -(event.y%c)
        tab.create_rectangle(x, y, x+c, y+c, fill='white')
        self.dico_co[x,y]=0

#Méthode renvoyant la valeur d'une cellule
        
    def valeur_cel(self, x, y):
        return self.dico_co[x, y]

#Méthode compilant le nombre de cellules vivantes autour d'une cellule dans le dictionnaire self.dico_tv
    
    def total_voisins(self):
        global flag
        i=0
        while i!= self.largeur/c: 
            j=0
            while j!= self.hauteur/c:
                x=i*c
                y=j*c
                if y==0: #Ligne du haut
                    if x==0: #Coin en haut à gauche
                        self.dico_tv[x, y]=self.valeur_cel(x, y+c)+self.valeur_cel(x+c, y)+self.valeur_cel(x+c, y+c)
                    elif x==self.largeur-c: #Coin en haut à droite
                        self.dico_tv[x, y]=self.valeur_cel(x-c, y)+self.valeur_cel(x-c, y+c)+self.valeur_cel(x, y+c)
                    else: #Ligne du haut sans les coins
                        self.dico_tv[x, y]=self.valeur_cel(x-c, y)+self.valeur_cel(x-c, y+c)+self.valeur_cel(x, y+c)+self.valeur_cel(x+c, y+c)+self.valeur_cel(x+c, y+c)
                elif y==self.hauteur-c: #Ligne du bas
                    if x==0: #Coin en bas à gauche
                        self.dico_tv[x, y]=self.valeur_cel(x, y-c)+self.valeur_cel(x+c, y-c)+self.valeur_cel(x+c, y)
                    elif x==self.largeur-c: #Coin en bas à droite
                        self.dico_tv[x, y]=self.valeur_cel(x-c, y-c)+self.valeur_cel(x-c, y)+self.valeur_cel(x, y-c)
                    else: #Ligne du bas sans les coins
                        self.dico_tv[x, y]=self.valeur_cel(x-c, y-c)+self.valeur_cel(x-c, y)+self.valeur_cel(x, y-c)+self.valeur_cel(x+c, y-c)+self.valeur_cel(x+c, y)
                else: #Autres cellules
                    if x==0: #Bord de gauche
                        self.dico_tv[x, y]=self.valeur_cel(x, y-c)+self.valeur_cel(x, y+c)+self.valeur_cel(x+c, y-c)+self.valeur_cel(x+c, y)+self.valeur_cel(x+c, y+c)
                    elif x==self.largeur-c: #Bord de droite
                        self.dico_tv[x, y]=self.valeur_cel(x-c, y-c)+self.valeur_cel(x-c, y)+self.valeur_cel(x-c, y+c)+self.valeur_cel(x, y-c)+self.valeur_cel(x, y+c)
                    else: #Toutes les cases qui ne sont pas sur les bords ou dans les coins
                        self.dico_tv[x, y]=self.valeur_cel(x-c, y-c)+self.valeur_cel(x-c, y)+self.valeur_cel(x-c, y+c)+self.valeur_cel(x, y-c)+self.valeur_cel(x, y+c)+self.valeur_cel(x+c, y-c)+self.valeur_cel(x+c, y)+self.valeur_cel(x+c, y+c)
                j+=1
            i+=1
        if flag==1: #Cette partie permet d'exécuter le code en boucle. Le if permet un arrêt rapide de la boucle en cas d'appui sur la touche espace (Cf. méthode run)
            self.resultat()
        
#Méthode redessinant le plateau en fonction des résultats obtenus au tour précédent
        
    def resultat(self):
        global flag
        tab.delete(ALL)
        self.plateau()
        i=0
        while i!= self.largeur/c:
            j=0
            while j!= self.hauteur/c:
                x=i*c
                y=j*c
                if (self.dico_tv[x, y]==3 or self.dico_tv[x, y]==2) and self.dico_co[x, y]==1:
                    self.dico_co[x, y]=1
                    tab.create_rectangle(x, y, x+c, y+c, fill=self.couleur)
                elif self.dico_co[x, y]==0 and self.dico_tv[x, y]==3:
                    self.dico_co[x, y]=1
                    tab.create_rectangle(x, y, x+c, y+c, fill=self.couleur)
                else:
                    self.dico_co[x, y]=0
                    tab.create_rectangle(x, y, x+c, y+c, fill='white')   
                j+=1
            i+=1
        if flag==1: #Cette partie permet d'exécuter le code en boucle. Le if permet un arrêt rapide de la boucle en cas d'appui sur la touche espace (Cf. méthode run)
            fen.after(50, self.total_voisins)

#Méthode permettant de lancer le jeu ou de l'arrêter
        
    def run(self, event):
        global flag
        if flag==0:
            flag=1
            self.total_voisins()
        else:
            flag=0

#Méthode réinitialisant le jeu à l'aide d'une touche

    def suppr(self, event):
        global flag
        flag=0
        tab.delete(ALL)
        self.dico_tv={}
        self.dico_co={}
        i=0
        while i!= self.largeur/c: 
            j=0
            while j!= self.hauteur/c:
                x=i*c
                y=j*c
                self.dico_co[x,y]=0
                j+=1
            i+=1
        self.plateau()

#Méthode réinitialisant le jeu directement depuis une commande (Utile pour les structures préenregistrées)
        
    def c_suppr(self):
        global flag
        flag=0
        tab.delete(ALL)
        self.dico_tv={}
        self.dico_co={}
        i=0
        while i!= self.largeur/c:
            j=0
            while j!= self.hauteur/c:
                x=i*c
                y=j*c
                self.dico_co[x,y]=0
                j+=1
            i+=1
        self.plateau()

#Méthode permettant l'actualisation du plateau après utilisation des méthode créant des structures prédefinies

    def actualiser(self):
        i=0
        while i!= self.largeur/c:
            j=0
            while j!= self.hauteur/c:
                x=i*c
                y=j*c
                if self.dico_co[x,y]==1:
                    tab.create_rectangle(x, y, x+c, y+c, fill=self.couleur)
                else:
                    tab.create_rectangle(x, y, x+c, y+c, fill='white')
                j+=1
            i+=1

    """
    Les méthodes qui suivent doivent être utilisées sur un plateau de jeu de 500x500
    pour une expérience optimale.
    """
    
#Méthode permettant de créer un canon à planeurs

    def canonplaneurs(self, event):
        global flag
        flag=0
        self.c_suppr()
        self.dico_co[2*c,6*c]=1
        self.dico_co[2*c,7*c]=1
        self.dico_co[3*c,6*c]=1
        self.dico_co[3*c,7*c]=1
        self.dico_co[12*c,6*c]=1
        self.dico_co[13*c,5*c]=1
        self.dico_co[14*c,4*c]=1
        self.dico_co[15*c,4*c]=1
        self.dico_co[12*c,7*c]=1
        self.dico_co[12*c,8*c]=1
        self.dico_co[13*c,9*c]=1
        self.dico_co[14*c,10*c]=1
        self.dico_co[15*c,10*c]=1
        self.dico_co[17*c,9*c]=1
        self.dico_co[18*c,8*c]=1
        self.dico_co[18*c,7*c]=1
        self.dico_co[19*c,7*c]=1
        self.dico_co[16*c,7*c]=1
        self.dico_co[18*c,6*c]=1
        self.dico_co[17*c,5*c]=1
        self.dico_co[22*c,6*c]=1
        self.dico_co[23*c,6*c]=1
        self.dico_co[23*c,5*c]=1
        self.dico_co[22*c,5*c]=1
        self.dico_co[22*c,4*c]=1
        self.dico_co[23*c,4*c]=1
        self.dico_co[24*c,3*c]=1
        self.dico_co[26*c,3*c]=1
        self.dico_co[26*c,2*c]=1
        self.dico_co[24*c,7*c]=1
        self.dico_co[26*c,7*c]=1
        self.dico_co[26*c,8*c]=1
        self.dico_co[36*c,5*c]=1
        self.dico_co[37*c,5*c]=1
        self.dico_co[37*c,4*c]=1
        self.dico_co[36*c,4*c]=1
        self.actualiser()
        
#Méthode créant des vaisseaux spatiaux (Structures pouvant se déplacer, comme les planeurs) de 3 tailles différentes

    def vaisseaux(self,event):
        global flag
        flag=0
        self.c_suppr()
        #Grand vaisseau
        self.dico_co[6*c,4*c]=1
        self.dico_co[7*c,4*c]=1
        self.dico_co[8*c,4*c]=1
        self.dico_co[9*c,4*c]=1
        self.dico_co[10*c,4*c]=1
        self.dico_co[11*c,4*c]=1
        self.dico_co[11*c,5*c]=1
        self.dico_co[11*c,6*c]=1
        self.dico_co[10*c,7*c]=1
        self.dico_co[8*c,8*c]=1
        self.dico_co[7*c,8*c]=1
        self.dico_co[5*c,7*c]=1
        self.dico_co[5*c,5*c]=1
        #Vaisseau moyen
        self.dico_co[7*c,13*c]=1
        self.dico_co[8*c,13*c]=1
        self.dico_co[9*c,13*c]=1
        self.dico_co[10*c,13*c]=1
        self.dico_co[11*c,13*c]=1
        self.dico_co[11*c,14*c]=1
        self.dico_co[11*c,15*c]=1
        self.dico_co[10*c,16*c]=1
        self.dico_co[8*c,17*c]=1
        self.dico_co[6*c,16*c]=1
        self.dico_co[6*c,14*c]=1
        #Petit vaisseau
        self.dico_co[8*c,22*c]=1
        self.dico_co[9*c,22*c]=1
        self.dico_co[10*c,22*c]=1
        self.dico_co[11*c,22*c]=1
        self.dico_co[11*c,23*c]=1
        self.dico_co[11*c,24*c]=1
        self.dico_co[10*c,25*c]=1
        self.dico_co[7*c,25*c]=1
        self.dico_co[7*c,23*c]=1
        self.actualiser()
              
#Méthode permettant de créer un Pulsar (Structure oscillante de période 3)

    def pulsar(self, event):
        global flag
        flag=0
        self.c_suppr()
        self.dico_co[20*c,10*c]=1
        self.dico_co[20*c,11*c]=1
        self.dico_co[20*c,12*c]=1
        self.dico_co[20*c,13*c]=1
        self.dico_co[20*c,14*c]=1
        self.dico_co[22*c,10*c]=1
        self.dico_co[22*c,14*c]=1
        self.dico_co[24*c,10*c]=1
        self.dico_co[24*c,11*c]=1
        self.dico_co[24*c,12*c]=1
        self.dico_co[24*c,13*c]=1
        self.dico_co[24*c,14*c]=1
        self.actualiser()
            
#Méthode permettant de créer un Pentadécathlon (Structure oscillante de période 15)

    def pentadecathlon(self, event):
        global flag
        flag=0
        self.c_suppr()
        self.dico_co[20*c,10*c]=1
        self.dico_co[21*c,10*c]=1
        self.dico_co[22*c,10*c]=1
        self.dico_co[23*c,10*c]=1
        self.dico_co[24*c,10*c]=1
        self.dico_co[25*c,10*c]=1
        self.dico_co[26*c,10*c]=1
        self.dico_co[27*c,10*c]=1
        self.dico_co[28*c,10*c]=1
        self.dico_co[29*c,10*c]=1
        self.actualiser()
        
#Méthode créant un "doublepenta"

    def doublepenta(self, event):
        global flag
        flag=0
        self.c_suppr()
        #Partie droite
        self.dico_co[26*c,24*c]=1
        self.dico_co[26*c,23*c]=1
        self.dico_co[26*c,25*c]=1
        self.dico_co[28*c,26*c]=1
        self.dico_co[29*c,26*c]=1
        self.dico_co[31*c,25*c]=1
        self.dico_co[31*c,24*c]=1
        self.dico_co[31*c,23*c]=1
        self.dico_co[29*c,22*c]=1
        self.dico_co[28*c,22*c]=1
        self.dico_co[32*c,24*c]=1
        self.dico_co[33*c,24*c]=1
        self.dico_co[34*c,24*c]=1
        self.dico_co[34*c,25*c]=1
        self.dico_co[34*c,23*c]=1
        self.dico_co[36*c,22*c]=1
        self.dico_co[37*c,22*c]=1
        self.dico_co[39*c,23*c]=1
        self.dico_co[39*c,24*c]=1
        self.dico_co[39*c,25*c]=1
        self.dico_co[37*c,26*c]=1
        self.dico_co[36*c,26*c]=1
        #Partie gauche
        self.dico_co[22*c,24*c]=1
        self.dico_co[22*c,23*c]=1
        self.dico_co[22*c,25*c]=1
        self.dico_co[20*c,26*c]=1
        self.dico_co[19*c,26*c]=1
        self.dico_co[17*c,25*c]=1
        self.dico_co[17*c,24*c]=1
        self.dico_co[17*c,23*c]=1
        self.dico_co[19*c,22*c]=1
        self.dico_co[20*c,22*c]=1
        self.dico_co[16*c,24*c]=1
        self.dico_co[15*c,24*c]=1
        self.dico_co[14*c,24*c]=1
        self.dico_co[14*c,25*c]=1
        self.dico_co[14*c,23*c]=1
        self.dico_co[12*c,22*c]=1
        self.dico_co[11*c,22*c]=1
        self.dico_co[9*c,23*c]=1
        self.dico_co[9*c,24*c]=1
        self.dico_co[9*c,25*c]=1
        self.dico_co[11*c,26*c]=1
        self.dico_co[12*c,26*c]=1
        self.actualiser()

#Méthode créant une spirale de ruches

    def spiruche(self, event):
        global flag
        flag=0
        self.c_suppr()
        #Ruche de droite
        self.dico_co[27*c,24*c]=1
        self.dico_co[27*c,23*c]=1
        self.dico_co[28*c,23*c]=1
        self.dico_co[29*c,23*c]=1
        self.dico_co[30*c,24*c]=1
        self.dico_co[29*c,25*c]=1
        self.dico_co[28*c,25*c]=1
        #Ruche du haut
        self.dico_co[24*c,21*c]=1
        self.dico_co[23*c,21*c]=1
        self.dico_co[23*c,20*c]=1
        self.dico_co[23*c,19*c]=1
        self.dico_co[24*c,18*c]=1
        self.dico_co[25*c,19*c]=1
        self.dico_co[25*c,20*c]=1
        #Ruche de gauche
        self.dico_co[21*c,24*c]=1
        self.dico_co[21*c,25*c]=1
        self.dico_co[20*c,25*c]=1
        self.dico_co[19*c,25*c]=1
        self.dico_co[18*c,24*c]=1
        self.dico_co[19*c,23*c]=1
        self.dico_co[20*c,23*c]=1
        #Ruche du bas
        self.dico_co[24*c,27*c]=1
        self.dico_co[25*c,27*c]=1
        self.dico_co[25*c,28*c]=1
        self.dico_co[25*c,29*c]=1
        self.dico_co[24*c,30*c]=1
        self.dico_co[23*c,29*c]=1
        self.dico_co[23*c,28*c]=1
        self.actualiser()
        
        
#Taille d'une cellule
c=10
#Définition du "flag" qui est une variable permettant l'arrêt et le lancement de l'exécution du programme
flag=0
#Définition du jeu
j=Jeudelavie()

"""
NB: Ici, l'interface graphique est conçue pour fonctionner avec l'instance de la classe Jeudelavie "j".
Si vous souhaitez modifier le nom de cette instance, pensez à le faire également dans les lignes qui suivent ce message !
"""

#Affichage des touches
print('espace--> Lancer ou stopper le jeu')
print('s--> Supprimer toutes les cellules du plateau')
print('a--> Créer un canon à planeurs')
print('z--> Créer des planeurs de 3 tailles différentes')
print('e--> Créer un Pulsar')
print('r--> Créer un Pentadécathlon')
print('t--> Créer un Doublepenta')
print('y--> Créer une Spirale de ruches')

#Définition de la fenêtre tkinter
fen=Tk()
fen.title("Jeu De La Vie")
fen.geometry("1000x1000")
fen.minsize(800, 800)
fen.configure(bg='grey')
fen.bind("<space>", j.run)
fen.bind("<KeyPress-s>", j.suppr)
fen.bind("<KeyPress-a>", j.canonplaneurs)
fen.bind("<KeyPress-z>", j.vaisseaux)
fen.bind("<KeyPress-e>", j.pulsar)
fen.bind("<KeyPress-r>", j.pentadecathlon)
fen.bind("<KeyPress-t>", j.doublepenta)
fen.bind("<KeyPress-y>", j.spiruche)

#Définition du plateau de jeu
tab=Canvas(fen, width=j.largeur, height=j.hauteur, bg='white')
tab.bind("<Button-1>", j.vie)
tab.bind("<Button-3>", j.mort)
tab.pack(expand=True)

#Création du jeu
j.plateau()
fen.mainloop()
