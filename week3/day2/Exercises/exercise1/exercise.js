
// Exercise 1: Change the article

let h1 = document.querySelector("h1");
console.log(h1);

let article = document.querySelector("article");
article.lastElementChild.remove();

let h2 = document.querySelector("h2");

h2.addEventListener("click", function() {
    h2.style.backgroundColor = "red";
});

let h3 = document.querySelector("h3");

h3.addEventListener("click", function() {
    h3.style.display = "none";
});

let button = document.getElementById("boldBtn");
let paragraphs = document.querySelectorAll("article p");

button.addEventListener("click", function() {
    for (let p of paragraphs) {
        p.style.fontWeight = "bold";
    }
});

h1.addEventListener("mouseover", function() {
    let randomSize = Math.floor(Math.random() * 101);
    h1.style.fontSize = randomSize + "px";
});

let secondP = paragraphs[1];

secondP.addEventListener("mouseover", function() {
    secondP.style.opacity = "0";
    secondP.style.transition = "opacity 1s";
});
