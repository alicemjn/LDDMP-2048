def affichage(grille, labels):
    LEN = len(grille)
    #met à jour les valeurs (text) prises par les cases de la grille, et leur associe une couleur en appelant la fonction color_case
    for i in range(LEN):
        for j in range(LEN):
            value = grille[i][j]
            labels[(i, j)].config(text=str(value) if value != 0 else "", bg=color_case(int(value)), fg=color_case("fg_"+str(value)))  #si value est égale à 0, aucun texte n'est affiché

def color_case(valeur):
    if isinstance(valeur, str) :
        if int(valeur.split('_')[1]) > 4: return "#ffffff"
        else: return "#756e66"
    else:
        colors = {
            # couleurs des cases
            0:"#cdc1b4", 2:"#eee4da" , 
            4: "#ebe0cb", 8:"#e8b481", 
            16:"#e89e6c", 32:"#e68367", 
            64:"#e46847", 128:"#e8d07f",
            256:"#e8cd72", 512:"#edcc61",
            1024:"#e4c655", 2048: "#edc22e", 
            4096: "#57beec"}
        return colors.get(valeur) #retourne la couleur associée à la valeur dans le dictionnaire
