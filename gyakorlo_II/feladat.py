# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147
def minta_egyezesek(dict1: dict, dict2: dict):
    if set(dict1.keys()) != set(dict2.keys()):
        return -1

    if not dict1 or not dict2:
        return 0

    egyezesek: int = 0
    for key in dict1:
        if dict1[key] == dict2[key]:
            egyezesek += 1

    return egyezesek


print(minta_egyezesek({"10:00": 33, "11:30": 66, "13:00": 132}, {"10:00": 33, "11:30": 63, "13:00": 132}))  # VĂĄrhatĂł: 2
print(minta_egyezesek({"10:00": 33, "11:30": 66, "13:00": 132}, {"10:00": 33, "11:00": 66, "13:00": 132}))  # VĂĄrhatĂł: -1
print(minta_egyezesek({}, {}))  # VĂĄrhatĂł: 0
