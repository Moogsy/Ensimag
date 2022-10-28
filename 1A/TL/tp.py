#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP TL1: implémentation des automates
"""

import sys

###############
# Cadre général

V = set((".", "e", "E", "+", "-") + tuple(str(i) for i in range(10)))


class Error(Exception):
    pass


INPUT_STREAM = sys.stdin
END = "\n"  # WARNING: test_tp modifies the value of END.

# Initialisation: on vérifie que END n'est pas dans V
def init_char():
    if END in V:
        raise Error("character " + repr(END) + " in V")


# Accès au caractère suivant dans l'entrée
def next_char():
    global INPUT_STREAM
    ch = INPUT_STREAM.read(1)
    # print("@", repr(ch))  # decommenting this line may help debugging
    if ch in V or ch == END:
        return ch
    raise Error("character " + repr(ch) + " unsupported")


############
# Question 1 : fonctions nonzerodigit et digit


def nonzerodigit(char):
    assert len(char) <= 1
    return "1" <= char <= "9"


def digit(char):
    assert len(char) <= 1
    return "0" <= char <= "9"

def digitzero(char):
    return digit(char) and not nonzerodigit(char)

############
# Question 2 : integer et pointfloat sans valeur


def integer_Q2():
    init_char()

    first = next_char()

    if first == END or not digit(first):
        return False

    elif digitzero(first):
        return integer_Q2_state_0()
    else:
        return integer_Q2_state_1()


def integer_Q2_state_0():
    while (char := next_char()) != END:
        if not digitzero(char):
            return False

    return True
 

def integer_Q2_state_1():
    while (char := next_char()) != END:
        if not digit(char):
            return False

    return True


def pointfloat_Q2():
    init_char()

    first = next_char()

    if first == ".":
        is_single_dot = True
        while (nxt := next_char()) != END:
            is_single_dot = False
            if not digit(nxt):
                return False
        else:
            return not is_single_dot

    elif digit(first):

        while (nxt := next_char()) != END:
            if not digit(nxt):
                if nxt == ".":
                    break
                else:
                    return False
        else:
            return False

        while (nxt := next_char()) != END:
            if not digit(nxt):
                return False

        return True

    else:
        return False


# Définir ici les fonctions manquantes


############
# Question 5 : integer avec calcul de la valeur
# si mot accepté, renvoyer (True, valeur)
# si mot refusé, renvoyer (False, None)

# Variables globales pour se transmettre les valeurs entre états
int_value = 0
exp_value = 0


def integer():
    return integer_state_0()
    

def integer_state_0():
    ch = next_char()

    if not digit(ch) or ch == END:
        return (False, None)

    if nonzerodigit(ch):
        is_integer, intvr = integer_state_2()
    else:
        is_integer, intvr = integer_state_1()

    if is_integer:
        intv = int(ch + intvr)
    else:
        intv = None

    global int_value
    int_value = intv

    return (is_integer, int_value)


def integer_state_1():
    while (ch := next_char()) != END:
        if not digitzero(ch):
            return (False, None)

    return (True, "")


def integer_state_2():
    int_value = ""

    while (ch := next_char()) != END:
        if digit(ch):
            int_value += ch
        else:
            return (False, None)

    return (True, int_value)

############
# Question 7 : pointfloat avec calcul de la valeur


def pointfloat():
    global int_value
    global exp_value
    init_char()
    int_value = 0.0
    exp_value = 0
    return pointfloat_state_0()


# Définir ici les fonctions manquantes
def pointfloat_state_0():
    intv = ""

    ch = next_char()

    if ch == ".":
        return pointfloat_state_1()

    elif digit(ch):
        return pointfloat_state_2()

    else:
        return (False, None)


def pointfloat_state_1():
    pass

def pointfloat_state_2():
    pass

# Question 8 : exponent, exponentfloat et number

# La valeur du signe de l'exposant : 1 si +, -1 si -
sign_value = 0


########################
#####    Projet    #####
########################


V = set(
    (".", "e", "E", "+", "-", "*", "/", "(", ")", " ")
    + tuple(str(i) for i in range(10))
)


############
# Question 10 : eval_exp


def eval_exp():
    print("@ATTENTION: eval_exp à finir !")  # LIGNE A SUPPRIMER
    ch = next_char()
    if ch == "+":
        n1 = eval_exp()
        n2 = eval_exp()
        return n1 + n2


############
# Question 12 : eval_exp corrigé

current_char = ""

# Accès au caractère suivant de l'entrée sans avancer
def peek_char():
    global current_char
    if current_char == "":
        current_char = INPUT_STREAM.read(1)
    ch = current_char
    # print("@", repr(ch))  # decommenting this line may help debugging
    if ch in V or ch in END:
        return ch
    raise Error("character " + repr(ch) + " unsupported")


def consume_char():
    global current_char
    current_char = ""


def number_v2():
    print("@ATTENTION: number_v2 à finir !")  # LIGNE A SUPPRIMER


def eval_exp_v2():
    print("@ATTENTION: eval_exp_v2 à finir !")  # LIGNE A SUPPRIMER


############
# Question 14 : automate pour Lex

operator = set(["+", "-", "*", "/"])


def FA_Lex():
    print("@ATTENTION: FA_lex à finir !")  # LIGNE A SUPPRIMER


############
# Question 15 : automate pour Lex avec token

# Token
NUM, ADD, SOUS, MUL, DIV, OPAR, FPAR = range(7)
token_value = 0


def FA_Lex_w_token():
    print("@ATTENTION: FA_lex_w_token à finir !")  # LIGNE A SUPPRIMER


# Fonction de test
if __name__ == "__main__":
    print("@ Test interactif de l'automate")
    print(
        "@ Vous pouvez changer l'automate testé en modifiant la fonction appelée à la ligne 'ok = ... '."
    )
    print("@ Tapez une entrée:")
    try:
        # ok = pointfloat_Q2()  # changer ici pour tester un autre automate sans valeur
        ok, val = integer() # changer ici pour tester un autre automate avec valeur
        # ok, val = True, eval_exp() # changer ici pour tester eval_exp et eval_exp_v2
        if ok:
            print("Accepted!")
            print("value:", val) # décommenter ici pour afficher la valeur (question 4 et +)
        else:
            print("Rejected!")
            print("value so far:", int_value) # décommenter ici pour afficher la valeur en cas de rejet
    except Error as e:
        print("Error:", e)
