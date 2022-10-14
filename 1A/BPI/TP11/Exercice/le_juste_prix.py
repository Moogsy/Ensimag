JUSTE_PRIX = 42


def main():
    n = int(input("Prix ? "))

    while n != JUSTE_PRIX:
        if n < 0:
            print("Comment ? Vous me pensez assez tordu pour avoir choisi un prix négatif ???")
        elif n == JUSTE_PRIX:
            print("Gagné !")
        elif n < JUSTE_PRIX:
            print("Plus haut")
        else:
            print("Plus bas")



if __name__ == "__main__":
    main()
