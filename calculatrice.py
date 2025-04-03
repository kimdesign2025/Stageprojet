from tkinter import *
#declaration des fonctions

expression ="" # pour garder ce qu'on a mis dans la calculatrice'
def appuyer (touche):
    if touche=="=":
        calculer()
        return
    global expression
    expression +=str(touche)
    equation.set(expression)

def calculer ():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        expression =""
        equation.set=""

def effacer ():
   global expression
   expression=""
   equation.set("")



if __name__ == "__main__":
    gui = Tk()  # Initialiser l'interface graphique Tkinter

    # Couleur du fond de la calculatrice
    gui.configure(background="#101419")

    # Titre de la calculatrice 
    gui.title("CALCULATOR")

    # Taille de la calculatrice
    gui.geometry("235x385")

    #variable pour stoker le contenue
    equation = StringVar()

    #boite de resultat
    resultat = Label(gui,bg="#101419",fg="#FFF",textvariable= equation, height="2")

    resultat.grid(columnspan=4) #nbre de colonne 

    #les boutons de la calculatrice
    boutons =[7, 8 ,9 ,"*", 4 , 5 , 6 ,"-", 1 , 2 , 3 ,"+", 0 , "." ,"/","="]

    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C9B" ,fg="#FFF",height=4,width=6) #couleur dutexte,du boutons et sa taille
        #pour rendre le texte clicquable
        b.bind("<Button-1>" ,lambda e, bouton=bouton:appuyer(bouton))
        b.grid(row= ligne ,column=colonne)#definir la ligne et la colunne 
        colonne +=1
        if colonne==4:
            colonne=0
            ligne +=1

    b = Label(gui, text="Effacer", bg="#984447" ,fg="#FFF",height=4,width=26) 
    b.bind("<Button-1>" ,lambda e: effacer())
    b.grid(columnspan=4)
    # ----
    # 789*
    # 456-
    # 123+
    # 0,/=
    # ----
    # Exécuter la boucle principale de l'interface
    gui.mainloop()