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

function startCarousel() {
    let modal = document.querySelector('.images__carousel');
    let closeBtn = document.querySelector('.images__carousel .close');
    let slides = document.querySelectorAll('.images__carousel-item');
    const sectionImg = document.querySelector('.first__section-img');
    let currentSlide = 0;

    sectionImg.addEventListener('click', (event) => {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
        showSlide(currentSlide);
    })

    document.addEventListener('keydown', (event) => {
        if(event.keyCode !== 27) return;
        if(modal.style.display === 'flex') {
            modal.style.display = 'none';
        }
    });

    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    });

    document.querySelector('.next').addEventListener('click', function() {
        showSlide(currentSlide += 1);
    });

    document.querySelector('.prev').addEventListener('click', function() {
        showSlide(currentSlide -= 1);
    });

    function showSlide(n) {
        if (n >= slides.length) {currentSlide = 0}
        if (n < 0) {currentSlide = slides.length - 1}

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none"; 
        }

        slides[currentSlide].style.display = "block";
    }
}
startCarousel();