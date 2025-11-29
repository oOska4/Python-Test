def czyPalindrom(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x) - i - 1]:
            return False
        return True

def main():
    x = input("Podaj liczbę: ")
    print(f"Liczba {x} jest palindromem " if czyPalindrom(x) else f"Liczba {x} nie jest palindromem ")
    


if __name__ == "__main__":
    main()
