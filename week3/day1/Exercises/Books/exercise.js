
// Exercise 7: My Book List

const allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://covers.openlibrary.org/b/isbn/9780747532699-M.jpg",
        alreadyRead: true
    },

    {
        title: "The Alchemist",
        author: "Paulo Coelho",
        image: "https://covers.openlibrary.org/b/isbn/9780062315007-M.jpg",
        alreadyRead: false
    }
];

let section = document.querySelector(".listBooks");

for (let book of allBooks) {

    let div = document.createElement("div");

    let details = document.createElement("p");

    details.textContent = book.title + " written by " + book.author;

    let img = document.createElement("img");

    img.src = book.image;
    img.style.width = "100px";

    if (book.alreadyRead === true) {
        details.style.color = "red";
    }

    div.appendChild(details);
    div.appendChild(img);

    section.appendChild(div);
}
