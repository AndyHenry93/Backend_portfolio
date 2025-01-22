document.addEventListener('click', (e) => {
    if (e.target.classList.contains('expand-text')) {
        e.preventDefault();
        const textElement = e.target.previousElementSibling;
        const fullText = textElement.getAttribute('data-full-text') || textElement.textContent;

        if (e.target.textContent === "Expand") {
            textElement.textContent = fullText;
            e.target.textContent = "Collapse";
        } else {
            textElement.textContent = fullText.slice(0, 100) + '...';
            e.target.textContent = "Expand";
        }
    }
});