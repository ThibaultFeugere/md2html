f = open("markdown2convert.md", "r")
h = open("index.html", "w")

liste = []

compteur = 0

for lettres in f:
    liste.append(lettres)
    
for lettres in liste:
    h.write(lettres)
    
# Affichage du nombre de lignes du fichier markdown
print("Nombre de lignes du fichier .md :", len(liste))

# Verification de la lecture du fichier markdown
print("La liste :\n", liste)