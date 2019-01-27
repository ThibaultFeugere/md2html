def compteur_elements(lettre, hashtags, etoiles, tirets):
    if lettre == "#":
        hashtags.append(lettre)
    if lettre == "*":
        etoiles.append(lettre)
    if lettre == "-":
        tirets.append(lettre)
        
def ecriture_hastags(fichier_index, hashtags, markdown, ligne_en_cours):
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