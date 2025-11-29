def z_dec(x, s):
    wynik = ""
    while x > 0:
        wynik = str(x % s) + wynik
        x //= s
    return wynik if wynik != "" else "0"

def main():
    x = int(input("Podaj liczbę dziesiętną: "))
    s = int(input("Podaj system (2–9): "))
    print("Wynik:", z_dec(x, s))

if __name__ == "__main__":
    main()
