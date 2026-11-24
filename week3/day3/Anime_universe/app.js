
// 1. SELECT HTML ELEMENTS

const cardsGrid = document.getElementById("cards-grid");
const emptyState = document.getElementById("empty-state");

const searchInput = document.getElementById("search-input");
const categoryFilter = document.getElementById("category-filter");
const animeFilter = document.getElementById("anime-filter");
const sortSelect = document.getElementById("sort-select");

const characterModal = document.getElementById("character-modal");
const closeModal = document.getElementById("close-modal");
const modalContent = document.getElementById("modal-content");


// 2. DISPLAY CHARACTERS

function displayCharacters(characters) {

    cardsGrid.innerHTML = "";

    if (characters.length === 0) {
        emptyState.classList.remove("hidden");
        return;
    }

    emptyState.classList.add("hidden");

    characters.forEach(character => {

        const card = document.createElement("article");
        card.classList.add("card");

        card.innerHTML = `
            <img 
                src="${character.image}" 
                alt="${character.name}"
                class="card-image"
            >

            <div class="card-content">

                <span class="badge">
                    ${character.category}
                </span>

                <h3>${character.name}</h3>

                <p>${character.anime}</p>

                <p>${character.shortDescription}</p>

                <div class="metric">
                    Power: ${character.metric}/100
                </div>

                <button class="details-btn" data-id="${character.id}">
                    View Details
                </button>

            </div>
        `;

        cardsGrid.appendChild(card);
    });
}


// 3. SEARCH, FILTER AND SORT

function applyFilters() {

    let filteredCharacters = [...catalogItems];

    const searchTerm = searchInput.value.toLowerCase().trim();
    const selectedCategory = categoryFilter.value;
    const selectedAnime = animeFilter.value;
    const sortOption = sortSelect.value;



    if (searchTerm !== "") {

        filteredCharacters = filteredCharacters.filter(character =>
            character.name.toLowerCase().includes(searchTerm) ||
            character.anime.toLowerCase().includes(searchTerm) ||
            character.shortDescription.toLowerCase().includes(searchTerm)
        );
    }


    // FILTER BY CATEGORY

    if (selectedCategory !== "All") {

        filteredCharacters = filteredCharacters.filter(character =>
            character.category === selectedCategory
        );
    }


    // FILTER BY ANIME

    if (selectedAnime !== "All") {

        filteredCharacters = filteredCharacters.filter(character =>
            character.anime === selectedAnime
        );
    }


    // SORT CHARACTERS

    if (sortOption === "az") {

        filteredCharacters.sort((a, b) =>
            a.name.localeCompare(b.name)
        );

    } else if (sortOption === "za") {

        filteredCharacters.sort((a, b) =>
            b.name.localeCompare(a.name)
        );

    } else if (sortOption === "power") {

        // Highest power first
        filteredCharacters.sort((a, b) =>
            b.metric - a.metric
        );
    }


    displayCharacters(filteredCharacters);
}


// 4. EVENT LISTENERS FOR SEARCH AND FILTERS

searchInput.addEventListener("input", applyFilters);

categoryFilter.addEventListener("change", applyFilters);

animeFilter.addEventListener("change", applyFilters);

// Sort when the sorting option changes
sortSelect.addEventListener("change", applyFilters);


// 5. OPEN CHARACTER DETAILS MODAL

cardsGrid.addEventListener("click", function(event) {

    // Check if the clicked element is a View Details button
    const button = event.target.closest(".details-btn");

    if (!button) {
        return;
    }

    // Get the character ID from the button
    const characterId = Number(button.dataset.id);

    // Find the character in the original data
    const character = catalogItems.find(item =>
        item.id === characterId
    );

    // If the character doesn't exist, stop
    if (!character) {
        return;
    }

    // Display the character's complete information
    modalContent.innerHTML = `
        <img
            src="${character.image}"
            alt="${character.name}"
            class="card-image"
        >

        <h2>${character.name}</h2>

        <p><strong>Anime:</strong> ${character.anime}</p>

        <p><strong>Category:</strong> ${character.category}</p>

        <p><strong>Power:</strong> ${character.metric}/100</p>

        <p>${character.fullDetails}</p>
    `;

    characterModal.showModal();
});


// 6. CLOSE THE MODAL

// Close when clicking the close button
closeModal.addEventListener("click", function() {
    characterModal.close();
});

// Close when clicking outside the modal content
characterModal.addEventListener("click", function(event) {

    if (event.target === characterModal) {
        characterModal.close();
    }

});

// Display all characters when the page loads
applyFilters();
