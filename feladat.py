# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147


class Konyv:
    def __init__(self, _cim, _oldalszam=100):
        self._cim = _cim
        self._oldalszam = _oldalszam

    @property
    def cim(self):
        return self._cim

    @property
    def oldalszam(self):
        return self._oldalszam

    @oldalszam.setter
    def oldalszam(self, _oldalszam):
        self._oldalszam = _oldalszam


class Kategoria:
    def __init__(self, nev):
        self.nev = nev
        self.konyvek = []

    def __iadd__(self, konyv):
        if not isinstance(konyv, Konyv):
            raise TypeError('A kategóriába csak könyvek kerülhetnek!')
        if konyv.oldalszam < 100:
            raise ValueError('Csak megfelelő hosszúságú könyvek kerülhetnek be!')
        self.konyvek.append(konyv)
        return self

    def __str__(self):
        retstr = ', '.join([konyv.cim for konyv in self.konyvek])
        return retstr

    def __iter__(self):
        return iter(self.konyvek)


def kiemelkedo_konyvek(kategoriak_listaja):
    retlista = []
    for kategoria in kategoriak_listaja:
        if len(kategoria.konyvek) > 1:
            for konyv in kategoria:
                if konyv.oldalszam > 199:
                    retlista.append(konyv)
    return retlista


class SemmiNemMaradtAKonyvtarban(Exception):
    def __init__(self, message='Minden könyv kiesett.'):
        super().__init__(message)


def statisztika(list_of_tuples):
    try:
        kategoria_dict = {}
        for cim, oldalszam, kategoria in list_of_tuples:
            if oldalszam >= 100:
                if kategoria not in kategoria_dict:
                    kategoria_dict[kategoria] = Kategoria(kategoria)
                kategoria_dict[kategoria] += Konyv(cim, oldalszam)

        kiemeltek = kiemelkedo_konyvek(list(kategoria_dict.values()))
        if not kiemeltek:
            raise SemmiNemMaradtAKonyvtarban()

        return kiemeltek

    except ValueError as e:
        print(f"ValueError: {e}")


# Test for Konyvek and Kategoria

# kat = Kategoria("Fantasy")
# kat += Konyv("A Gyűrűk Ura", 450)
# kat += Konyv("Harry Potter", 300)
# print(kat)  # Output: A Gyűrűk Ura, Harry Potter
#
# # Test for statisztika
#
# adatok = [
#     ("Könyv1", 150, "Tudomány"),
#     ("Könyv2", 180, "Irodalom"),
#     ("Könyv3", 200, "Tudomány"),
#     ("Könyv4", 220, "Irodalom"),
#     ("Könyv5", 80, "Művészet"),  # Túl rövid, nem kerül be
# ]
#
# kiemelt_konyvek = statisztika(adatok)
# for konyv in kiemelt_konyvek:
#     print(konyv.cim)  # Expected output: Könyv1, Könyv2, Könyv3, Könyv4
