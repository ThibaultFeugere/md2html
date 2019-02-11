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
        
def ecriture_head(fichier_index, markdown, hashtags, ligne_en_cours, alphabet):
    if len(hashtags) == 1 and alphabet[0] == "#":
        fichier_index.write("<h1>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h1>")
    elif len(hashtags) == 2 and alphabet[1] == "#":
        fichier_index.write("<h2>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h2>")
    elif len(hashtags) == 3 and alphabet[2] == "#":
        fichier_index.write("<h3>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h3>")
    elif len(hashtags) == 4 and alphabet[3] == "#":
        fichier_index.write("<h4>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h4>")
    elif len(hashtags) == 5 and alphabet[4] == "#":
        fichier_index.write("<h5>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h5>")
    elif len(hashtags) == 6 and alphabet[5] == "#":
        fichier_index.write("<h6>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</h6>")

def ecriture_list(fichier_index, markdown, ligne_en_cours, alphabet):
    if alphabet[0] == "*" and alphabet[1] == " " and alphabet[-1] != "*":
        fichier_index.write("<ul>")
        fichier_index.write("<li>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</li>")
        fichier_index.write("</ul>")
    elif alphabet[0] == "-" and alphabet[1] == " ":
        fichier_index.write("<ul>")
        fichier_index.write("<li>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</li>")
        fichier_index.write("</ul>")
    elif alphabet[0] == "+" and alphabet[1] == " ":
        fichier_index.write("<ul>")
        fichier_index.write("<li>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</li>")
        fichier_index.write("</ul>")


def ecriture_hr(fichier_index, markdown, ligne_en_cours, alphabet):
    if alphabet[0] == "-" and alphabet[1] == "-" and alphabet[2] == "-":
        fichier_index.write("<hr>")

def ecriture_italic(fichier_index, markdown, ligne_en_cours, alphabet):
    if alphabet[0] == "*":
        if alphabet[-1] == "*" or alphabet[-2] == "*":
            fichier_index.write("<i>")
            fichier_index.write(markdown[ligne_en_cours])
            fichier_index.write("</i>")

def ecriture_bold(fichier_index, markdown, ligne_en_cours, alphabet):
    if alphabet[0] == "*" and alphabet[1] == "*":
        fichier_index.write("<strong>")
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</strong>")

def ecriture_url(fichier_index, markdown, ligne_en_cours, alphabet):
    if "http://" in markdown[ligne_en_cours]:
        fichier_index.write('<a href="')
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write('">')
        fichier_index.write(markdown[ligne_en_cours])
        fichier_index.write("</a>")

def finalistation(fichier_index):
    fichier_index.write('''<footer style="color:grey; font-family: roboto; font-size: 22px;">
        Script python développé par Thibault Feugère.
    </footer>
</body>
</html>''')