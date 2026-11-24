
// Exercise 5: Users

let container = document.getElementById("container");
console.log(container);

let firstList = document.querySelector(".list");
firstList.children[1].textContent = "Richard";

let lists = document.querySelectorAll(".list");
lists[1].children[1].remove();

for (let list of lists) {
    list.children[0].textContent = "Ines";
}

for (let list of lists) {
    list.classList.add("student_list");
}

lists[0].classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

lists[1].children[1].style.display = "none";

lists[0].children[1].style.border = "1px solid black";

document.body.style.fontSize = "18px";

if (container.style.backgroundColor === "lightblue") {
    let x = lists[0].children[0].textContent;
    let y = lists[1].children[0].textContent;

    alert("Hello " + x + " and " + y);
}
