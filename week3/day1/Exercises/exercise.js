// Exercise 1: Find the numbers divisible by 23

function displayNumbersDivisible(divisor = 23) {
    let sum = 0;

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        }
    }

    console.log("Sum:", sum);
}

displayNumbersDivisible();

// Exercise 2: Shopping List

const stock = {
    banana: 6,
    apple: 0,
    pear: 12,
    orange: 32,
    blueberry: 1
};

const prices = {
    banana: 4,
    apple: 2,
    pear: 1,
    orange: 1.5,
    blueberry: 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;

    for (let item of shoppingList) {
        if (stock[item] > 0) {
            total += prices[item];

            // Bonus: decrease stock
            stock[item]--;
        }
    }

    return total;
}

console.log("Total:", myBill());


// Exercise 3: What's in my wallet?

function changeEnough(itemPrice, amountOfChange) {

    let quarters = 25;
    let dimes = 10;
    let nickels = 5;
    let pennies = 1;

    let total =
        amountOfChange[0] * quarters +
        amountOfChange[1] * dimes +
        amountOfChange[2] * nickels +
        amountOfChange[3] * pennies;

    let price = itemPrice * 100;

    return total >= price;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));
console.log(changeEnough(0.75, [0, 0, 20, 5]));


// # Exercise 4: Vacations Costs


// # Exercise 4: Vacations Costs

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function hotelCost(nights) {
    return nights * 140;
}

function planeRideCost(destination) {
    if (destination.toLowerCase() === "london") {
        return 183;
    }
    else if (destination.toLowerCase() === "paris") {
        return 220;
    }
    else {
        return 300;
    }
}

function rentalCarCost(days) {
    let cost = days * 40;

    if (days > 10) {
        cost = cost * 0.95;
    }

    return cost;
}

function totalVacationCost() {

    rl.question("How many nights in the hotel? ", function(nights) {

        nights = Number(nights);

        if (isNaN(nights) || nights <= 0) {
            console.log("Please enter a valid number.");
            rl.close();
            return;
        }

        rl.question("Where do you want to travel? ", function(destination) {

            if (destination.trim() === "") {
                console.log("Please enter a destination.");
                rl.close();
                return;
            }

            rl.question("How many days for the car rental? ", function(days) {

                days = Number(days);

                if (isNaN(days) || days <= 0) {
                    console.log("Please enter a valid number.");
                    rl.close();
                    return;
                }

                let hotel = hotelCost(nights);
                let plane = planeRideCost(destination);
                let car = rentalCarCost(days);

                let total = hotel + plane + car;

                console.log("Hotel cost: $" + hotel);
                console.log("Plane tickets: $" + plane);
                console.log("Car rental: $" + car);
                console.log("Total vacation cost: $" + total);

                rl.close();
            });
        });
    });
}

totalVacationCost();
