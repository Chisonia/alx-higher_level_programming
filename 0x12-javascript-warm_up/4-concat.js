#!/usr/bin/node

console.log(
  (process.argv[2] !== undefined ? process.argv[2] : 'undefined') +
    ' is ' +
    (process.argv[3] !== undefined ? process.argv[3] : 'undefined')
);

// if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
//     console.log(process.argv[2] + ' is ' + process.argv[3]);
// } else if (process.argv[2] !== undefined && process.argv[3] === undefined) {
//     console.log(process.argv[2] + ' is undefined');
// } else if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
//     console.log('undefined is ' + process.argv[3]);
// } else {
//     console.log('undefined is undefined');
// }
