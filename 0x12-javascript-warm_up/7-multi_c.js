#!/usr/bin/node
let x = Number(process.argv[2]);
if (isNaN(x)) {
        console.log('Missing number of occurrences');
} else {
        for (i = 0; i < x; i++) {
                console.log('C is fun');
        }
}
