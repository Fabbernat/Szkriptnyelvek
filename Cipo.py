# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147


def utolso_x_szo(string, number):
    if not isinstance(string, str) or not isinstance(number, int) or number < 1 or any(
            char in string for char in "!.,?"):
        return "-"
    lista = string.split()
    if len(lista) < number:
        return "-"
    ujlista = lista[-number:]
    ujlista[0] = ujlista[0].capitalize()
    retstr = " ".join(ujlista) + "."
    return retstr


print(utolso_x_szo('én vagyok a legnagyobb rajongód', 3))
print(utolso_x_szo('én vagyok az egyik fanod', 4))
print(utolso_x_szo('Gercsó gónósz', 2))
print(utolso_x_szo('vigyázni kell magamra, nincs b terv!', 4))
print(utolso_x_szo('na most figyeld öcsikesz, azarát metriosz-zintosz', 2))


def karakter_modusz(string):
    if not isinstance(string, str) or len(string.split()) == 0 or not string.split() or "uwu" in string:
        return {"hibas": -1}
    found_chars_dict = {}
    for char in string:
        if char not in " \r\f\t\n":
            if char in found_chars_dict:
                found_chars_dict[char] += 1
            else:
                found_chars_dict[char] = 1

    if not found_chars_dict:
        return {"hibas": -1}

    most_common_char = max(found_chars_dict, key=found_chars_dict.get)

    return {most_common_char: found_chars_dict[most_common_char]}


print(karakter_modusz("aaabbc"))
print(karakter_modusz(
    "mondtam,                fuss el, szedd a              lábad,              jól elbújtál, nem talállak                 "))
print(karakter_modusz("'megvárom veled a buszt uwu de csak ha szeretnéd owo'"))


class Cipo:

    def __init__(self, marka, meret, _ar=10000):
        self._ar = _ar
        self.marka = marka
        self.meret = meret
        self.matricak = []
        self.teljes_matricanevek = []
        if self._ar < 1:
            self._ar = 10000

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self, ar):
        if isinstance(ar, (int, float)):
            if ar > 0:
                self._ar = ar
            else:
                self._ar = 10000
        else:
            raise ValueError("Hibas ar!")

    def matrica_hozzaadas(self, hozzaadando_nev):
        if not isinstance(hozzaadando_nev, str):
            raise ValueError("Hibas matrica!")
        feldolgozott_matrica = hozzaadando_nev[::2]
        if feldolgozott_matrica not in self.matricak:
            self.teljes_matricanevek.append(hozzaadando_nev)
            self.matricak.append(feldolgozott_matrica)

    def matrica_torles(self, torlendo_nev):
        if not isinstance(torlendo_nev, str):
            raise ValueError("Hibas matrica!")

        feldolgozott_matrica = torlendo_nev[::2]
        if feldolgozott_matrica in self.matricak:
            # Visszafelé haladunk a listában, hogy biztonságosan törölhessük az elemeket
            for i in range(len(self.matricak) - 1, -1, -1):
                if self.matricak[i] == feldolgozott_matrica:
                    del self.teljes_matricanevek[i]
                    del self.matricak[i]
                    break
        else:
            raise ValueError("A matrica nincs a cipon.")

    def __str__(self):
        if len(self.teljes_matricanevek) <= 0:
            return f"Az uj {self.marka} markaju, EU {self.meret}meretu cipo ara jelenleg {self._ar} Ft es meg se lett meg sertve matricakkal."
        else:
            kiirando = ", ".join(map(str, self.teljes_matricanevek))
            return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft. {len(self.teljes_matricanevek)} db matrica van rajta.\nNev szerint: {kiirando}."

    def __iadd__(self, other):
        if other is None or not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        for matrica in other.matricak:
            if matrica not in self.matricak:
                self.teljes_matricanevek.append(matrica)
                self.matricak.append(matrica)
        self.ar += int(other.ar * 0.7)
        return self

    def __eq__(self, other):
        if other is None or not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        else:
            return self.marka == other.marka and self._ar == other._ar


egy_cipo = Cipo("Nike", 35, 5000)
egy_masik_cipo = Cipo("Adidas", 36, 5005)
egy_cipo.ar = -1
egy_masik_cipo.matrica_hozzaadas("Valami")
egy_masik_cipo.matrica_hozzaadas("Kekw")
egy_cipo += egy_masik_cipo
print(egy_cipo)  # Az uj Nike markaju cipo, EU 35 meretu cipo ara jelenleg 13503 Ft. 2 db matrica van rajta.
# Nev szerint: Valami, Kekw.
print(egy_cipo == egy_masik_cipo)  # False