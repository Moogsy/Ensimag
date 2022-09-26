def demande_entier() -> int:
    n = input("Entrez un entier: ")
    return int(n)


a = demande_entier()
b = demande_entier()
print(f"Somme: {a + b}")
