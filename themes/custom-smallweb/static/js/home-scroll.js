const row = document.querySelector(".home-image-row");

if (row) {
  document.addEventListener("wheel", e => {
    row.scrollLeft += e.deltaY;
    e.preventDefault();
  }, { passive: false });
}