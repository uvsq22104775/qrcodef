import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 



######            A PRECISER : BEAUCOUP DE PROBLEME D'IMPORTATION LIEES A PILLOW , ne veut pas s'importer correctement   ###########


def saving(matPix, filename):#sauvegarde l'image contenue dans matpix dans le fichier filename
							 #utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave=pil.Image.new(mode = "1", size = (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)

def loading(filename):#charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
					  #l'image en noir et blanc
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat


create=True
nomImgCourante=""
nomImgDebut = ""

def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    global nomImgDebut
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante=filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)
        create=False
        
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin=canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)

def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante="modif.png"

def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

image_courante = "qr_code_ssfiltre_ascii_rotation.png"




# DEBUT DU PROGRAMME 

# Question 1 -- Dimension des coins de la matrice, fonction qui trouve le coin manquant, rotation de l'image

matrice = loading(image_courante)



def symbole_matrice():

    global symbole_matrice

    symbole_matrice = [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,11,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1]
                       

    return symbole_matrice

def coin_mystere():

    global symbole_matrice
    global qrcode_trouver
    

    cpt = 0

    coin_mystere = []
    for i in range(18,25):
        for j in range(18,25):
            coin_mystere.append(matrice[i][j])

    print(coin_mystere)

    while cpt < 3 :

        matrice = rotate(matrice)
        coin_mystere = []
        for i in range(18,25):
            for j in range(18,25):
                coin_mystere.append(matrice[i][j])
    cpt += 1

    qrcode_trouver = matrice

    saving(qrcode_trouver, "photo.png")
    return qrcode_trouver



def rotate():
    mat=loading(nomImgCourante)
    matrotate=[[(0,0,0,255)] *(nbrLig(mat)) for j in range(nbrCol(mat))]
    for i in range(nbrLig(matrotate)):
        for j in range(nbrCol(matrotate)):
            matrotate[i][j]=mat[nbrLig(mat)-j-1][i]
    modify(matrotate)


# Question 2 -- Fonction qui verifie que ces lignes apparaissent correctement

def verification_ligne():

    matrice = loading(image_courante)
    qr_code = []
    cpt = 0
    pointillée = [0,1,0,1,0,1,0,1]

    matrice_ligne = []
    matrice_colonne = []
    for i in range(8,16):
        matrice_ligne.append(matrice[6][i])
        matrice_colonne.append(matrice[i][6])

    while cpt < 3 :
        if matrice_colonne != nbrLig or matrice_ligne != nbrLig :
            matrice = rotate(matrice)
            matrice_colonne = []
            matrice_ligne = []
            for i in range(8, 16):
                matrice_colonne.append(matrice[6][i])
                matrice_ligne.append(matrice[i][6])
        cpt += 1

qrcode = matrice

saving(qrcode)


print(qrcode)

    



# Question 3 -- Fonction qui lit 7 bits et renvoie 4 bit après correction d'erreur

def code_Hammings(liste):

    l = []

    valeur_1 = (liste[0] + liste[1] + liste[3])%2
    valeur_2 = (liste[0] + liste[2] + liste[3])%2
    valeur_3 = (liste[1] + liste[2] + liste[3])%2
    if (valeur_1 != liste[4] and valeur_2 != liste[5] and c3 ==liste[6]):
        liste[0] = (liste[0] + 1)%2
    if (valeur_2 != liste[4] and valeur_2 != liste[6] and valeur_2 ==liste[5]):
        liste[1] = (liste[1] + 1 )%2
    if (valeur_2 != liste[5] and valeur_3 != liste[6]) and valeur_1 ==liste[4]:
        liste[2] = (liste[2]+ 1)%2
    if valeur_2 != liste[5] and valeur_3 != liste[6] and valeur_1 != liste[4]:
        liste[3] =(liste[3] + 1)%2
    if valeur_1 != liste[4] and (valeur_2 == liste[5] and valeur_3 == liste[6]):
        liste[4] = (liste[4]+ 1)%2
    if valeur_2 != liste[5] and (valeur_1 == liste[4] and valeur_3 == liste[6]):
        liste[5] = (liste[5] + 1)%2
    if valeur_3 != liste[6] and (valeur_2==liste[5] and valeur_3 == liste[4]):
        liste[6] = (liste[6] + 1)%2

    l.append(liste[0])
    l.append(liste[1])
    l.append(liste[2])
    l.append(liste[3])

    return l 







# Question 4 -- Programmer une fonction qui parcourt l’image d’un QR code pour renvoyer l’information lue sous la
            #  forme d’une liste de listes de 14 bits

mat_charger = []
res =[[],[]]

def parcour_code(x,y):

    global res

    res =[[],[]]

    for i in range(2):
        for j in range(7):
            res[i].append(mat_charger[x+i][y+j])
    return res

parcour_matrice = [[2,2,2,2,2,2,2], [2,2,2,2,2,2,2]]

def parcour_bloc_de_droite_à_gauche(x,y):
    global parcour_matrice
    parcour_code(x,y)
    k = 0
    for j in range(7):
        if j%2 == 0:
           parcour_matrice[0][j] = res[(j+1)%2][-1-k]
           parcour_matrice[1][j] = res[j%2][-4-k]
           k = k + 1
        else:

            k = k - 1
            parcour_matrice[0][j] = res[(j+1)%2][-1-k]
            k = k + 1
            parcour_matrice[1][j]= res[j%2][-4-k]

parcour_matrice[0][6] = res[1][3]
parcour_matrice[1][6] = res[0][0]

