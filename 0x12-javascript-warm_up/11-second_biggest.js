#!/usr/bin/node

const values = process.argv.slice(2).map(arg => parseInt(arg));

if (values.length < 2) {
  console.log(0);
} else {
  values.sort((a, b) => b - a);
  console.log(values[1]);
  // let largest = -Infinity;
  // let secondLargest = -Infinity;
  // for (let i = 0; i < values.length; i++){
  //     const num = values[i];
  //     if (num > largest){
  //         secondLargest = largest;
  //         largest = num;
  //     }else if(num > secondLargest && num !== largest){
  //         secondLargest = num;
  //     }
  // }
  // console.log(secondLargest);
}
