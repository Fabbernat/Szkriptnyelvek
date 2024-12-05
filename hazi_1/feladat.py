# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147


def szekem(index):
    index -= 1  # atalakitas 0-based indexszĂŠ
    # tekintsÄĹşk a lelÄÄtÄĹt egy x y koordinÄÄta-rendszernek!
    x = index // 14 + 1  # megadja, hogy hanyadik sorba kaptuk a jegyet.
    y = index % 14 + 1  # 0 = legbaloldali, 13 = legjobboldali

    if y < 8:
        oldal = "jobb"
        szam = 8 - y
    else:
        oldal = "bal"
        szam = y - 7
    return f"{x}. sor, {oldal} {szam}. szek"


print(szekem(1))
print(szekem(2))
print(szekem(6))
print(szekem(7))
print(szekem(8))
print(szekem(13))
print(szekem(14))
print(szekem(21))
print(szekem(99999999999))
