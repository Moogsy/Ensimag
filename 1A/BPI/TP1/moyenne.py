#!/usr/bin/env python3

def moyenne_notes(notes: list[tuple[int, int]]) -> float:
    moyenne = 0

    for note, coeff in notes:
        moyenne += note * coeff

    return moyenne / len(notes)


notes = [(17, 9), (15, 6), (4, 1)]

print(moyenne_notes(notes))

# Fais crash le programme, un tuple est immutable

# notes[2](1) = 2

