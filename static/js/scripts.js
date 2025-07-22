const cards = document.querySelectorAll(".card");
const dropZone = document.getElementById("activation-zone");
const log = document.getElementById("log");

cards.forEach(card => {
  card.addEventListener("dragstart", e => {
    e.dataTransfer.setData("text/plain", card.dataset.type);
    e.dataTransfer.effectAllowed = "move";
  });
});

dropZone.addEventListener("dragover", e => {
  e.preventDefault();
  dropZone.style.backgroundColor = "#d4ffd4";
});

dropZone.addEventListener("dragleave", e => {
  dropZone.style.backgroundColor = "#ffffffaa";
});

dropZone.addEventListener("drop", e => {
  e.preventDefault();
  dropZone.style.backgroundColor = "#ffffffaa";
  const cardType = e.dataTransfer.getData("text/plain");

  if (cardType) {
    log.textContent = `Activated a ${cardType.toUpperCase()} card!`;
  }
});
