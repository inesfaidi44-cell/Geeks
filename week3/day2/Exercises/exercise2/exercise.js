
// Exercise 2: Work with forms

let form = document.querySelector("form");
console.log(form);

let fname = document.getElementById("fname");
let lname = document.getElementById("lname");

console.log(fname);
console.log(lname);

let firstname = document.getElementsByName("firstname");
let lastname = document.getElementsByName("lastname");

console.log(firstname);
console.log(lastname);

form.addEventListener("submit", function(event) {

    event.preventDefault();

    let firstValue = fname.value.trim();
    let lastValue = lname.value.trim();

    if (firstValue !== "" && lastValue !== "") {

        let ul = document.querySelector(".usersAnswer");

        let li1 = document.createElement("li");
        li1.textContent = firstValue;

        let li2 = document.createElement("li");
        li2.textContent = lastValue;

        ul.appendChild(li1);
        ul.appendChild(li2);

        fname.value = "";
        lname.value = "";
    }
    else {
        alert("Please fill in both fields!");
    }
});
