
// Exercise 3: Transform the sentence

let allBoldItems;

function getBoldItems() {
    allBoldItems = document.querySelectorAll("strong");
}

function highlight() {
    for (let item of allBoldItems) {
        item.style.color = "blue";
    }
}

function returnItemsToDefault() {
    for (let item of allBoldItems) {
        item.style.color = "black";
    }
}


let paragraph = document.querySelector("p");

getBoldItems();

paragraph.addEventListener("mouseover", highlight);

paragraph.addEventListener("mouseout", returnItemsToDefault);
