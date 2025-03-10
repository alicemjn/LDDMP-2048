# Lauren Pan
import tkinter as tk
import random as rd

colors = { "case": "#cbc0b5",
           "contour": "#b9ada1",
           "font": "#756e66",
           "2": "#ece4db",
           "4": "#ebe0cb",
           "2048" : "#57beec"}

HEIGHT = 400
WIDTH = 400

ROW=4
COLUMN=4

largeur_case = HEIGHT // ROW
hauteur_case = HEIGHT // COLUMN

racine= tk.Tk()
racine.title("2048")

canvas = tk.Frame(racine,bg=colors["case"], height=HEIGHT, width=WIDTH)
canvas.grid(row=0, column=0)

bloc=tk.Frame(canvas,bg=colors["2"],height=largeur_case, width=hauteur_case)
bloc.place(x=(rd.randint(0,3))*100,y=(rd.randint(0,3))*100)

racine.mainloop()