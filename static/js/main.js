function openOrigamiModal(id) {
    const rawData = document.getElementById(`data-${id}`).textContent;
    const project = JSON.parse(rawData);

    document.getElementById('origamiTitle').innerText = project.title;
    document.getElementById('origamiDescription').innerText = project.description;
    document.getElementById('origamiVideo').src = project.video_url;
    document.getElementById('origamiImage').src = project.image;
    document.getElementById('origamiDiagram').src = project.diagram_image;

    // Render Steps List
    const stepsContainer = document.getElementById('origamiSteps');
    stepsContainer.innerHTML = '';
    project.steps.forEach(step => {
        const li = document.createElement('li');
        li.innerText = step;
        stepsContainer.appendChild(li);
    });

    document.getElementById('origamiModal').style.display = 'flex';
}

function closeOrigamiModal() {
    const modal = document.getElementById('origamiModal');
    document.getElementById('origamiVideo').src = ''; // Stop video audio on close
    modal.style.display = 'none';
}

// Close when clicking outside modal box
window.onclick = function(event) {
    const modal = document.getElementById('origamiModal');
    if (event.target === modal) {
        closeOrigamiModal();
    }
};