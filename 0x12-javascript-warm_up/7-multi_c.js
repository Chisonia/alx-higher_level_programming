#!/usr/bin/node
let i;
const x = process.argv[2]? parseInt(process.argv[2]) : undefined;

if (x === undefined) {
    console.log('Missing number of occurrences');
} else if (isNaN(x)) {
    console.log('Invalid number of occurrences');
} else if (x < 0) {
    return 1;
} else {
    for (let i = 0; i < x; i++) {
        console.log('C is fun');
    }
}