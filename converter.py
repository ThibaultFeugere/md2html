from library import compteur_elements

fichier_markdown = open("markdown.md", "r")
fichier_index = open("index.html", "w")

markdown = []
texte_pur = []

index = []

# Variable stockant la ligne qui est entrain d'être traitée
ligne = 0

hashtags = []
etoiles = []
tirets = []

compteur = 0

for ligne in fichier_markdown:
    markdown.append(ligne)

for lettre in markdown[compteur]:
    compteur_elements(lettre, hashtags, etoiles, tirets)    

while ligne <= len(markdown):
    if len(hashtags) == 1:
        fichier_index.write("<h1>")
        fichier_index.write(texte_pur[ligne])
        fichier_index.write("</h1>")
    elif len(hashtags) == 2:
        fichier_index.write("<h2>")
        fichier_index.write(texte_pur[ligne])
        fichier_index.write("</h2>")
    elif len(hashtags) == 3:
        fichier_index.write("<h3>")
        fichier_index.write(texte_pur[ligne])
        fichier_index.write("</h3>")
    elif len(hashtags) == 4:
        fichier_index.write("<h4>")
        fichier_index.write(texte_pur[ligne])
        fichier_index.write("</h4>")
    elif len(hashtags) == 5:
        fichier_index.write("<h5>")
        fichier_index.write(texte_pur[ligne])
        fichier_index.write("</h5>")
    elif len(hashtags) == 6:
        fichier_index.write("<h6>")
        fichier_index.write(texte_pur[ligne])
        fichier_index.write("</h6>")

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