from library import compteur_elements, ecriture_head

fichier_markdown = open("markdown.md", "r")
fichier_index = open("index.html", "w")

markdown = []
texte_pur = []

for ligne in fichier_markdown:
    print(ligne)
    markdown.append(ligne)
    texte_pur.append(ligne)

# Verification de la lecture du fichier markdown
print("Les lignes :\n", markdown)
print("Les lignes pures :\n", texte_pur)

index = []

# Variable stockant la ligne qui est entrain d'être traitée
ligne_en_cours = 0

compteur = 0

while ligne_en_cours < len(markdown):
    
    hashtags = []
    etoiles = []
    tirets = []
    
    print("Analyse et conversion de la ligne :", ligne_en_cours + 1, "\n")
    
    for lettre in markdown[compteur]:
        compteur_elements(lettre, hashtags, etoiles, tirets)
    
    print("Nombre de hashtags :", hashtags)
    print("Nombre de d'étoiles :", etoiles)
    print("Nombre de tirets :", tirets, "\n")
    
    ecriture_head(fichier_index, hashtags, markdown, ligne_en_cours)
    
    compteur += 1
    ligne_en_cours += 1

# Affichage du nombre de lignes du fichier markdown
print("Nombre de lignes du fichier .md :", len(markdown))