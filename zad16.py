def to_u2(n, bits=16):
    # opcjonalna kontrola: czy liczba się mieści w zadanej szerokości
    min_val = -2**(bits-1)
    max_val = 2**(bits-1) - 1
    if n < min_val or n > max_val:
        raise ValueError(f"n poza zakresem dla {bits} bitów: [{min_val}..{max_val}]")

    if n < 0:
        n = n + 2**bits    # dodaj 2^bits — to zamienia liczbę ujemną na reprezentację U2
        print(n)

    s = ""
    for _ in range(bits):
        s = str(n % 2) + s  # bieremy resztę z dzielenia przez 2 (LSB), doklejamy z przodu
        n //= 2             # dzielimy przez 2, przechodzimy do następnego bitu
    return s

# przykłady
print(to_u2(5, bits=16))   # -> '00000101'
print(to_u2(-5, bits=16))  # -> '11111011'

# albo calosc w 1 lini:

print("Liczba -5 w systemie u2 to: " + (lambda n,bits=16: "".join(str(((n + (0 if n>=0 else 2**bits)) // (2**i)) % 2) for i in range(bits-1, -1, -1)))(-5))

