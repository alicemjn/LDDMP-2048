import tkinter as tk

grille = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

def afficher(grille):
    # afficher la matrice dans le terminal
    for line in grille:
        print(line)
    # afficher la matrice dans la fenetre tkinter
    btn1.config(text=grille[0][0])
    btn2.config(text=grille[0][1])
    btn3.config(text=grille[0][2])
    btn4.config(text=grille[0][3])
    btn5.config(text=grille[1][0])
    btn6.config(text=grille[1][1])
    btn7.config(text=grille[1][2])
    btn8.config(text=grille[1][3])
    btn9.config(text=grille[2][0])
    btn10.config(text=grille[2][1])
    btn11.config(text=grille[2][2])
    btn12.config(text=grille[2][3])
    btn13.config(text=grille[3][0])
    btn14.config(text=grille[3][1])
    btn15.config(text=grille[3][2])
    btn16.config(text=grille[3][3])
racine = tk.Tk()
racine.title('2048')

HEIGHT = 410
WIDTH = 410

canva=tk.Canvas(racine,bg='#cbc0b5',height=HEIGHT, width=WIDTH)
canva.place(x=0,y=0)

btn1 = tk.Label(racine, text="",)
btn2 = tk.Label(racine, text="")
btn3 = tk.Label(racine, text="")
btn4 = tk.Label(racine, text="")
btn5 = tk.Label(racine, text="")
btn6 = tk.Label(racine, text="")
btn7 = tk.Label(racine, text="")
btn8 = tk.Label(racine, text="")
btn9 = tk.Label(racine, text="",)
btn10 = tk.Label(racine, text="")
btn11 = tk.Label(racine, text="")
btn12 = tk.Label(racine, text="")
btn13 = tk.Label(racine, text="")
btn14 = tk.Label(racine, text="")
btn15 = tk.Label(racine, text="")
btn16 = tk.Label(racine, text="")

btn1.place(x=10, y=10, height=90,width=90)
btn2.place(x=110,y=10,height=90,width=90)
btn3.place(x=210, y=10, height=90,width=90)
btn4.place(x=310,y=10,height=90,width=90)
btn5.place(x=10,y=110,height=90,width=90)
btn6.place(x=110,y=110,height=90,width=90)
btn7.place(x=210,y=110,height=90,width=90)
btn8.place(x=310,y=110,height=90,width=90)
btn9.place(x=10, y=210, height=90,width=90)
btn10.place(x=110,y=210,height=90,width=90)
btn11.place(x=210, y=210, height=90,width=90)
btn12.place(x=310,y=210,height=90,width=90)
btn13.place(x=10,y=310,height=90,width=90)
btn14.place(x=110,y=310,height=90,width=90)
btn15.place(x=210,y=310,height=90,width=90)
btn16.place(x=310,y=310,height=90,width=90)

afficher(grille)

racine.mainloop()