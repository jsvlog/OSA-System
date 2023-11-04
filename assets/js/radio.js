
const option1 = document.getElementById('option1');
const option2 = document.getElementById('option2');
const page1 = document.getElementById('DisplayTo');
const page2 = document.getElementById('DisplayFrom');

option1.addEventListener('change', () => {
    if (option1.checked) {
        page1.style.display = 'block';
        page2.style.display = 'none';
    }
});

option2.addEventListener('change', () => {
    if (option2.checked) {
        page1.style.display = 'none';
        page2.style.display = 'block';
    }
});
