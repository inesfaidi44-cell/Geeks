// Method 1: Using one for loop
let stars = "";

for (let i = 1; i <= 6; i++) {
    stars += "* ";
    console.log(stars);
}

// Method 2: Using nested for loops
for (let i = 1; i <= 6; i++) {
    let line = "";

    for (let j = 1; j <= i; j++) {
        line += "* ";
    }

    console.log(line);
}