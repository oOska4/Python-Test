def na_dec(x, s):
    cyfry = "0123456789ABCDEF"
    x = x.upper()
    wynik = 0
    for cyfra in x:
        wynik = wynik * s + cyfry.index(cyfra)
    return wynik

def main():
    x = input("Podaj liczbę w systemie s: ")
    s = int(input("Podaj system (2–16): "))
    print("Wynik:", na_dec(x, s))

if __name__ == "__main__":
    main()
