document.addEventListener("DOMContentLoaded", function() {
    function activeTextPhotoItem() {
        const photoItemList = document.querySelectorAll('.photo__item');
        let currentActive = null;
    
        document.addEventListener('scroll', function(e) {
            let mostCenteredItem = null;
            let smallestDistance = Infinity;  // Initialize with a large value
    
            for (let item of photoItemList) {
                let distanceToCenter = distanceFromCenter(item);
    
                // If this item's center is closer to the viewport's center than the previous items
                if (distanceToCenter < smallestDistance) {
                    smallestDistance = distanceToCenter;
                    mostCenteredItem = item;
                }
            }
    
            if (currentActive !== mostCenteredItem) {
                if (currentActive) {
                    currentActive.classList.remove('active');
                }
                if (mostCenteredItem) {
                    mostCenteredItem.classList.add('active');
                }
                currentActive = mostCenteredItem;
            }
        });
    
        function distanceFromCenter(elm) {
            const rect = elm.getBoundingClientRect();
            const viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
            const centerOfElm = rect.top + (rect.height / 2);
            const centerOfView = viewHeight / 2;
            
            return Math.abs(centerOfElm - centerOfView);
        }
    }
    activeTextPhotoItem();

    const imagesCarouselList = document.querySelector(".images__carousel-list");
    const photoItemList = document.querySelectorAll(".photo__item");

    function getSrcFromElement(elm) {
        let style = window.getComputedStyle(elm);
        let backgroundImage = style.backgroundImage;

        let url = backgroundImage.slice(4, -1).replace(/["']/g, "");
        return url;
    }

    photoItemList.forEach((photoItem) => {
        const src = getSrcFromElement(photoItem);
        const li = document.createElement('li');
        li.setAttribute('class', 'images__carousel-item');
        const imgEl = document.createElement('img');
        imgEl.setAttribute('src', src);
        li.appendChild(imgEl);
        imagesCarouselList.appendChild(li);
    });

    function startCarousel() {
        let modal = document.querySelector('.images__carousel');
        let closeBtn = document.querySelector('.images__carousel .close');
        let slides = document.querySelectorAll('.images__carousel-item');
        let currentSlide = 0;

        photoItemList.forEach((photoItem, index) => {
            photoItem.addEventListener('click', (event) => {
                modal.style.display = 'flex';
                currentSlide = index;
                showSlide(currentSlide);
            })
        });

        document.addEventListener('keydown', (event) => {
            if(event.keyCode !== 27) return;
            if(modal.style.display === 'flex') {
                modal.style.display = 'none';
            }
        });

        closeBtn.addEventListener('click', function() {
            modal.style.display = 'none';
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

});