print(parcour_matrice)




def parcour_bloc_de_gauche_à_droite(x,y):

    global parcour_matrice
    parcour_code(x,y)
    k = 0
    for j in range(7):
        if j%2 == 0:
            parcour_matrice[0][j] = res[(j+1)%2][k]
            parcour_matrice[1][j] = res[j%2][3+k]
            k = k + 1
        else: 
            k = k - 1
            parcour_matrice[0][j] = res[(j+1)% 2][ k]
            k = k+1
            parcour_matrice[1][j] = res[j % 2][3 + k]
    parcour_matrice[0][6] = res[1][3]
    parcour_matrice[1][6] = res[0][6]

    return parcour_matrice

def parcour_bloc(x,y):
    if x == 11 or x == 15 or x == 19 or x== 23:
       return  parcour_bloc_de_droite_à_gauche(x,y)
        
    else:
        return parcour_bloc_de_gauche_à_droite(x,y)

# Question 5 -- Afficher le contenu d’un QR code, en prenant en compte le type de données

def symboles_hexadecimaux(liste1, liste2):
    

    symboles_hexadecimaux = (symbole_1, symbole_2)

    symbole_1 = 0
    symbole_2 = 0

    liste = liste1 + liste2

    if mat_charger[24][8] == 1:
        for i in range(len(liste1)):
            symbole_1 = symbole_1 + (liste1[-i-1]*(2**i))
        if symbole_1 == 10:
            symbole_1 = "A"
        if symbole_1 == 11:
            symbole_1 = "B"
        if symbole_1 == 12:
           symbole_1 = "C"
        if symbole_1 == 13:
            symbole_1 =="D"
        if symbole_1 == 14:
            symbole_1 = "E"
        if symbole_1 == 15:
            symbole_1 = "F"

        print(symbole_1)

        symboles_hexadecimaux += str(symbole_1) 
        for i in range(len(liste2)):
            symbole_2 += (liste2[-i-1]*(2**i))
        if symbole_2 == 10:
            symbole_2 = "A"
        if symbole_2 == 11:
            symbole_2 = "B"
        if symbole_2 == 12:
            symbole_2 = "C"
        if symbole_2 == 13:
            symbole_2 = "D"
        if symbole_2 == 14:
            symbole_2 = "E"
        if symbole_2 == 15:
            symbole_2 = "F"

        print(symbole_2)
        symboles_hexadecimaux += str(symbole_2)

    else:
            liste3= []
            for i in range(len(liste)-1):
                liste3.append(liste[-i])
            for i in range(len(liste3)):
                symbole += (liste3[-i-1]*(2**i))
            symbole = chr(s)
            symboles_hexadecimaux += symbole
    print("message :", symboles_hexadecimaux)





# Question 6 -- Fonction qui applique le bon filtre selon les bits de controle

def filtre(matrice):

    image_filtre = [matrice[22][8]] + [matrice[23][8]]

    filtre_de_la_matrice = [[0]*nbrCol(matrice) for i in range(nbrLig(matrice))]

    if image_filtre == [0,0]:
    
     print("pas de changement , entierement noire")

    elif image_filtre == [0,1]:

      pixel = 0
    for i in range(nbrLig(matrice)):
        for j in range(nbrCol(matrice)):
            filtre_de_la_matrice[i][j] = pixel
            if pixel == 0:
                pixel = 1
            else:
                pixel = 0
        if filtre_de_la_matrice[i][0] == 0:
                pixel = 1
        else:
            pixel = 0
    print("case en haut à gauche noire")


    image_filtre == [1,0]
    pixel = 0
    for i in range(nbrLig(matrice)):
         for j in range(nbrCol(matrice)):
             filtre_de_la_matrice[i][j] = pixel
         if pixel == 0:
             pixel = 1
         else:
             pixel = 0

    print("des lignes horizontales alternees noires et blanches, la plus haute etant noire")
   


    image_filtre == [1,1]
    pixel = 0
    for i in range(nbrLig(matrice)):
          for j in range(nbrCol(matrice)):
            filtre_de_la_matrice[i][j] = pixel
            if pixel == 0:
                pixel = 1
            else:
                pixel = 0
    if filtre_de_la_matrice[i][0] == 0:
            pixel = 0
    else:
        pixel = 1

        return filtre_de_la_matrice

    print("des lignes verticales alternees noires et blanches, la plus a gauche etant noire")

# Question 7 -- Décoder tous les QR codes donnees en exemple, pour verifier si votre code fonctionne. Le QR code
               # contient une suite de valeurs hexadecimales qui commence par 14BAD et contient 10 valeurs


def nbr_bloc_à_decoder(matrice):

    liste = [matrice[13][0],matrice[14][0],matrice[15][0],matrice[16][0],matrice[17][0]]
    
    nbr_bloc = conversionEntier(liste)
    print(nbr_bloc)
    return nbr_bloc

def conversionEntier(liste):
    res = 0
    liste.reverse()
    for i in range(len(liste)):
        res+= liste[i]*(2**i)

    return res

 
#Tkinter -- boucles principale

racine = tk.Tk()

Bouton_charger = tk.Button(racine, text="charger", command=lambda:charger(racine))
Bouton_charger.grid(row = 5, column =1)

Bouton_lire = tk.Button(racine, text="lire", command=lambda: lire())
Bouton_lire.grid(row=5, column=2) 

Label = tk.Label(racine, text="")
Label.grid(row=6, column =1, columnspan=2)

racine.mainloop()





