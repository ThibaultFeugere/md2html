f = open("markdown2convert.md", "r")

liste = []

for lettres in f:
    liste.append(lettres)

# Verification de la lecture du fichier markdown
print(liste)

# Affichage du nombre de lignes du fichier markdown
print(len(liste))