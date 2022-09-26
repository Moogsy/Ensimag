import rotx

nom_fichier = input("Entrez un nom de fichier: ")
nom = "Thibault"

with open(nom_fichier, "w", encoding="utf-8") as f:
    print(*map(rotx.rot13, "nirPrfne"), file=f, sep='')
    print(*[rotx.rot(4, lettre) for lettre in nom], sep='', file=f)
