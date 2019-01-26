def compteur_elements(lettre, hashtags, etoiles, tirets):
    if lettre == "#":
        hashtags.append(lettre)
    if lettre == "*":
        etoiles.append(lettre)
    if lettre == "-":
        tirets.append(lettre)