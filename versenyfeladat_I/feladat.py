# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147

def elvalasztas(word):
    ### strings
    vowels = "aeiou"
    vowels = "aáeéiíoóuúöőüű"
    consonants = "bcdfghjklmnpqrstvwxyz"
    current_syllable = ""

    ### dicts
    digraphs = {"cs", "sz", "ty", "gy", "ny", "dz", "dzs"}

    ### lists
    syllables = []
    # config: egy
    known_prefixes = [
        "meg",  "egy",
        "fel", "el",
        "kép", "köz",
        "szem", "kör",
        "biz", "gon",
        "tár", "gyors",
        "gyógy", "füg",
        "ál", "dön",
        "nyelv", "tér",
        "asz", "gyer",
        "ün", "or",
        "mun", "al",
        "in", "ér",
        "rész", "nyil",
        "rend", "karszt",
        "kap", "vég"
    ]
    # known_suffixes = ["ság", "ség", "os", "es", "ás", "és", "szág", "ügy", "mány"]

    ### ints
    i = 0

    for prefix in known_prefixes:
        if word.startswith(prefix):
            syllables.append(prefix)
            i = len(prefix)  # Move index after the prefix
            break

    # Iterate through the word to form syllables
    while i < len(word):
        char = word[i]
        current_syllable += char

        # Check for syllable breaks: vowel followed by consonant or end of word
        if char in vowels:
            # Handle consonant clusters between vowels
            j = i + 1
            consonant_cluster = ""
            while j < len(word) and word[j] not in vowels:
                consonant_cluster += word[j]
                j += 1

            # If a consonant cluster is found, apply splitting rule
            if len(consonant_cluster) > 1:
                split_point = len(consonant_cluster) - 1  # Default split: n-1 left, 1 right
                for digraph in digraphs:
                    if consonant_cluster.startswith(digraph):
                        split_point = len(digraph)
                        break

                # Append the left side of the cluster to the current syllable
                current_syllable += consonant_cluster[:split_point]
                syllables.append(current_syllable)
                current_syllable = consonant_cluster[split_point:]
                i = j - 1  # Adjust index to just before next vowel
            else:
                syllables.append(current_syllable)
                current_syllable = ""
        elif i == len(word) - 1 and current_syllable:
            # Handle trailing consonants by appending them to the last syllable
            if syllables:
                syllables[-1] += current_syllable
            else:
                syllables.append(current_syllable)
            current_syllable = ""
        i += 1

    # Final check for dangling consonants at the end of the word
    if current_syllable:  # Append remaining part as a syllable
        if current_syllable[-1] in consonants:
            # Append remaining consonants to the last syllable
            if syllables and all(char in consonants for char in current_syllable):
                syllables[-1] += current_syllable
            else:
                syllables.append(current_syllable)
        else:
            syllables.append(current_syllable)

    # Check for suffix attachment if word ends with a known suffix

    return "-".join(syllables)



