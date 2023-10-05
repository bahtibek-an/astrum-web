let isDragging = false;
let startX;
let startScrollLeft;

const sliderContainer = document.querySelector('.wee-slider__slides');

sliderContainer.addEventListener('mousedown', (e) => {
    if (e.button !== 0) return;

    isDragging = true;
    startX = e.clientX;
    startScrollLeft = sliderContainer.scrollLeft;
    sliderContainer.style.cursor = 'grabbing';

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
});

sliderContainer.addEventListener('dragstart', (e) => {
    e.preventDefault();
});

function onMouseMove(e) {
    if (!isDragging) return;

    const x = e.clientX;
    const walk = (x - startX);
    sliderContainer.scrollLeft = startScrollLeft - walk;

    e.preventDefault(); 
}

function onMouseUp(e) {
    if (e.button !== 0) return;

    isDragging = false;
    sliderContainer.style.cursor = 'grab';
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
}
