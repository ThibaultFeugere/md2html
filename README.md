# Markdown2HTML - Thibault Feugère
A little script in Python to convert a file.md in index.html.

## Interface en ligne de commande

* `-i ./un_fichier` ou `--input-directory ./un_fichier` : le chemin du fichier à convertir
* `-o ./un_fichier` ou `--output-directory ./au_fichier` : le chemin du fichier à créer en .html
  * si le dossier existe déjà, libre à vous de soit l'effacer, soit écrire dedans pour faire des mises à jours (cela sera expliqué dans le mode d'emploi de votre outil)
  * vous pouvez choisir la convention de nommage qui vous plaît pour les fichiers générés, par exemple vous pouvez utiliser comme préfixe le nom du fichier markdown correspondant (cela sera aussi expliqué)
* `-t ./autre_dossier` ou `--template-directory ./autre_dossier` : éventuellement le dossier contenant des modèles de pages web à compléter
* `-h` ou `--help` : pour afficher de l'aide pour exliquer les paramètres de la commande

## Avancement du projet :

# Checklist

| Élément à vérifier                             | Barême |
| ---------------------------------------------- | ------ |
| Implication                                    | FAIT      |
| Qualité du README.md                           | FAIT      |
| Lecture de fichiers markdown                   | FAIT      |
| Écriture de fichiers HTML                      | FAIT      |
| Utilisation de template                        | NON      |
| Support de -i ou --input-directory             | FAIT      |
| Support de -o ou --output-directory            | FAIT      |
| Support de -h ou --help                        | FAIT      |
| Conversion des #                               | FAIT      |
| Conversion des ##                              | FAIT      |
| Conversion des ###                             | FAIT      |
| Conversion des listes non ordonnées            | FAIT      |
| Conversion des URL                             | FAIT      |
| Conversion des textes importants               | FAIT      |
| Respect PEP 8                                  | FAIT      |
| Respect PEP 20                                 | FAIT      |
| Support de -i ET --input-directory             | FAIT VIA FICHIER     |
| Support de -o ET --output-directory            | FAIT VIA FICHIER     |
| Support de -k ou --kikoo-lol                   | NON     |
| Support de -a ou --achtung                     | EN COURS     |
| Robustesse aux fichiers markdown               | NON     |
| Projet open-source                             | FAIT     |
| Package sur le Python Package Index            | FAIT     |
| Utilisation des expressions régulières         | EN COURS     |
| Utilisation de packages de la communauté       | FAIT     |
| Fourniture d'un requirements.txt ou équivalent | FAIT     |

## Exemple de fichiers markdown pour la robustesse

Le fichier https://raw.githubusercontent.com/vpoulailleau/site_statique/master/robustesse.md donne, une fois interprété par GitHub, https://github.com/vpoulailleau/site_statique/blob/master/robustesse.md.

## En développement :

* `-k` ou `--kikoo-lol` qui ajoutera dans le texte des « kikoo », « lol », « mdr », « ptdr » ou qui répète des lettres comme dans Hellllo, et autres déformations du français.
* `-a` ou `--achtung` pour aider les allemands à lire nos blogs français.
* Ajout d'un système permettant d'ajouter plusieurs balises par ligne
