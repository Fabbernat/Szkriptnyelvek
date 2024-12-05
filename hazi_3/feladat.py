# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147



def hogolyo_csata(korok: list):
    statisztika = {}
    for kor in korok:
        for jatekos, adat in kor.items():
            if jatekos not in statisztika:
                statisztika[jatekos] = {
                    'eldobott_hogolyok': 0,
                    'talalt': 0,
                    'fejtalalat': 0
                }
            statisztika[jatekos]['eldobott_hogolyok'] += adat.get('eldobott_hogolyok', 0)
            statisztika[jatekos]['talalt'] += adat.get('talalt', 0)
            statisztika[jatekos]['fejtalalat'] += adat.get('fejtalalat', 0)
    return statisztika


def hogolyo_pontossag(statisztika):
    for jatekos, adat in statisztika.items():
        if adat['eldobott_hogolyok'] > 0:
            adat['pontossag'] = adat['talalt'] / adat['eldobott_hogolyok']
        else:
            adat['pontossag'] = 0
    return statisztika


def hogolyo_piros_lap(statisztika: dict):
    piros_lapok = []

    for jatekos, adat in statisztika.items():
        if adat['pontossag'] >= 0.7 and adat['fejtalalat'] / adat['talalt'] >= 0.5:
            piros_lapok.append(jatekos)

    return piros_lapok


coeur = {
    'Bence': {
        'eldobott_hogolyok': 4,
        'talalt': 1
    },
    'Gabor': {
        'eldobott_hogolyok': 16,
        'talalt': 6,
        'fejtalalat': 1
    },
    'Zsolt': {
        'eldobott_hogolyok': 28,
    },
    'Imre': {
        'eldobott_hogolyok': 4,
        'talalt': 1,
        'fejtalalat': 1
    },
    'Sandor': {
        'eldobott_hogolyok': 17,
        'talalt': 7
    }
}

csata_input = [
    {
        'Tamas': {
            'eldobott_hogolyok': 4,
            'talalt': 1
        },
        'Ferenc': {
            'eldobott_hogolyok': 16,
            'talalt': 6,
            'fejtalalat': 1
        },
        'Csaba': {
            'eldobott_hogolyok': 28,
        }
    },
    {
        'Tamas': {
            'eldobott_hogolyok': 2,
            'talalt': 2
        },
        'Ferenc': {
            'eldobott_hogolyok': 3,
            'talalt': 2,
            'fejtalalat': 1
        },
        'Csaba': {
            'eldobott_hogolyok': 4,
            'talalt': 2,
            'fejtalalat': 1
        }
    }
]
pontossag_input = {
    "Tamas": {
        "eldobott_hogolyok": 6,
        "talalt": 3,
        "fejtalalat": 0
    },
    "Ferenc": {
        "eldobott_hogolyok": 19,
        "talalt": 8,
        "fejtalalat": 2
    },
    "Csaba": {
        "eldobott_hogolyok": 32,
        "talalt": 2,
        "fejtalalat": 1
    }
}

piros_lap_input = {
    "Geza": {
        "eldobott_hogolyok": 14,
        "talalt": 4,
        "fejtalalat": 0,
        "pontossag": 0.2857142857142857
    },
    "Lajos": {
        "eldobott_hogolyok": 45,
        "talalt": 36,
        "fejtalalat": 22,
        "pontossag": 0.8
    },
    "Jozsef": {
        "eldobott_hogolyok": 37,
        "talalt": 29,
        "fejtalalat": 15,
        "pontossag": 0.7837837837837838
    }
}

out1 = hogolyo_csata(csata_input)
print(out1)
kibovitett_dict = hogolyo_pontossag(pontossag_input)
print(kibovitett_dict)
piros_laposok = hogolyo_piros_lap(piros_lap_input)
print(piros_laposok)

