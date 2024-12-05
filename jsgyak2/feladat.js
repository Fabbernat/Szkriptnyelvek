function ragcsak(arr, index) {
    if (arr.length <= 1) {
        return undefined;
    }
    if (typeof index !== 'number') {
        return null;
    }
    return arr.slice(index).join('; ');
}

function egyetemistak(student) {
    const requiredProperties = ['nev', 'eletkor', 'informatikus_szakos', 'programok'];
    for (let prop of requiredProperties) {
        if (!student.hasOwnProperty(prop)) {
            return `Nincs ${prop} property-je az egyetemistának!`;
        }
    }

    if (!student.informatikus_szakos) {
        student.informatikus_szakos = true;
        return student;
    }

    const { nev, eletkor, programok } = student;
    if (programok.includes('kocsmázik') || programok.includes('romkocsmázik')) {
        return `${nev}, aki ${eletkor} éves és informatika szakos, péntekenként sajnos tanulás helyett kocsmázik...`;
    } else {
        return `${nev}, aki ${eletkor} éves és informatika szakos, péntekenként ${programok.join(', ')} és nem kocsmázik.`;
    }
}

// Példák:
// console.log(ragcsak([], 2)); // undefined
// console.log(ragcsak(["ropi", "keksz"], "index")); // null
// console.log(ragcsak(["chips", "ropi", "nachos", "popcorn", "keksz"], 2)); // "nachos; popcorn; keksz"


// Példák:
// console.log(egyetemistak({nev: "Tibike", eletkor: 22, programok: ["tanul", "rajzol"]}));
// "Nincs informatikus_szakos property-je az egyetemistának!"

// console.log(egyetemistak({nev: "Tibike", eletkor: 22, informatikus_szakos: false, programok: ["tanul", "rajzol"]}));
// {nev: "Tibike", eletkor: 22, informatikus_szakos: true, programok: ["tanul", "rajzol"]}

// console.log(egyetemistak({nev: "Tibike", eletkor: 22, informatikus_szakos: true, programok: ["tanul", "rajzol"]}));
// "Tibike, aki 22 éves és informatika szakos, péntekenként tanul, rajzol és nem kocsmázik."