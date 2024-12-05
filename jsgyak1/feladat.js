// Nev: Fabian Bernat
// Neptun: URX5VP
// h: h259147



function lama(nev, kor = 5) {
    if (nev === undefined) {
        return "Nincsen neve szegény párának!";
    }

    if (nev.endsWith("láma")) {
        return "Ez egy igazi láma!";
    }

    if (kor <= 2) {
        return `${nev} még gyerek, csak ${kor} éves!`;
    }

    if (kor >= 15) {
        return `${nev} már egy bölcs öreg, megérte ${kor} éves kort!`;
    }

    for (let i = 0; i < kor; i++) {
        nev += "láma";
    }

    return `${nev} egy igazi láma lett!`;
}

// Példák
// console.log(lama("Kiraláma")); // output: Ez egy igazi láma!
// console.log(lama("Kira", 2)); // output: Kira még gyerek, csak 2 éves!
// console.log(lama("Kira")); // output: Kiralámalámalámalámaláma egy igazi láma lett!
// console.log(lama()); // output: Nincsen neve szegény párának!
// console.log(lama("Lámácska", 15)); // output: Lámácska már egy bölcs öreg, megérte 15 éves kort!