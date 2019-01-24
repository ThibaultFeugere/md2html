def compteur_hastag(lettre, hashtags):
    if lettre == "#":
        hashtags.append(lettre)
        
def compteur_etoile(lettre, etoiles):
    if lettre == "*":
        etoiles.append(lettre)
        
def compteur_tiret(lettre, tirets):
    if lettre == "-":
        tirets.append(lettre)