dictionary = {
    "asztal": "asz-tal",
    "katona": "ka-to-na",
    "rendőr": "rend-őr",
    "megszentségteleníthetetlenségeskedéseitekért": "meg-szent-ség-te-le-nít-he-tet-len-sé-ges-ke-dé-se-i-te-kért",
    "gyümölcs": "gyü-mölcs",
    "számítógép": "szá-mí-tó-gép",
    "tanulás": "ta-nu-lás",
    "gyermek": "gyer-mek",
    "halászlé": "ha-lász-lé",
    "szőlő": "sző-lő",
    "madár": "ma-dár",
    "ünnep": "ün-nep",
    "szeretlek": "sze-ret-lek",
    "ország": "or-szág",
    "tulajdonság": "tu-laj-don-ság",
    "megoldás": "meg-ol-dás",
    "tudomány": "tu-do-mány",
    "szívem": "szí-vem",
    "háziorvos": "há-zi-or-vos",
    "megbízható": "meg-bíz-ha-tó",
    "tanító": "ta-ní-tó",
    "munkahely": "mun-ka-hely",
    "iskola": "is-ko-la",
    "testvér": "test-vér",
    "hétköznap": "hét-köz-nap",
    "magyarország": "ma-gyar-or-szág",
    "nemzetközi": "nem-zet-kö-zi",
    "szabadság": "sza-bad-ság",
    "vizsgálat": "vizs-gá-lat",
    "nyelvtanulás": "nyelv-ta-nu-lás",
    "vállalat": "vál-la-lat",
    "társadalom": "tár-sa-da-lom",
    "kutatás": "ku-ta-tás",
    "egészségügy": "e-gész-ség-ügy",
    "hagyomány": "ha-gyo-mány",
    "számítás": "szá-mí-tás",
    "elmélet": "el-mé-let",
    "fejlesztés": "fej-lesz-tés",
    "időjárás": "i-dő-já-rás",
    "kultúra": "kul-tú-ra",
    "ünnepély": "ün-ne-pély",
    "egyetem": "e-gye-tem",
    "könyvtár": "könyv-tár",
    "gyógyszer": "gyógy-szer",
    "szeretet": "sze-re-tet",
    "család": "csa-lád",
    "állampolgár": "ál-lam-pol-gár",
    "gondolat": "gon-do-lat",
    "tulajdonos": "tu-laj-do-nos",
    "szívesen": "szí-ve-sen",
    "megértés": "meg-ér-tés",
    "művészet": "mű-vé-szet",
    "gyorsvonat": "gyors-vo-nat",
    "biztonság": "biz-ton-ság",
    "találkozó": "ta-lál-ko-zó",
    "felhőkarcoló": "fel-hő-kar-co-ló",
    "állatkert": "ál-lat-kert",
    "közlekedés": "köz-le-ke-dés",
    "mesterséges": "mes-ter-sé-ges",
    "felhasználó": "fel-hasz-ná-ló",
    "környezetvédelem": "kör-nye-zet-vé-de-lem",
    "szemüveg": "szem-ü-veg",
    "állatorvos": "ál-lat-or-vos",
    "megfelelés": "meg-fe-le-lés",
    "döntés": "dön-tés",
    "tájékoztatás": "tá-jé-koz-ta-tás",
    "számológép": "szá-mo-ló-gép",
    "rendszer": "rend-szer",
    "egység": "egy-ség",
    "műszaki": "mű-sza-ki",
    "dolog": "do-log",
    "barátság": "ba-rát-ság",
    "magatartás": "ma-ga-tar-tás",
    "független": "füg-get-len",
    "bizalom": "bi-za-lom",
    "közvetítés": "köz-ve-tí-tés",
    "feladat": "fel-a-dat",
    "kapcsolat": "kap-cso-lat",
    "térkép": "tér-kép",
    "jóváhagyás": "jó-vá-ha-gyás",
    "tudatos": "tu-da-tos",
    "alkalmazás": "al-kal-ma-zás",
    "bizonyíték": "bi-zo-nyí-ték",
    "felmérés": "fel-mé-rés",
    "érdeklődés": "ér-dek-lő-dés",
    "követelmény": "kö-ve-tel-mény",
    "figyelem": "fi-gye-lem",
    "valóság": "va-ló-ság",
    "ellenőrzés": "el-len-őr-zés",
    "közösség": "kö-zös-ség",
    "segítség": "se-gít-ség",
    "nyilvános": "nyil-vá-nos",
    "vélemény": "vé-le-mény",
    "részvétel": "rész-vé-tel",
    "hatékonyság": "ha-té-kony-ság",
    "együttműködés": "e-gyütt-mű-kö-dés",
    "értékelés": "ér-té-ke-lés",
    "intézmény": "in-téz-mény",
    "megbízhatóság": "meg-bíz-ha-tó-ság",
    "felügyelet": "fel-ü-gye-let",
    "működés": "mű-kö-dés",
    "szabályzat": "sza-bály-zat",
    "képzés": "kép-zés",
    "végrehajtás": "vég-re-haj-tás",
    "irányítás": "i-rá-nyí-tás",
    "összekötés": "ösz-sze-kö-tés",
    "almalé": "al-ma-lé",
    "karsztstrand": "karszt-strand",
    "fiaiéi": "fi-a-i-é-i"

}

total_errors = 0

for word, expected_output in dictionary.items():
    output = elvalasztas(word)
    if output != expected_output:
        print(f"Error in word '{word}': expected '{expected_output}', got '{output}'")
        total_errors += 1

print(f"Total errors: {total_errors}")
print(f"Length of dictionary: {len(dictionary)}")
