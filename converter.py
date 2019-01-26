from library import compteur_elements

fichier_markdown = open("markdown.md", "r")
fichier_index = open("index.html", "w")

markdown = []
index = []

hashtags = []
etoiles = []
tirets = []

compteur = 0

for ligne in fichier_markdown:
    markdown.append(ligne)

for lettre in markdown[compteur]:
    compteur += 1
    compteur_elements(lettre, hashtags, etoiles, tirets)    


'''         
for lettres in markdown:
    fichier_index.write("<h1>")
    fichier_index.write(lettres)
    fichier_index.write("</h1>")
'''

# Affichage du nombre de lignes du fichier markdown
print("Nombre de lignes du fichier .md :", len(markdown))

# Verification de la lecture du fichier markdown
print("La liste :\n", markdown)

print("Nombre de hashtags :\n", hashtags)

print("Nombre de etoiles :\n", etoiles)

print("Nombre de tirets :\n", tirets)