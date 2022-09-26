def joue_coup(cases: list[int | str], symbole: str) -> int:

    while True:
        n_case = int(
            input(f"Entrez un numero de case vide pour le joueur ({symbole}): ")
        )

        if cases[n_case] not in ("x", "o"):
            return n_case
        else:
            print("Le numéro de case entré n'est pas vide.")
