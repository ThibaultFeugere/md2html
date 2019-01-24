from checker import hastag

fichier_markdown = open("markdown.md", "r")
fichier_index = open("index.html", "w")

markdown = []
index = []

hashtag = []

compteur = 0

for ligne in fichier_markdown:
    markdown.append(ligne)

for lettre in markdown[compteur]:
    compteur += 1
    hastag(lettre, hashtag)
   
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

# Affichage du nombre de hashtag
print("Valeur du titre :\n", hashtag)