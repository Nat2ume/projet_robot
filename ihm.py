from tkinter import * 

fenetre = Tk()
def clavier(event):
    global coords

    touche = event.keysym

    if touche == "z":
        coords = (350, 325)
    elif touche == "s":
        coords = (350, 475)
    elif touche == "d":
        coords = (450, 400)
    elif touche == "q":
        coords = (250,400)
    elif touche == "e":
        coords = (450,325)
    elif touche == "a":
        coords = (250,325)
    elif touche == "space" :
        coords = (350,400)
    # changement de coordonnées pour le rectangle
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+50, coords[1]+50)

# création du canvas

canvas = Canvas(fenetre, width=700, height=850, bg="ivory",background="oldlace")

rectangle0 = canvas.create_rectangle(350,400,400,450)
txt = canvas.create_text(375, 425, text="Space", font="Arial 12 italic", fill="indigo")

txt = canvas.create_text(375, 300, text="Avancer", font="Arial 16 italic", fill="indigo")
txt = canvas.create_text(375, 350, text="Z", font="Arial 16 italic", fill="indigo")
rectangle1 = canvas.create_rectangle(350,325,400,375,)

txt = canvas.create_text(475, 390, text="Tourner à droite", font="Arial 12 italic", fill="indigo")
txt = canvas.create_text(475, 420, text="D", font="Arial 16 italic", fill="indigo")
rectangle2 = canvas.create_rectangle(450,400,500,450,)

txt = canvas.create_text(375, 545, text="Reculer", font="Arial 16 italic", fill="indigo")
txt = canvas.create_text(375, 500, text="S", font="Arial 16 italic", fill="indigo")
rectangle3 = canvas.create_rectangle(350,475,400,525,)

txt = canvas.create_text(275, 390, text="Tourner à gauche", font="Arial 12 italic", fill="indigo")
txt = canvas.create_text(275, 420, text="Q", font="Arial 16 italic", fill="indigo")
rectangle4 = canvas.create_rectangle(250,400,300,450,)

txt = canvas.create_text(475, 310, text="Lever le bras", font="Arial 12 italic", fill="indigo")
txt = canvas.create_text(475, 350, text="E", font="Arial 16 italic", fill="indigo")
rectangle5 = canvas.create_rectangle(450,325,500,375,)

txt = canvas.create_text(275, 310, text="Baisser le bras", font="Arial 12 italic", fill="indigo")
txt = canvas.create_text(275, 350, text="A", font="Arial 16 italic", fill="indigo")
rectangle6 = canvas.create_rectangle(250,325,300,375,)


txt = canvas.create_text(350, 100, text="Manette de controle du robot", font="Arial 38 italic", fill="indigo")
ligne = canvas.create_line(20,130,680,130,fill="indigo",width=5) 
# coordonnées initiales
coords = (350, 400)
# création du rectangle
rectangle = canvas.create_rectangle(350,400,400,450,fill="black")
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()
fenetre.mainloop()

