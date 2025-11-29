def z_dec(x, s):
    cyfry = "0123456789ABCDEF"
    wynik = ""
    while x > 0:
        wynik = cyfry[x % s] + wynik
        x //= s
    return wynik if wynik != "" else "0"

def main():
    x = int(input("Podaj liczbę dziesiętną: "))
    s = int(input("Podaj system (2–16): "))
    print("Wynik:", z_dec(x, s))

if __name__ == "__main__":
    main()
