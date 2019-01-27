from library import compteur_elements, ecriture_hastags

fichier_markdown = open("markdown.md", "r")
fichier_index = open("index.html", "w")

markdown = []
texte_pur = []

index = []

# Variable stockant la ligne qui est entrain d'être traitée
ligne_en_cours = 0

compteur = 0

compteur_lettre = 0

for ligne in fichier_markdown:
    markdown.append(ligne)   

print(len(markdown[compteur]))

while ligne_en_cours < len(markdown):
    hashtags = []
    etoiles = []
    tirets = []
    print("Analyse et conversion de la ligne :", ligne_en_cours + 1)
    for lettre in markdown[compteur]:
        compteur_elements(lettre, hashtags, etoiles, tirets)
    print("Nombre de hashtags :", hashtags)
    print("Nombre de d'étoiles :", etoiles)
    print("Nombre de tirets :", tirets)
    compteur += 1
    ecriture_hastags(fichier_index, hashtags, markdown, ligne_en_cours)
    ligne_en_cours += 1

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