// Nev: Fabian Bernat
// Neptun: URX5VP
// h: h259147

class Hallgato {
    constructor(neptun, felev = 1) {
        this.neptun = neptun;
        this._felev = felev;
        this.jegyek = [];
    }

    get felev() {
        return this._felev;
    }

    set felev(ujFelev) {
        if (Number.isInteger(ujFelev)) {
            this._felev = Math.max(ujFelev, this._felev);
        }
    }

    zarthelyi(targy, orak) {
        let jegy = 1;
        if (targy !== 'kalkulus') {
            jegy = Math.floor(Math.sqrt(this._felev * orak));
            jegy = Math.min(jegy, 5);
        }
        this.jegyek.push(jegy);
    }

    felevVege() {
        const osszeg = this.jegyek.reduce((acc, jegy) => acc + jegy, 0);
        const atlag = this.jegyek.length > 0 ? osszeg / this.jegyek.length : 0;
        return `Neptun: ${this.neptun}, ${this._felev}. felev, ${atlag} atlag`;
    }
}

class TTIKHallgato extends Hallgato {
    constructor(neptun, hAzonosito, felev) {
        super(neptun, felev);
        this.hAzonosito = hAzonosito;
    }

    zarthelyi(targy, orak) {
        if (targy === 'kalkulus') {
            this.jegyek.push(5);
        } else {
            super.zarthelyi(targy, orak);
        }
    }

    felevVege() {
        const alapSzoveg = super.felevVege();
        return `${alapSzoveg} (h: ${this.hAzonosito})`;
    }
}

const hallgato = new Hallgato('NEP234');
// console.log(hallgato.felev); // 1
hallgato.felev = 3;
hallgato.zarthelyi('kalkulus', 4); // Kalkulusból 1-est kapott
hallgato.zarthelyi('szkriptnyelvek', 6); // Itt 4-est kapott
// console.log(hallgato.felevVege()); // "Neptun: NEP234, 3. felev, 2.5 atlag"

const ttikHallgato = new TTIKHallgato('XYZ123', 'h123456', 2);
ttikHallgato.zarthelyi('kalkulus', 5);  // Kalkulusból 5-öst kapott
ttikHallgato.zarthelyi('programozás', 8);
// console.log(ttikHallgato.felevVege()); // "Neptun: XYZ123, 2. felev, 4.5 atlag (h: h123456)"