
// Exercise 1 : Create Video Class

class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    // 2.
    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }
}


// Exercise 2 : Create First Video Instance

const video1 = new Video("JavaScript Tutorial", "Ines", 3600);

video1.watch();


// Exercise 3 : Create Second Video Instance

const video2 = new Video("Python for Beginners", "Sarah", 1800);

video2.watch();


// Exercise 4 : Store Data for Five Videos

const videosData = [
    ["HTML Tutorial", "John", 1200],
    ["CSS Tutorial", "Sarah", 900],
    ["JavaScript Basics", "Ines", 2400],
    ["Python Course", "Ahmed", 3600],
    ["React Tutorial", "Emma", 1800]
];


// Exercise 5 : Instantiate Videos Using a Loop

const videos = [];

videosData.forEach(video => {
    const newVideo = new Video(video[0], video[1], video[2]);

    videos.push(newVideo);
});


// Exercise 6 : Display All Videos

videos.forEach(video => {
    video.watch();
});
