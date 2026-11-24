
const catalogItems = [
    {
        id: 1,
        name: "Gojo Satoru",
        anime: "Jujutsu Kaisen",
        category: "Hero",
        image: "https://i.servimg.com/u/f16/20/00/60/49/jujuts10.png",
        metric: 100,
        shortDescription: "The strongest Jujutsu Sorcerer, known for his incredible abilities.",
        fullDetails: "Gojo Satoru is a special grade sorcerer and teacher at Tokyo Jujutsu High. He possesses the Six Eyes and Limitless techniques."
    },
    {
        id: 2,
        name: "Yuji Itadori",
        anime: "Jujutsu Kaisen",
        category: "Hero",
        image: "https://images.everyeye.it/img-notizie/scopri-5-migliori-stregoni-jujutsu-kaisen-v3-764386-1200x1200.webp",
        metric: 85,
        shortDescription: "A brave student who becomes the vessel of Ryomen Sukuna.",
        fullDetails: "Yuji Itadori is a student at Tokyo Jujutsu High. He is known for his physical strength, courage and determination."
    },
    {
        id: 3,
        name: "Monkey D. Luffy",
        anime: "One Piece",
        category: "Hero",
        image: "https://images.everyeye.it/img-notizie/perchE-one-piece-non-introdotto-canti-marinareschi-veri-pirati-v3-816684-1200x1200.webp",
        metric: 98,
        shortDescription: "A pirate who dreams of becoming the King of the Pirates.",
        fullDetails: "Luffy is the captain of the Straw Hat Pirates. He has a rubber-like body and a strong desire for freedom and adventure."
    },
    {
        id: 4,
        name: "Roronoa Zoro",
        anime: "One Piece",
        category: "Hero",
        image: "https://i.pinimg.com/736x/d4/7c/9e/d47c9edcff2729de9131090d3a37b01e.jpg",
        metric: 95,
        shortDescription: "A powerful swordsman who dreams of becoming the world's greatest.",
        fullDetails: "Zoro is the swordsman of the Straw Hat Pirates. He is famous for his Three-Sword Style and incredible determination."
    },
    {
        id: 5,
        name: "Naruto Uzumaki",
        anime: "Naruto",
        category: "Hero",
        image: "https://anime-market.co.il/cdn/shop/collections/922cc4ce3a0e44a7d78ead8f67fe9762_1200x1200.jpg?v=1688320792",
        metric: 97,
        shortDescription: "A ninja who never gives up on his dream of becoming Hokage.",
        fullDetails: "Naruto is a ninja from the Hidden Leaf Village. He carries the Nine-Tailed Fox and becomes one of the strongest shinobi."
    },
    {
        id: 6,
        name: "Sasuke Uchiha",
        anime: "Naruto",
        category: "Anti-Hero",
        image: "https://upload.wikimedia.org/wikipedia/tr/b/b4/SasukeUchiha.png",
        metric: 96,
        shortDescription: "A talented ninja driven by revenge and the search for power.",
        fullDetails: "Sasuke belongs to the Uchiha clan. He possesses the Sharingan and follows a complicated path throughout his journey."
    },
    {
        id: 7,
        name: "Levi Ackerman",
        anime: "Attack on Titan",
        category: "Hero",
        image: "https://image.zeta-ai.io/profile-image/36dccb28-8ac7-461b-b404-0762833e4d2a/9742532b-2209-4b3a-b1db-29e81005ec78/fecd8262-41d5-4559-93e6-312c0bccf433.jpeg",
        metric: 94,
        shortDescription: "Humanity's strongest soldier, known for his combat skills.",
        fullDetails: "Levi Ackerman is a captain in the Survey Corps. He is famous for his exceptional speed, precision and discipline."
    },
    {
        id: 8,
        name: "Eren Yeager",
        anime: "Attack on Titan",
        category: "Anti-Hero",
        image: "https://wallpapers.com/images/hd/eren-yeager-intense-look-h7l9zqh4ax3kbzho.png",
        metric: 99,
        shortDescription: "A determined character whose desire for freedom changes everything.",
        fullDetails: "Eren Yeager is the main character of Attack on Titan. His journey transforms him from a young soldier into a controversial figure."
    },
    {
        id: 9,
        name: "Killua Zoldyck",
        anime: "Hunter x Hunter",
        category: "Hero",
        image: "https://www.looper.com/img/gallery/hunter-x-hunter-fans-sound-off-about-why-killua-is-the-star-of-the-show/l-intro-1667494654.jpg",
        metric: 91,
        shortDescription: "A young assassin with incredible speed and electrical abilities.",
        fullDetails: "Killua comes from the famous Zoldyck assassin family. He becomes Gon Freecss's closest friend and develops powerful Nen abilities."
    },
    {
        id: 10,
        name: "Gon Freecss",
        anime: "Hunter x Hunter",
        category: "Hero",
        image: "https://www.cultture.com/pics/2020/12/hunter-x-hunter-5-personajes-mas-inteligentes-que-killua-y-5-que-no-lo-son-1.jpg",
        metric: 88,
        shortDescription: "An energetic young Hunter searching for his father.",
        fullDetails: "Gon is an adventurous boy who becomes a Hunter. He is known for his strong determination and natural talent."
    },
    {
        id: 11,
        name: "Tanjiro Kamado",
        anime: "Demon Slayer",
        category: "Hero",
        image: "https://i.pinimg.com/736x/a5/e7/1f/a5e71f23895a0fbfd94ceebdaa6409ce.jpg",
        metric: 90,
        shortDescription: "A kind-hearted demon slayer who fights to protect his sister.",
        fullDetails: "Tanjiro joins the Demon Slayer Corps after his family is attacked by demons. He uses Water Breathing and later learns Sun Breathing."
    },
    {
        id: 12,
        name: "Light Yagami",
        anime: "Death Note",
        category: "Villain",
        image: "https://img.52tiemo.com/uploads/allimg/2023052010/hhwv2z5c3ty.jpg",
        metric: 93,
        shortDescription: "A brilliant student who discovers a notebook with deadly powers.",
        fullDetails: "Light Yagami discovers the Death Note and uses it to judge criminals. His actions lead to a battle of intelligence with detective L."
    }
];
