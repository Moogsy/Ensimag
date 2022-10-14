def insert_sort(tableau: list):
    """Tri par insertion

    - Complexité spatiale: O(1)
    - Complexité temporelle: O(n^2)

    - En place
    - Stable
    """
    for indice_limite_partie_ordonee in range(1, len(tableau)):

        indice_element_a_trier = indice_limite_partie_ordonee

        while (
            tableau[indice_element_a_trier - 1] > tableau[indice_element_a_trier]
            and indice_element_a_trier > 0
        ):

            tableau[indice_element_a_trier], tableau[indice_element_a_trier - 1] = (
                tableau[indice_element_a_trier - 1],
                tableau[indice_element_a_trier],
            )

            indice_element_a_trier -= 1


def select_sort(tableau: list[int]):
    """Tri par sélection

    - Complexité spatiale: O(1)
    - Complexité temporelle: O(n^2)

    - En place
    - Non stable
    """
    for delimiteur, _ in enumerate(tableau):
        index_local, _ = min(enumerate(tableau[delimiteur:]), key=lambda t: t[1])
        index = index_local + delimiteur

        tableau[index], tableau[delimiteur] = tableau[delimiteur], tableau[index]
