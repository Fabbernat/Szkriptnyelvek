# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147
def exponens(szoveg: str, szorzoszam=1, kitevo=1) -> str:
    if kitevo < 1:
        kitevo = 1
    return str(szoveg)*(int(szorzoszam)**int(kitevo))


def kodolo(szoveg: str) -> str:
    return szoveg.replace("a", "#").replace("e", "##").replace("i", "###").replace("o", "####").replace("u", "#####")


def test_exponens():
    # AlapĂŠrtelmezett szorzĂłszĂĄm ĂŠs kitevĹ
    assert exponens("levĂŠl") == "levĂŠl"

    # KettĹszĂśrĂśzĂŠs
    assert exponens("alma", 2, 2) == "almaalmaalmaalma"

    # HĂĄromszoros ismĂŠtlĂŠs
    assert exponens("kĂśrte", 3, 0) == "kĂśrtekĂśrtekĂśrte"  # KitevĹ 0, szorzĂłszĂĄm nem hatvĂĄnyozva

    # SzĂĄm mint string
    assert exponens("10", 2, 3) == "1010101010101010"

    # NegatĂ­v kitevĹ, szorzĂłszĂĄm nem hatvĂĄnyozva
    assert exponens("szĂł", 3, -1) == "szĂłszĂłszĂł"

    # KitevĹ 1
    assert exponens("gyĂźmĂślcs", 5, 1) == "gyĂźmĂślcsgyĂźmĂślcsgyĂźmĂślcsgyĂźmĂślcsgyĂźmĂślcs"


    print("Minden teszteset sikeresen lefutott.")


# TeszteljĂźk a fĂźggvĂŠnyt
test_exponens()


def test_kodolo():
    # AlapvetĹ magĂĄnhangzĂł cserĂŠk
    assert kodolo("alma") == "#lm#"

    # TĂśbb magĂĄnhangzĂł cserĂŠje
    assert kodolo("gumiabroncs") == "g#####m####br####ncs"

    # MagĂĄnhangzĂłk ismĂŠtlĹdĂŠse
    assert kodolo("istĂĄllĂł") == "###stĂĄllĂł"

    # Ăres string
    assert kodolo("") == ""

    # Nincs magĂĄnhangzĂł
    assert kodolo("xyz") == "xyz"  # Semmi nem vĂĄltozik

    # Ăsszetett magĂĄnhangzĂłk
    assert kodolo("aerodinamikus") == "###r####d###n#m###k#####s"  # Vegyes magĂĄnhangzĂłk

    print("Minden teszteset sikeresen lefutott.")


# TeszteljĂźk a fĂźggvĂŠnyt
test_kodolo()
