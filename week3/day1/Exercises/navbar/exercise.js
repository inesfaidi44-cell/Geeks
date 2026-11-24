
// Exercise 6: Change the Navbar

let navBar = document.getElementById("navBar");

navBar.setAttribute("id", "socialNetworkNavigation");

let ul = navBar.querySelector("ul");

let newLi = document.createElement("li");

let text = document.createTextNode("Logout");

newLi.appendChild(text);

ul.appendChild(newLi);

let first = ul.firstElementChild;
let last = ul.lastElementChild;

console.log("First link:", first.textContent);
console.log("Last link:", last.textContent);
