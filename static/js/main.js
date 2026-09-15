function openGameModal(title, url) {
    const modal = document.getElementById("gameModal");
    const modalTitle = document.getElementById("modalTitle");
    const gameIframe = document.getElementById("gameIframe");

    if (modalTitle) modalTitle.innerText = title;
    if (gameIframe) gameIframe.src = url;
    if (modal) modal.style.display = "flex";
}

function closeGameModal() {
    const modal = document.getElementById("gameModal");
    const gameIframe = document.getElementById("gameIframe");

    if (gameIframe) gameIframe.src = ""; // Stops game audio on close
    if (modal) modal.style.display = "none";
}

function openOrigamiModal(id) {
    const dataElement = document.getElementById(`data-${id}`);
    if (!dataElement) {
        console.error(`Data script element "data-${id}" was not found.`);
        return;
    }

    try {
        const project = JSON.parse(dataElement.textContent);

        // Target Modal Elements
        const titleElem = document.getElementById('origamiTitle');
        const descElem = document.getElementById('origamiDescription');
        const videoElem = document.getElementById('origamiVideo');
        const imgElem = document.getElementById('origamiImage');
        const diagramElem = document.getElementById('origamiDiagram');
        const stepsContainer = document.getElementById('origamiSteps');

        // Populate Text and Media
        if (titleElem) titleElem.innerText = project.title || 'Origami Project';
        if (descElem) descElem.innerText = project.description || '';
        if (videoElem) videoElem.src = project.video_url || '';
        if (imgElem) imgElem.src = project.image || '';
        if (diagramElem) diagramElem.src = project.diagram_image || '';

        // Populate Step-by-Step Instructions List
        if (stepsContainer) {
            stepsContainer.innerHTML = '';
            if (project.steps && Array.isArray(project.steps)) {
                project.steps.forEach(step => {
                    const li = document.createElement('li');
                    li.innerText = step;
                    stepsContainer.appendChild(li);
                });
            }
        }

        // Show Origami Modal
        const modal = document.getElementById('origamiModal');
        if (modal) modal.style.display = 'flex';

    } catch (error) {
        console.error('Error parsing origami project JSON:', error);
    }
}

function closeOrigamiModal() {
    const modal = document.getElementById('origamiModal');
    const videoElem = document.getElementById('origamiVideo');
    
    // Clear video src to stop video audio on close
    if (videoElem) videoElem.src = '';
    if (modal) modal.style.display = 'none';
}

/* ==========================================================================
   GLOBAL CLICK EVENT (Close Modals on Background Click)
   ========================================================================== */

window.onclick = function(event) {
    const origamiModal = document.getElementById('origamiModal');
    const gameModal = document.getElementById('gameModal');

    if (event.target === origamiModal) {
        closeOrigamiModal();
    }
    
    if (event.target === gameModal) {
        closeGameModal();
    }
};