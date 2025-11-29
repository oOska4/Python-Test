def Ekl(x, y):
    """Największy wspólny dzielnik (algorytm Euklidesa). Działa dla x,y>=0"""
    x, y = abs(x), abs(y)
    while y != 0:
        x, y = y, x % y
    return x

def skracaj(licz, mian):
    """Zwraca skrócony (licz, mian) z zachowaniem znaku w liczniku."""
    if mian == 0:
        raise ZeroDivisionError("Mianownik nie może być 0.")
    if licz == 0:
        return 0, 1
    sign = -1 if (licz * mian) < 0 else 1
    licz, mian = abs(licz), abs(mian)
    g = Ekl(licz, mian)
    return sign * (licz // g), mian // g

def dodaj(l1, m1, l2, m2):
    num = l1 * m2 + l2 * m1
    den = m1 * m2
    return num, den

def odejmij(l1, m1, l2, m2):
    num = l1 * m2 - l2 * m1
    den = m1 * m2
    return num, den

def mnoz(l1, m1, l2, m2):
    num = l1 * l2
    den = m1 * m2
    return num, den

def dziel(l1, m1, l2, m2):
    if l2 == 0:
        raise ZeroDivisionError("Nie można dzielić przez ułamek o liczniku 0.")
    num = l1 * m2
    den = m1 * l2
    # poprawiamy znak tak, żeby mianownik był dodatni
    if den < 0:
        num, den = -num, -den
    return num, den

def pokaz(licz, mian):
    """Zwraca łańcuch z ułamkiem nieskróconym i skróconym"""
    try:
        sk_l, sk_m = skracaj(licz, mian)
    except ZeroDivisionError:
        return "Błąd: mianownik 0"
    return f"{licz}/{mian}  =  {sk_l}/{sk_m}"

def czytaj_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Podaj liczbę całkowitą.")

def main():
    print("Program działa na dwóch ułamkach zwykłych.")
    print("Podaj 4 liczby całkowite: licz_1, mian_1, licz_2, mian_2")
    l1 = czytaj_int("licz_1: ")
    m1 = czytaj_int("mian_1: ")
    l2 = czytaj_int("licz_2: ")
    m2 = czytaj_int("mian_2: ")

    if m1 == 0 or m2 == 0:
        print("Błąd: mianownik nie może być 0.")
        return

    print("\nUłamki:")
    print("Pierwszy ->", pokaz(l1, m1))
    print("Drugi   ->", pokaz(l2, m2))

    # suma
    s_num, s_den = dodaj(l1, m1, l2, m2)
    print("\nSuma:   ", pokaz(s_num, s_den))

    # różnica
    r_num, r_den = odejmij(l1, m1, l2, m2)
    print("Różnica:", pokaz(r_num, r_den))

    # iloczyn
    p_num, p_den = mnoz(l1, m1, l2, m2)
    print("Iloczyn:", pokaz(p_num, p_den))

    # iloraz
    try:
        q_num, q_den = dziel(l1, m1, l2, m2)
        print("Iloraz: ", pokaz(q_num, q_den))
    except ZeroDivisionError as e:
        print("Iloraz: Błąd —", e)

if __name__ == "__main__":
    main()
