// 1. feladat: Disarium szám

function isDisarium(number) {
    if (typeof number !== 'number' || number < 0) {
        return undefined;
    }

    const strNumber = number.toString();
    let sum = 0;
    for (let i = 0; i < strNumber.length; i++) {
        sum += Math.pow(parseInt(strNumber[i]), i + 1);
    }

    return sum === number;
}

// Példák:
// console.log(isDisarium(175)); // true
// console.log(isDisarium(42)); // false
// console.log(isDisarium('macska')); // undefined


// 2. feladat: Betűkombinációk

function letterCombinations(digits) {
    if (digits === null || digits.length === 0) {
        return [];
    }

    const mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    };

    const result = [];

    function backtrack(index, path) {
        if (path.length === digits.length) {
            result.push(path);
            return;
        }

        const letters = mapping[digits[index]];
        for (let i = 0; i < letters.length; i++) {
            backtrack(index + 1, path + letters[i]);
        }
    }

    backtrack(0, '');

    return result;
}

// Példa:
// console.log(letterCombinations('532'));
// ["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]


// 3. feladat: Savanyúság

class Savanyusag {
    constructor(minosegetMegorzi, nyitva, hozzavalok) {
        this.minosegetMegorzi = minosegetMegorzi;
        this.nyitva = nyitva;
        this.hozzavalok = hozzavalok;
        this._tipus = this.setTipus();
    }

    setTipus() {
        const first = this.hozzavalok[0];
        if (this.hozzavalok.every(hozzavalo => hozzavalo === first)) {
            return first;
        } else {
            return 'csalamade';
        }
    }

    get tipus() {
        return this._tipus;
    }

    set tipus(ujTipus) {
        if (this.hozzavalok.includes(ujTipus)) {
            this._tipus = ujTipus;
        }
    }

    szavatos(ev, honap, nap) {
        const [lejaratiEv, lejaratiHonap, lejaratiNap] = this.minosegetMegorzi;
        return (
            ev < lejaratiEv ||
            (ev === lejaratiEv && honap < lejaratiHonap) ||
            (ev === lejaratiEv && honap === lejaratiHonap && nap <= lejaratiNap)
        );
    }

    fedeletElcsavar() {
        this.nyitva = !this.nyitva;
    }

    osszeont(masikSavanyusag) {
        if (!(masikSavanyusag instanceof Savanyusag)) {
            return 'HIBA! Nem savanyusag!';
        }
        if (!this.nyitva || !masikSavanyusag.nyitva) {
            return 'HIBA! A savanyusag fedele zarva van!';
        }

        this.hozzavalok = this.hozzavalok.concat(masikSavanyusag.hozzavalok);
        this.minosegetMegorzi = this.minosegetMegorzi < masikSavanyusag.minosegetMegorzi
            ? this.minosegetMegorzi
            : masikSavanyusag.minosegetMegorzi;
        this._tipus = this.setTipus();

        return 'Savanyusagok osszeontve!';
    }

    info() {
        const fedelAllapot = this.nyitva ? 'nyitva' : 'zarva';
        return `Savanyitott ${this._tipus}, aminek a fedele ${fedelAllapot}`;
    }

    hozzavalokatTobbszoroz(szorzo) {
        const ujHozzavalok = [];
        for (const hozzavalo of this.hozzavalok) {
            for (let i = 0; i < szorzo; i++) {
                ujHozzavalok.push(hozzavalo);
            }
        }
        this.hozzavalok = ujHozzavalok;
    }
}

// Példák a Savanyusag osztály használatára:
// const savanyusag1 = new Savanyusag([2025, 12, 24], true, ['uborka', 'paprika']);
// console.log(savanyusag1.info()); // "Savanyitott csalamade, aminek a fedele nyitva"
// savanyusag1.fedeletElcsavar();
// console.log(savanyusag1.info()); // "Savanyitott csalamade, aminek a fedele zarva"
// savanyusag1.fedeletElcsavar();
// console.log(savanyusag1.szavatos(2024, 12, 24)); // true
// console.log(savanyusag1.szavatos(2026, 12, 24)); // false
//
// const savanyusag2 = new Savanyusag([2024, 12, 24], true, ['paprika']);
// console.log(savanyusag1.osszeont(savanyusag2)); // "Savanyusagok osszeontve!"
// console.log(savanyusag1.info()); // "Savanyitott csalamade, aminek a fedele nyitva"
// console.log(savanyusag1.hozzavalok); // ["uborka", "paprika", "paprika"]
//
// savanyusag1.hozzavalokatTobbszoroz(2);
// console.log(savanyusag1.hozzavalok); // ["uborka", "uborka", "paprika", "paprika", "paprika", "paprika"]