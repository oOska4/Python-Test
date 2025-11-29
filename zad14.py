def na_dec(x, s):
    cyfry = "0123456789ABCDEF"
    x = x.upper()
    wynik = 0
    for c in x:
        wynik = wynik * s + cyfry.index(c)
    return wynik

def z_dec(x, s):
    cyfry = "0123456789ABCDEF"
    wynik = ""
    while x > 0:
        wynik = cyfry[x % s] + wynik
        x //= s
    return wynik if wynik else "0"

def main():
    x = input("Podaj liczbę: ")
    s1 = int(input("Podaj system wejściowy: "))
    s2 = int(input("Podaj system docelowy: "))

    dec = na_dec(x, s1)
    wynik = z_dec(dec, s2)

    print("Wynik:", wynik)

if __name__ == "__main__":
    main()
