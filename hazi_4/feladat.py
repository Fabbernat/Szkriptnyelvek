# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147


class Palack:
    def __init__(self, ital: str | None, max_urtartalom: float | int, _jelenlegi_urtartalom: float = 1.0):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = _jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, uj_folyadek_mennyisege: int | float):
        self._jelenlegi_urtartalom = max(0, min(self.max_urtartalom, uj_folyadek_mennyisege))
        if uj_folyadek_mennyisege == 0:
            self.ital = None

    def suly(self):
        return self.max_urtartalom / 35 + self._jelenlegi_urtartalom

    def __str__(self) -> str:
        if self is None:
            return ""
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

    def __eq__(self, other) -> bool:
        if other is None or isinstance(other, str) or not isinstance(other, Palack):
            return False
        return self.ital == other.ital and self.max_urtartalom == other.max_urtartalom and self._jelenlegi_urtartalom == other._jelenlegi_urtartalom

    def __iadd__(self, other) -> "Palack":
        if other is None or isinstance(other, str) or not isinstance(other, Palack):
            return self
        total_volume = self._jelenlegi_urtartalom + other._jelenlegi_urtartalom
        self._jelenlegi_urtartalom = min(total_volume, self.max_urtartalom)
        if self.ital == other.ital:
            pass
        elif self.ital is None or self._jelenlegi_urtartalom < 1:
            self.ital = other.ital
        elif other is not None and other._jelenlegi_urtartalom > 0:
            self.ital = "keverek"
        return self


class VisszavalthatoPalack(Palack):
    def __init__(self, ital: str, max_urtartalom: float, _jelenlegi_urtartalom: float = 1.0,
                 palackdij = 25):
        super().__init__(ital, max_urtartalom, _jelenlegi_urtartalom)
        self._palackdij = palackdij #private

    @property
    def palackdij(self):
        return self._palackdij #returns private

    @palackdij.setter
    def palackdij(self, level: int | float):
        self._palackdij = max(0, level)

    def apply_discount(self, percent: float) -> float:
        self.price = self.max_urtartalom * (1 - min(percent, 10) / 100)
        return self.price

    def __str__(self):
        if self is None:
            return ""
        return f"VisszavalthatoPalack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."


class Rekesz:
    def __init__(self, max_teherbiras: str | int | float):
        self.max_teherbiras = max_teherbiras
        self.palackok = []

    def suly(self):
        if len(self.palackok) == 0:
            return 0
        summa = 0
        for palack in self.palackok:
            summa += palack.suly()
        return summa

    def uj_palack(self, obj):
        if obj is None or isinstance(obj, str) or not isinstance(obj, Palack):
            return None
        if self.suly() + obj.suly() <= self.max_teherbiras:
            self.palackok.append(obj)
            return None

    def osszes_penz(self):
        summa = 0
        for palack in self.palackok:
            if isinstance(palack, VisszavalthatoPalack) or type(palack) is VisszavalthatoPalack:
                summa += palack.palackdij
        return summa


palack1 = Palack("narancslé", 1000, 500)
palack2 = Palack("narancslé", 500, 300)
palack1 += palack2  # palack1 jelenlegi űrtartalma 800 ml lesz, ital: narancslé
print(str(palack1))
palack3 = Palack("kóla", 1000, 200)
palack1 += palack3  # palack1 jelenlegi űrtartalma 1000 ml lesz, ital: keverek
print(str(palack1))
visszavalthatoPalack = VisszavalthatoPalack("tej",500, 400, 40)
print(str(visszavalthatoPalack))
r = Rekesz(500)
print(r.suly())
r.uj_palack(visszavalthatoPalack)
print(r.osszes_penz())
