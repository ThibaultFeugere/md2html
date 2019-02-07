import codecs
from library import initialisation ,compteur_elements, ecriture_head, ecriture_list, ecriture_hr, ecriture_italic, ecriture_bold, finalistation

fichier_markdown = codecs.open("markdown/markdown.md", "r", "utf-8")
# W supprime le contenu du fichier avant d'écrire dedans.
fichier_index = codecs.open("html/index.html", "w", "utf-8")

# On écrit le début du code html
initialisation(fichier_index)

markdown = []
texte_pur = []

for ligne in fichier_markdown:
    print(ligne)
    suppression_hastags = ligne.replace("#", "")
    '''
    suppression_retour = ligne.replace("\n", "")
    suppression_etoiles = ligne.replace("*", "")
    suppression_plus = ligne.replace("+ ", "")
    suppression_tirets = ligne.replace("- ", "")
    '''
    markdown.append(ligne)
    texte_pur.append(suppression_hastags)
    '''
    texte_pur.append(suppression_retour)
    texte_pur.append(suppression_etoiles)
    texte_pur.append(suppression_plus)
    texte_pur.append(suppression_tirets)
    '''

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
    apostrophe_chelou = []
    plus = []
    
    print("Analyse et conversion de la ligne :", ligne_en_cours + 1, "\n")
    
    for lettre in markdown[compteur]:
        compteur_elements(lettre, hashtags, etoiles, tirets, apostrophe_chelou, plus)
    
    print("Nombre de hashtags :", hashtags)
    print("Nombre de d'étoiles :", etoiles)
    print("Nombre de tirets :", tirets)
    print("Nombre d'apostrophes chelous :", apostrophe_chelou, "\n")
    
    ecriture_head(fichier_index, hashtags, markdown, ligne_en_cours)
    ecriture_list(fichier_index, etoiles, tirets, plus, markdown, ligne_en_cours)
    ecriture_hr(fichier_index, tirets, markdown, ligne_en_cours)
    ecriture_italic(fichier_index, etoiles, markdown, ligne_en_cours)
    ecriture_bold(fichier_index, etoiles, markdown, ligne_en_cours)

    compteur += 1
    ligne_en_cours += 1

# On finalise en fermant certaines balises avec petit copyright
finalistation(fichier_index)

# Affichage du nombre de lignes du fichier markdown
print("Nombre de lignes du fichier .md :", len(markdown))
