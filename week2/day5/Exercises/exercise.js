/* Exercise 1 : List of people 
Part I - Review about arrays*/

const people = ["Greg", "Mary", "Devon", "James"];

people.splice(0, 1);

people[2] = "Jason";
    
people.push("Ines");

console.log(people.indexOf("Mary")); 

const newPeople = people.slice(1, 3);
console.log(newPeople);

console.log(people.indexOf("Foo")); 

const last = people[people.length - 1];
console.log(last);

/* Part II - Loops */

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);

    if (people[i] === "Devon") {
        break;
    }
}

// Exercise 2 : Your favorite colors

const colors = ["blue", "red", "green", "black", "white"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}`);
}

const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}

// Exercise 3 : Repeat the question

/*let number = Number(prompt("Enter a number:"));

while (number < 10) {
    number = Number(prompt("Enter another number:"));
}

console.log("Your number is:", number);
*/
//  Exercise 4 : Building Management
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors);

console.log(
    building.numberOfAptByFloor.firstFloor +
    building.numberOfAptByFloor.thirdFloor
); 

console.log(building.nameOfTenants[1]); 
console.log(building.numberOfRoomsAndRent.dan[0]); 

const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const danRent = building.numberOfRoomsAndRent.dan[1];
const davidRent = building.numberOfRoomsAndRent.david[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log(building.numberOfRoomsAndRent.dan);

//  Exercise 5 : Family

const family = {
    father: "Ahmed",
    mother: "Fatima",
    sister: "Sara",
    brother: "Youssef"
};

for (let key in family) {
    console.log(key);
}


for (let key in family) {
    console.log(family[key]);
}

// Exercise 6 : Rudolf

const details = {
    my: "name",
    is: "Rudolf",
    the: "reindeer"
};

let sentence = "";

const keys = Object.keys(details);

for (let i = 0; i < keys.length; i++) {
    sentence += keys[i] + " " + details[keys[i]] + " ";
}

console.log(sentence.trim());

// Exercise 7 : Secret Group

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let societyName = [];

for (let i = 0; i < names.length; i++) {
    societyName.push(names[i][0]);
}

societyName.sort();

console.log(societyName.join(""));

