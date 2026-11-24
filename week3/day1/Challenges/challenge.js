
const planets = [
    { name: "Mercury", color: "gray", moons: [] },
    { name: "Venus", color: "orange", moons: [] },
    { name: "Earth", color: "blue", moons: ["Moon"] },
    { name: "Mars", color: "red", moons: ["Phobos", "Deimos"] },
    { name: "Jupiter", color: "brown", moons: ["Io", "Europa", "Ganymede", "Callisto"] },
    { name: "Saturn", color: "gold", moons: ["Titan", "Enceladus"] },
    { name: "Uranus", color: "lightblue", moons: ["Miranda", "Ariel"] },
    { name: "Neptune", color: "darkblue", moons: ["Triton"] }
];

const section = document.querySelector(".listPlanets");

planets.forEach(planet => {

    const div = document.createElement("div");

    div.classList.add("planet");

    div.style.backgroundColor = planet.color;

    section.appendChild(div);

    planet.moons.forEach(moon => {

        const moonDiv = document.createElement("div");

        moonDiv.classList.add("moon");

        div.appendChild(moonDiv);

    });

});
