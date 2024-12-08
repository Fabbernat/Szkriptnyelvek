function faktor(numStr) {
    let num = BigInt(numStr);
    if (num % 2n === 0n) return '2';
    let factor = 3n;
    while (factor * factor <= num) {
        if (num % factor === 0n) return factor.toString();
        factor += 2n;
    }
    return num.toString();
}
