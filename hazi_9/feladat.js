// Nev: Fabian Bernat
// Neptun: URX5VP
// h: h259147

class Nyuszi {
    _repa
    vendegek = []


    constructor(repa = 0) {
        this._repa = repa;
        this.vendegek = [];
    }


    get repa() {
        return this._repa;
    }

    ultet(mennyiseg = 1){
        this._repa += mennyiseg;
    }

    vendeg(vendeg_neve){
        if (typeof vendeg_neve === 'string'){
            this.vendegek.push(vendeg_neve);
        }
    }

    etet(){
        while (this._repa > 0 && this.vendegek.length > 0) {
            this._repa--;
            this.vendegek.shift();
        }
    }
}

// nincs répája Nyuszinak.
// var nyusz = new Nyuszi(0);
// //ültet egy répát.
// nyusz.ultet(1);
// console.log(nyusz.repa); // 1.
// console.log(nyusz.vendegek); //még nincs vendége az eredmény [].
// nyusz.vendeg('Robert Gida'); // Róbert Gida megérkezik Nyuszihoz.
// nyusz.vendeg('Malacka'); // Malacka megérkezik Nyuszihoz.
// console.log(nyusz.vendegek); // ['Robert Gida', 'Malacka']
// nyusz.etet(); // Mivel van egy 1 répa, Robert Gida kap egyet és utána haza megy. Malackának már nem jutott répa, ezért neki várnia kell.
// console.log(nyusz.repa) // 0
// console.log(nyusz.vendegek); // ['Malacka']