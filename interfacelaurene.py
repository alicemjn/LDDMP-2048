import tkinter as tk 

HEIGHT = 800
WIDTH = 800

ROW=4
COLUMN=4

largeur_case = HEIGHT // ROW
hauteur_case = HEIGHT // COLUMN

tk.root=tk.Tk()
tk.root.title("2048")
tk.canvas=tk.Canvas(tk.root,bg="wheat2",height=HEIGHT, width=WIDTH)
tk.root.mainloop()
