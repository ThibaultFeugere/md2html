import codecs
import argparse
from library import initialisation ,compteur_elements, ecriture_head, ecriture_list, ecriture_hr, ecriture_italic, ecriture_bold, ecriture_url, finalistation

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input-directory", required="True", help="directory d'entrée", metavar="")
parser.add_argument("-o", "--output-directory", required="True", help="directory de sortie", metavar="")
parser.add_argument("-k", "--kikoo-lol", help="Pour les kikoos geek", metavar="")
parser.add_argument("-a", "--achtung", help="Pour nos amis les allemands", metavar="")

parser.parse_args()

markdown_folder = parser.parse_args().input_directory
html_folder = parser.parse_args().output_directory

fichier_markdown = codecs.open(markdown_folder, "r", "utf-8")
# W supprime le contenu du fichier avant d'écrire dedans.
fichier_index = codecs.open(html_folder, "w", "utf-8")

# On écrit le début du code html
initialisation(fichier_index)

markdown = []
texte_pur = []

n = 0

for ligne in fichier_markdown:
    print(ligne)
    markdown.append(ligne)

# Verification de la lecture du fichier markdown
print("Les lignes :\n", markdown)
print("Les lignes pures :\n", texte_pur)

index = []

# Variable stockant la ligne qui est entrain d'être traitée
ligne_en_cours = 0

compteur = 0

while ligne_en_cours < len(markdown):
    
    alphabet = []

    hashtags = []
    etoiles = []
    tirets = []
    apostrophe_chelou = []
    plus = []
    
    print("Analyse et conversion de la ligne :", ligne_en_cours + 1, "\n")
    
    for lettre in markdown[compteur]:
        if lettre != "\n":
            alphabet.append(lettre)
        else:
            alphabet.append(" ")
        compteur_elements(lettre, hashtags, etoiles, tirets, apostrophe_chelou, plus)
    
    print("Nombre de hashtags :", hashtags)
    print("Nombre de d'étoiles :", etoiles)
    print("Nombre de tirets :", tirets)
    print("Nombre de plus :", plus)
    print("Nombre d'apostrophes chelous :", apostrophe_chelou, "\n")

    print("Les lettres de cette ligne sont :", alphabet)
    print(alphabet[2:-1])
    
    ecriture_head(fichier_index, markdown, hashtags, ligne_en_cours, alphabet)
    ecriture_list(fichier_index, markdown, ligne_en_cours, alphabet)
    ecriture_hr(fichier_index, markdown, ligne_en_cours, alphabet)
    ecriture_italic(fichier_index, markdown, ligne_en_cours, alphabet)
    ecriture_bold(fichier_index, markdown, ligne_en_cours, alphabet)
    ecriture_url(fichier_index, markdown, ligne_en_cours, alphabet)

    compteur += 1
    ligne_en_cours += 1

# On finalise en fermant certaines balises avec petit copyright
finalistation(fichier_index)

# Affichage du nombre de lignes du fichier markdown
print("Nombre de lignes du fichier .md :", len(markdown))