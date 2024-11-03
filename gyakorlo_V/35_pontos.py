# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147

def utolso_x_szo(string, n):
    if not isinstance(string, str) or not isinstance(n, int) \
            or n <= 0 or any(char in string for char in "!.,?"):
        return '-'
    szavaklista = string.strip().split(' ')  # maybe strip unncecssary
    if n > len(szavaklista):
        return '-'
    ujlista = szavaklista[-n:]
    ujlista[0] = ujlista[0].capitalize()
    retstr = ' '.join(ujlista)
    return retstr + '.'


print(utolso_x_szo('ĂŠn vagyok a legnagyobb rajongĂłd', 3))
# Return: 'A legnagyobb rajongĂłd.'
print(utolso_x_szo('vigyĂĄzni kell magamra, nincs b terv!', 4))
# Return: '-'
print(utolso_x_szo('na most figyeld Ăścsikesz, azarĂĄt metriosz-zintosz', 2))
# Return: '-'

print(utolso_x_szo('-1 na most figyeld Ăścsikesz, azarĂĄt metriosz-zintosz', -1))
print(utolso_x_szo(' 0 na most figyeld Ăścsikesz, azarĂĄt metriosz-zintosz', 0))


def karakter_modusz(string):
    if not isinstance(string, str) or len(string.split()) == 0 or "uwu" in string:
        return {"hibas": -1}
    found_chars_dict = {}
    for char in string:
        if char not in " \r\f\t\n\0":
            if char in found_chars_dict:
                found_chars_dict[char] += 1
            else:
                found_chars_dict[char] = 1
    if not found_chars_dict:
        return {"hibas": -1}

    most_common_char = max(found_chars_dict, key=found_chars_dict.get)

    return {most_common_char: found_chars_dict[most_common_char]}


class Cipo:
    def __init__(self, marka, meret, _ar=10000):
        self_ar = _ar
        self.marka = marka
        self.meret = meret
        self.matricak = []
        self.teljes_matricanevek = []
        if isinstance(_ar, int | float):
            self._ar = _ar
            self._ar = min(0, _ar)
        else:
            self._ar = 10000

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self, uj_ar):
        if isinstance(uj_ar, (int, float)):
            self._ar = max(0, uj_ar)
        else:
            self._ar = 10000

    def matrica_hozzaadas(self, szoveg):
        if not isinstance(szoveg, str):
            raise ValueError("Hibas matrica!")
        tmpstr = ''
        for i in range(0, len(szoveg), 2):
            tmpstr += szoveg[i]
        if tmpstr not in self.matricak:
            self.matricak += tmpstr

    def matrica_torles(self, szoveg):
        if not isinstance(szoveg, str):
            raise ValueError("Hibas matrica!")
        tmpstr = ''
        for i in range(0, len(szoveg), 2):
            tmpstr += szoveg[i]
        while szoveg in self.matricak:
            self.matricak.remove(szoveg)
        while tmpstr in self.matricak:
            self.matricak.remove(tmpstr)

    def __iadd__(self, other):
        if other is None or not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        self.ar = self.ar + other.ar * 1.7
        self.ar = int(self.ar)
        self.matricak.extend(other.matricak)
        return self

    def __str__(self):
        if len(self.matricak <= 0):
            return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft es meg se lett meg sertve matricakkal."
        return f"Az uj {self.marka} markaju, EU {self.meret} meretu cipo ara jelenleg {self.ar} Ft. {len(self.matricak)} db matrica van rajta.\nNev szerint: {[matrica for matrica in self.matricak]}."

    def __eq__(self, other):
        if other is None or not isinstance(other, Cipo):
            raise ValueError("Hibas tipus!")
        return self.marka == other.marka and self._ar == other._ar
#
# print(utolso_x_szo('én vagyok a legnagyobb rajongód', 3))
# print(utolso_x_szo('én vagyok az egyik fanod', 4))
# print(utolso_x_szo('Gercsó gónósz', 2))
# print(utolso_x_szo('vigyázni kell magamra, nincs b terv!', 4))
# print(utolso_x_szo('na most figyeld öcsikesz, azarát metriosz-zintosz', 2))
#
#
#
# print(karakter_modusz("aaabbc"))
# print(karakter_modusz(
#     "mondtam,                fuss el, szedd a              lábad,              jól elbújtál, nem talállak                 "))
# print(karakter_modusz("'megvárom veled a buszt uwu de csak ha szeretnéd owo'"))
#
#
# egy_cipo = Cipo("Nike", 35, 5000)
# egy_masik_cipo = Cipo("Adidas", 36, 5005)
# egy_cipo.ar = -1
# egy_masik_cipo.matrica_hozzaadas("Valami")
# egy_masik_cipo.matrica_hozzaadas("Kekw")
# egy_cipo += egy_masik_cipo
# print(egy_cipo)  # Az uj Nike markaju cipo, EU 35 meretu cipo ara jelenleg 13503 Ft. 2 db matrica van rajta.
# # Nev szerint: Valami, Kekw.
# print(egy_cipo == egy_masik_cipo)  # False