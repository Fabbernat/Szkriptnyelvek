// Nev: Fabian Bernat
// Neptun: URX5VP
// h: h259147

function tokeletes(num) {
    let tokeletes = 0;
    for (let i = 0; i < num.length; i++) {
        if (num[i] === num[i + 1]) {
            tokeletes++;
        }
    }
    return tokeletes;
    
}

class Webbongeszo{
    constructor(nev, neptun, h) {
        this.nev = nev;
        this.neptun = neptun;
        this.h = h;
    }
}