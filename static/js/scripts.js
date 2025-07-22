document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");
  const dropZone = document.getElementById("activation-zone");
  const log = document.getElementById("log");
  const gameLog = document.getElementById("game-log");

  const startBtn = document.getElementById("start-btn");
  const attackBtn = document.getElementById("attack-btn");

  startBtn.addEventListener("click", () => {
    fetch("/game/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ player_name: "Hero" })
    })
      .then(res => res.json())
      .then(data => {
        gameLog.innerText = data.message;
      });
  });

  attackBtn.addEventListener("click", () => {
    fetch("/game/attack", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ player_name: "Hero", enemy: "Goblin" })
    })
      .then(res => res.json())
      .then(data => {
        gameLog.innerText = data.result;
      });
  });

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

  dropZone.addEventListener("dragleave", () => {
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
});
