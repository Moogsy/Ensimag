from random import randint

def main():
    attemps = 0
    n = randint(0, 100)
    guess = None

    while guess != n:
        attemps += 1
        guess = int(input("Guess a number: "))

        if guess > n:
            print("Lower")
        elif guess < n:
            print("Higher")
        else:
            print("Win !")

        if attemps > 3:
            break

if __name__ == "__main__":
    main()

