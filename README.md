# Markdown2HTML - Thibault Feugère
A little script in Python to convert a file.md in index.html.

## Interface en ligne de commande

* `-i ./un_dossier` ou `--input-directory ./un_dossier` : le chemin du dossier de fichiers source (contenant les fichiers markdown)
* `-o ./un_autre_dossier` ou `--output-directory ./un_autre_dossier` : le chemin du dossier où seront mis les fichiers générés pour le site statique
  * si le dossier existe déjà, libre à vous de soit l'effacer, soit écrire dedans pour faire des mises à jours (cela sera expliqué dans le mode d'emploi de votre outil)
  * vous pouvez choisir la convention de nommage qui vous plaît pour les fichiers générés, par exemple vous pouvez utiliser comme préfixe le nom du fichier markdown correspondant (cela sera aussi expliqué)
* `-t ./autre_dossier` ou `--template-directory ./autre_dossier` : éventuellement le dossier contenant des modèles de pages web à compléter
* `-h` ou `--help` : pour afficher de l'aide pour exliquer les paramètres de la commande

Vous pouvez éventuellement ajouter des paramètres comme :
* ce que vous voulez
* `-k` ou `--kikoo-lol` qui ajoutera dans le texte des « kikoo », « lol », « mdr », « ptdr » ou qui répète des lettres comme dans Hellllo, et autres déformations du français.
* `-a` ou `--achtung` pour aider les allemands à lire nos blogs français.
