function openGameModal(title, url) {
    const modal = document.getElementById("gameModal");
    const modalTitle = document.getElementById("modalTitle");
    const gameIframe = document.getElementById("gameIframe");

    modalTitle.innerText = title;
    gameIframe.src = url;
    modal.style.display = "flex";
}

function closeGameModal() {
    const modal = document.getElementById("gameModal");
    const gameIframe = document.getElementById("gameIframe");

    // Clear source to stop audio/game in background when closed
    gameIframe.src = "";
    modal.style.display = "none";
}

// Close modal if user clicks outside the modal box
window.onclick = function(event) {
    const modal = document.getElementById("gameModal");
    if (event.target === modal) {
        closeGameModal();
    }
}