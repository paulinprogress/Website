document.addEventListener("DOMContentLoaded", () => {
    const row = document.querySelector(".home-image-row");
    if (!row) return;

    const images = row.querySelectorAll("img");
    if (!images.length) return;

    let current = 0;
    let interval = null;

    const isMobile = () => window.innerWidth <= 600;

    const start = () => {
        if (interval || !isMobile()) return;

        images[current].classList.add("active");

        interval = setInterval(() => {
            images[current].classList.remove("active");
            current = (current + 1) % images.length;
            images[current].classList.add("active");
        }, 2000);
    };

    const stop = () => {
        if (!interval) return;

        clearInterval(interval);
        interval = null;

        images.forEach(img => img.classList.remove("active"));
        current = 0;
    };

    const update = () => {
        if (isMobile()) {
            start();
        } else {
            stop();
        }
    };

    update();
    window.addEventListener("resize", update);
});