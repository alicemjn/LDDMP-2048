# Lauren Pan
import tkinter as tk

L=[[for i]]


colors = { "case": "#cbc0b5",
           "contour": "#b9ada1",
           "font": "#756e66",
           "2": "#ece4db",
           "4": "#ebe0cb",
           "8":"#e8b481",
           "16":"#e89e6c",
           "32":"#e68367",
           "64":"#e46847",
           "128":"#e8d07f",
           "256":"#e8cd72",
           "512":"#edcc61",
           "1024":"#e4c655",
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


racine.mainloop()