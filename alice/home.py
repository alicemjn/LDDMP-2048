import tkinter as tk

racine = tk.Tk()
racine.title('variations')

canva = tk.Canvas(racine, bg="#b9ada1", height=300, width=410, highlightthickness=0)
canva.grid(row=0, column=0, padx=0, pady=0)

standard = tk.Button(racine, text="4 x 4", font=("#756e66", 30, "bold"), bg="#eee4da", fg="white")
standard.place(x=15 , y=10, width=180, height=130)

huitxhuit = tk.Button(racine, text="8 x 8", font=("#756e66", 30, "bold"), bg="#eee4da", fg="white")
huitxhuit.place(x=215 , y=10, width=180, height=130)

custom = tk.Button(racine, text="CUSTOM", font=("#756e66", 20, "bold"), bg="#ebe0cb", fg="white")
custom.place(x=215 , y=155, width=180, height=130)

competitif = tk.Button(racine, text="COMPETITIF", font=("#756e66", 20, "bold"), bg="#ebe0cb", fg="white")
competitif.place(x=15 , y=155, width=180, height=130)

racine.mainloop()
