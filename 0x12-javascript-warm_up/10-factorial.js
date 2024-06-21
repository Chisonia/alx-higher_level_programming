#!/usr/bin/node

function factorial (n) {
  if (n <= 1) { // condition to stop
    return 1;
  } else {
    return n * factorial(n - 1); // recursion
  }
}
const num = parseInt(process.argv[2]);
const fact = isNaN(num) ? 1 : factorial(num);// handle case if the first argument is not an integer
console.log(fact);
