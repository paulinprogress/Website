document.addEventListener("DOMContentLoaded", () => {
    if (window.innerWidth > 1200) return;

    const row = document.querySelector(".home-image-row");
    if (!row) return;

    const images = row.querySelectorAll("img");
    if (!images.length) return;

    let current = 0;

    images[current].classList.add("active");

    setInterval(() => {
        images[current].classList.remove("active");
        current = (current + 1) % images.length;
        images[current].classList.add("active");
    }, 2000);
});