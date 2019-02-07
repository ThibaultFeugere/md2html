def initialisation(fichier_index):
    fichier_index.write('''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8" />
    <title>Conversion Md2Html</title>
</head>
<body>''')

def compteur_elements(lettre, hashtags, etoiles, tirets, apostrophe_chelou, plus):
    if lettre == "#":
        hashtags.append(lettre)
    if lettre == "*":
        etoiles.append(lettre)
    if lettre == "-":
        tirets.append(lettre)
    if lettre == "`":
        apostrophe_chelou.append(lettre)
    if lettre == "+":
        plus.append(lettre)
        
def ecriture_head(fichier_index, hashtags, markdown, ligne_en_cours):
    if len(hashtags) == 1:
        fichier_index.write("<h1>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h1>")
    elif len(hashtags) == 2:
        fichier_index.write("<h2>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h2>")
    elif len(hashtags) == 3:
        fichier_index.write("<h3>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h3>")
    elif len(hashtags) == 4:
        fichier_index.write("<h4>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h4>")
    elif len(hashtags) == 5:
        fichier_index.write("<h5>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h5>")
    elif len(hashtags) == 6:
        fichier_index.write("<h6>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h6>")

def ecriture_list(fichier_index, etoiles, tirets, plus, markdown, ligne_en_cours):
    if len(etoiles) == 1:
        fichier_index.write("<ul>")
        fichier_index.write("<li>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</li>")
        fichier_index.write("</ul>")
    elif len(tirets) == 1:
        fichier_index.write("<ul>")
        fichier_index.write("<li>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</li>")
        fichier_index.write("</ul>")
    elif len(plus) == 1:
        fichier_index.write("<ul>")
        fichier_index.write("<li>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</li>")
        fichier_index.write("</ul>")


def ecriture_hr(fichier_index, tirets, markdown, ligne_en_cours):
    if len(tirets) >= 3:
        fichier_index.write("<hr>")

def ecriture_italic(fichier_index, etoiles, markdown, ligne_en_cours):
    if len(etoiles) == 2:
        fichier_index.write("<i>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</i>")

def ecriture_bold(fichier_index, etoiles, markdown, ligne_en_cours):
    if len(etoiles) == 4:
        fichier_index.write("<strong>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</strong>")

def finalistation(fichier_index):
    fichier_index.write('''<footer>
        Script python développé par Thibault Feugère.
    </footer>
</body>
</html>''')