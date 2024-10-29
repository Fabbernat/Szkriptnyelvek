# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147

class StadiumData:
    Team = 0
    FDCOUK = 1
    City = 2
    Stadium = 3
    Capacity = 4
    Latitude = 5
    Longitude = 6
    Country = 7


def legnagyobb_stadion(path) -> None:
    with open(path, 'r', encoding='utf-8') as csv_file:
        sorok = csv_file.readlines()
        stadionok = []
        for sor in sorok[1:]:
            adatok = sor.strip().split(',')
            adatok = [elem.strip() for elem in adatok]
            stadionok.append(adatok)

        max_capacity = 0
        max_stadium = "Nincs (Nincs)"
        for stadion in stadionok:
            try:
                capacity = int(stadion[StadiumData.Capacity])
                if capacity > max_capacity:
                    max_capacity = capacity
                    name = stadion[StadiumData.Stadium]  # stadion neve
                    city = stadion[StadiumData.City]  # stadion vĂĄrosa
                    max_stadium = f"{name} ({city})"
            except ValueError:
                continue

        with open('legnagyobb.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(max_stadium + '\n')


# legnagyobb_stadion("../stadium.csv")

def osszes_arena(path) -> None:
    with open(path, 'r', encoding='utf-8') as csv_file:
        sorok = csv_file.readlines()
        stadionok = []
        for sor in sorok[1:]:
            adatok = sor.strip().split(',')
            adatok = [elem.strip() for elem in adatok]
            stadionok.append(adatok)
        # Team, FDCOUK, City, Stadium, Capacity, Latitude, Longitude, Country = []

        output_data = 'Stadium,City,Country,Big\n'
        for stadion in stadionok:
            try:
                if stadion[StadiumData.Stadium].endswith("Arena"):
                    is_large = "True" if int(stadion[StadiumData.Capacity]) > 50000 else "False"
                    output_data += f"{stadion[StadiumData.Stadium]},{stadion[StadiumData.City]},{stadion[StadiumData.Country]},{is_large}\n"
            except ValueError:
                continue

        with open('arena_park.csv', 'w', encoding='utf-8') as output_file:
            output_file.write(output_data)


# osszes_arena("../stadium.csv")

def osszes_park(path) -> None:
    with open(path, 'r', encoding='utf-8') as csv_file:
        sorok = csv_file.readlines()
        stadionok = []
        for sor in sorok[1:]:
            adatok = sor.strip().split(',')
            adatok = [elem.strip() for elem in adatok]
            stadionok.append(adatok)
        output_data = ''
        for stadion in stadionok:
            try:
                if stadion[StadiumData.Stadium].endswith("Arena"):
                    is_large = "True" if int(stadion[StadiumData.Capacity]) > 20000 else "False"
                    output_data += f"{stadion[StadiumData.Stadium]},{stadion[StadiumData.City]},{stadion[StadiumData.Country]},{is_large}\n"
            except ValueError:
                continue

        with open('arena_park.csv', 'a', encoding='utf-8') as output_file:
            output_file.write(output_data)


# osszes_park("../stadium.csv")


def varosok_szama(path, *orszagok) -> None:
    if not orszagok:
        raise Exception("Nincs megadva egy orszag sem!")
    try:
        with open(path, 'r', encoding='utf-8') as csv_file:
            sorok = csv_file.readlines()
            stadionok = []
            for sor in sorok[1:]:
                adatok = sor.strip().split(',')
                adatok = [elem.strip() for elem in adatok]
                stadionok.append(adatok)

            orszag_varosok = {}
            for orszag in orszagok:
                varosok = sorted(
                    set(stadion[StadiumData.City] for stadion in stadionok if stadion[StadiumData.Country] == orszag))
                orszag_varosok[orszag] = varosok

            with open('varosok.txt', 'w', encoding='utf-8') as output_file:
                for orszag, varosok in orszag_varosok.items():
                    output_file.write(f"{orszag} varosai:\n")
                    for varos in varosok:
                        output_file.write(f"\t{varos}\n")
                    output_file.write("----------\n")
    except Exception as e:
        raise Exception("Nincs megadva egy orszag sem!")


legnagyobb_stadion("../stadium.csv")
osszes_arena("../stadium.csv")
osszes_park("../stadium.csv")
varosok_szama("../stadium.csv", "England", "Hungary")
varosok_szama("../stadium.csv")
