// test.js
import faktor from './feladat.js'; // Assuming 'feladat.js' is in the same directory

// Test cases for the faktor function
const testCases = {
    "33": "3",                    // 33 = 3 * 11
    "121": "11",                  // 121 = 11 * 11
    "131237": "263",              // 131237 = 263 * 499
    "1000000007": "1000000007",   // 1000000007 is a prime number
    "29996224275833": "5479",     // 29996224275833 = 5479 * 5479
    "10403": "101",               // 10403 = 101 * 103
    "1234567891": "1234567891",   // 1234567891 is a prime number
    "899809363": "2999",          // 899809363 = 2999 * 3001
    "2": "2",                     // Smallest prime number
    "9": "3",                     // 9 = 3 * 3
    "49": "7",                    // 49 = 7 * 7
    "1000003": "1000003",         // 1000003 is a prime number
    "10000300003": "100003",      // 10000300003 = 100003 * 100003
    "9999999967": "9999999967",   // 9999999967 is a prime number
    "98989898989": "9091",        // 98989898989 = 9091 * 10891
};

let totalErrors = 0;

for (const [input, expectedOutput] of Object.entries(testCases)) {
    const output = faktor(input);
    if (output !== expectedOutput) {
        console.error(`Error in input '${input}': expected '${expectedOutput}', got '${output}'`);
        totalErrors += 1;
    }
}

console.log(`\nTotal errors: ${totalErrors}`);
console.log(`Total test cases: ${Object.keys(testCases).length}`);