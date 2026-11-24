
const form = document.getElementById("libform");
const story = document.getElementById("story");
const shuffleButton = document.getElementById("shuffle-button");

let stories = [];
let currentIndex = -1;

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const noun = document.getElementById("noun").value.trim();
    const adjective = document.getElementById("adjective").value.trim();
    const person = document.getElementById("person").value.trim();
    const verb = document.getElementById("verb").value.trim();
    const place = document.getElementById("place").value.trim();

    if (
        noun === "" ||
        adjective === "" ||
        person === "" ||
        verb === "" ||
        place === ""
    ) {
        alert("Please fill in all the fields!");
        return;
    }

    stories = [
        `One day, ${person} saw a ${adjective} ${noun} in ${place} and decided to ${verb}.`,

        `${person} went to ${place} with a ${adjective} ${noun} to ${verb} all day.`,

        `Yesterday, a ${adjective} ${noun} followed ${person} to ${place} while trying to ${verb}.`
    ];

    currentIndex = Math.floor(Math.random() * stories.length);

    story.textContent = stories[currentIndex];

    shuffleButton.disabled = false;

});

shuffleButton.addEventListener("click", function() {

    let newIndex;

    do {
        newIndex = Math.floor(Math.random() * stories.length);
    } while (newIndex === currentIndex);

    currentIndex = newIndex;

    story.textContent = stories[currentIndex];

});
