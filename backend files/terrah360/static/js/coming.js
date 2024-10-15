// JavaScript for Popup
const notifyButton = document.querySelector('.notify');
const popup = document.getElementById('popup');
const closeBtn = document.getElementById('close-btn');

notifyButton.addEventListener('click', (e) => {
    e.preventDefault(); // Prevent link behavior
    popup.style.display = 'flex';
});

closeBtn.addEventListener('click', () => {
    popup.style.display = 'none';
});

window.addEventListener('click', (e) => {
    if (e.target === popup) {
        popup.style.display = 'none';
    }
});