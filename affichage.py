
def police(valeur):
    if valeur < 1024:
        return 30    
    elif valeur < 10000:
        return 24
    else:
        return 20



def affichage(grille, labels, pack):
    LEN = len(grille)
    #met à jour les valeurs (text) prises par les cases de la grille, et leur associe une couleur en appelant la fonction color_case
    for i in range(LEN):
        for j in range(LEN):
            value = grille[i][j]
            labels[(i, j)].config(text=str(value) if value != 0 else "", bg=color_case(int(value), pack), fg=color_case("fg_"+str(value), pack),font=('Helvetica',police(value))) 




def color_case(valeur, pack):
    if isinstance(valeur, str) :
        if valeur in globals()[pack]:
            return globals()[pack][valeur]
        else:
            return globals()[pack]["default_font"]
    else:
        if valeur in globals()[pack]:
            return globals()[pack][valeur] # retourne la couleur associée à la valeur dans le dictionnaire
        else:
            return "black" # à défaut renvoie noir (pour les grandes cases)

default = {
    ### packs de couleurs par défaut
    # bordures de la grille
    "background": "#b9ada1",
    # couleurs de la police
    "default_font": "#ffffff",
    "fg_2": "#756e66",
    "fg_4": "#756e66",
    # couleurs des cases
    0:"#cdc1b4", 2:"#eee4da" , 
    4: "#ebe0cb", 8:"#e8b481", 
    16:"#e89e6c", 32:"#e68367", 
    64:"#e46847", 128:"#e8d07f",
    256:"#e8cd72", 512:"#edcc61",
    1024:"#e4c655", 2048: "#edc22e", 
    4096: "#57beec"}

moderne = {
    ### packs de couleurs Moderne
    # bordures de la grille
    "background": "#7E5460",
    # couleurs de la police
    # couleurs de la police
    "default_font": "#FFFFFF",
    "fg_2": "#424952",
    "fg_4": "#424952",
    "fg_8": "#424952",
    "fg_256": "#424952",
    "fg_512": "#424952",
    # couleurs des cases
    0:"#997478", 2:"#FFF3E3" ,
    4: "#FFE9CB", 8:"#FFC378", 
    16:"#FFA762", 32:"#FF8357", 
    64:"#FF5F58", 128:"#BEC77D",
    256:"#94CD91", 512:"#5ACCB1",
    1024:"#00CAD7", 2048: "#03C1EF"}

billard = {
    ### packs de couleurs inspiré des couleurs des boules de billard
    # bordures de la grille
    "background": "#764423",
    # couleurs de la police
    "default_font": "#ffffff",
    "fg_2": "#000000",
    # couleurs des cases
    0:"#37a143", 2:"#f7f5e3" ,
    4: "#FDBD03", 8:"#FA0502", 
    16:"#5921A9", 32:"#FE6A00", 
    64:"#0230CD", 128:"#A60107",
    256:"#FD6F00", 512:"#090504"}

squid_game = {
    ### packs de couleurs inspiré de la série Squid Game
    # bordures de la grille
    "background": "#744832",
    # couleurs de la police
    "default_font": "#ffffff",
    # couleurs des cases
    0:"#E6AA76", 2:"#ED267A" ,
    4: "#186F68", 8:"#395A73", 
    16:"#2F9EB5", 32:"#9CAA10", 
    64:"#A4E593", 128:"#85B490",
    256:"#4B5413", 512:"#87547C",
    1024:"#BBC6D4", 2048: "#E99D0E"}

barbie = {
    ### packs de couleurs Barbie
    # bordures de la grille
    "background": "#02B9E3",
    # couleurs de la police
    "default_font": "#FFFFFF",
    # couleurs des cases
    0:"#76cde0", 2:"#F29DD9" ,
    4: "#EE75C5", 8:"#F75EBA", 
    16:"#F141B4", 32:"#E519B0", 
    64:"#E22B8D", 128:"#35554B",
    256:"#FADE9E", 512:"#E1949C",
    1024:"#9F5D4B", 2048: "#FF96C8"}

android = {
    ### packs de couleurs Android
    # bordures de la grille
    "background": "#000000",
    # couleurs de la police
    "default_font": "#FFFFFF",
    # couleurs des cases
    0:"#373737", 2:"#9601FF" ,
    4: "#F0145A", 8:"#FFC919", 
    16:"#00C418", 32:"#0095D5", 
    64:"#CE007B", 128:"#FF5418",
    256:"#28D7A5", 512:"#3C14AE",
    1024:"#FF0024", 2048: "#5F069B"}

aveugle = {
    ### packs de couleurs Aveugle
    "background": "#FFFFFF",
    "default_font": "#000000",
    0: "#FFFFFF"}