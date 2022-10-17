def insert_sort(tableau: list):
    """Tri par insertion

    - Complexité spatiale: O(1)
    - Complexité temporelle: O(n^2)

    - En place
    - Stable
    """
    for indice_limite_partie_ordonee in range(1, len(tableau)):

        indice_element_a_trier: int = indice_limite_partie_ordonee

        while (
            tableau[indice_element_a_trier - 1] > tableau[indice_element_a_trier]
            and indice_element_a_trier > 0
        ):

            tableau[indice_element_a_trier], tableau[indice_element_a_trier - 1] = (
                tableau[indice_element_a_trier - 1],
                tableau[indice_element_a_trier],
            )

            indice_element_a_trier -= 1


def select_sort(tableau: list[int]) -> None:
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


def merge(li_g: list[int], li_d: list[int]) -> list[int]:
    """Rassemblement de deux listes déjà triées en une seule"""
    out: list[int] = []

    if not (li_g and li_d):
        return li_g + li_d

    i = 0
    j = 0

    while i < len(li_g) and j < len(li_d):

        if li_g[i] <= li_d[j]:
            out.append(li_g[i])
            i += 1
        else:
            out.append(li_d[j])
            j += 1

    return out + li_g[i:] + li_d[j:]


def merge_sort(tableau: list[int]) -> list[int]:
    """Tri fusion

    - Complexité spatiale: O(n)
    - Complexité temporelle: O(n log(n))

    - Pas en place
    - Non stable
    """
    if len(tableau) <= 1:
        return tableau

    elif len(tableau) == 2:
        a, b = tableau

        if a <= b:
            return tableau
        else:
            return [b, a]

    else:
        milieu: int = len(tableau) // 2

        trie_g = merge_sort(tableau[:milieu])
        trie_d = merge_sort(tableau[milieu:])

        return merge(trie_g, trie_d)
