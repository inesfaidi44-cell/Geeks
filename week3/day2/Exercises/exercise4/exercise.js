
// Exercise 4: Volume of a Sphere

let form = document.getElementById("MyForm");

let radius = document.getElementById("radius");
let volume = document.getElementById("volume");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    let r = Number(radius.value);

    let result = (4 / 3) * Math.PI * Math.pow(r, 3);

    volume.value = result.toFixed(2);

});
