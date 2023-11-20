'use strict';

// $(window).on('loader', function () {
//   $('[data-loader="circle-side"]').fadeOut(4400); // will first fade out the loading animation
//   $('#preloader').delay(4400).fadeOut('slow'); // will fade out the white DIV that covers the website.
//   $('body').delay(4400);
// });

/**
 * Add event listener on multiple elements
 */

const addEventOnElements = function (elements, eventType, callback) {
  for (let i = 0, len = elements.length; i < len; i++) {
    elements[i].addEventListener(eventType, callback);
  }
}



/**
 * MOBILE NAVBAR TOGGLER
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");

const toggleNav = () => {
  navbar.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNav);


//  ---------------------------------------------------  //
function checkVisible(elm) {
  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
  return !(rect.bottom < 0 || (rect.top - viewHeight + 300) >= 0);
}

function handleAboutContainer() {
  const aboutContainer = document.querySelector(".about-right-box");
  const bool = checkVisible(aboutContainer);
  if(bool) {
    aboutContainer.classList.add("is_active");
  } else {
    aboutContainer.classList.remove("is_active");
  }
}

if (window.matchMedia("(max-width: 900px)").matches) {
  window.addEventListener("scroll", handleAboutContainer);
}

// ----------------------------------------------------  //


/**
 * SLIDER
 */

// const slider = document.querySelector("[data-slider]");
// const sliderContainer = document.querySelector("[data-slider-container]");
// const sliderPrevBtn = document.querySelector("[data-slider-prev]");
// const sliderNextBtn = document.querySelector("[data-slider-next]");

// let totalSliderVisibleItems = Number(getComputedStyle(slider).getPropertyValue("--slider-items"));
// let totalSlidableItems = sliderContainer.childElementCount - totalSliderVisibleItems;

// let currentSlidePos = 0;

// const moveSliderItem = function () {
//   sliderContainer.style.transform = `translateX(-${sliderContainer.children[currentSlidePos].offsetLeft}px)`;
// }

/**
 * NEXT SLIDE
 */

// const slideNext = function () {
//   const slideEnd = currentSlidePos >= totalSlidableItems;

//   if (slideEnd) {
//     currentSlidePos = 0;
//   } else {
//     currentSlidePos++;
//   }

//   moveSliderItem();
// }

// sliderNextBtn.addEventListener("click", slideNext);

/**
 * PREVIOUS SLIDE
 */

// const slidePrev = function () {
//   if (currentSlidePos <= 0) {
//     currentSlidePos = totalSlidableItems;
//   } else {
//     currentSlidePos--;
//   }

//   moveSliderItem();
// }

// sliderPrevBtn.addEventListener("click", slidePrev);

/**
 * RESPONSIVE
 */
// window.addEventListener("resize", function () {
//   totalSliderVisibleItems = Number(getComputedStyle(slider).getPropertyValue("--slider-items"));
//   totalSlidableItems = sliderContainer.childElementCount - totalSliderVisibleItems;

//   moveSliderItem();
// }); 




// 
// const revealElements = document.querySelectorAll("[data-revele]");

// const scrollReveal = function () {
//     for (let i = 0, len = revealElements.length; i < len; i++) {
//         const isElementOnScreen = revealElements[i].getBoundingClientRect().top < window.innerHeight;

//         if (isElementOnScreen) {
//             revealElements[i].classList.add("revealed");
//         } else {
//             revealElements[i].classList.remove("reveale");
//         }
//     }
// };

// window.addEventListener("scroll", scrollReveal);
// window.addEventListener("load", scrollReveal);
// 
// const revealElements = document.querySelectorAll(".section");
// const isElementOnScreen = revealElements[i].getBoundingClientRect().top < window.innerHeight;

// document.addEventListener("DOMContentLoaded", function() {
//   var section = document.querySelector(".section");
  
//   setTimeout(function() {
//     section.classList.add("show");
//   }, 1000);
// });

function switchConfirmModal(type) {
  const confirmModal = document.querySelector(".confirm__modal");
  if(type) {
    confirmModal.classList.add("show");
    confirmModal.style.display = "block";
    return
  }
  confirmModal.classList.remove("show");
  confirmModal.style.display = "none";
}

function switchSuccessModal(type) {
  const successModal = document.querySelector(".success__modal");
  if(type) {
    successModal.classList.add("show");
    successModal.style.display = "block";
    return
  }
  successModal.classList.remove("show");
  successModal.style.display = "none";
}

document.querySelector(".btn-close__confirm-modal").addEventListener('click', () => {
  switchConfirmModal(false);
});

document.querySelector(".phone_number").addEventListener("input", function(e) {
  const input = e.target;
  const value = input.value.replace(/\D/g, "");  // Removes any non-digit characters
  
  let formatted = "+";

  if (value.length <= 3) {
      formatted += `(${value}`;
  } else if (value.length <= 5) {
      formatted += `(${value.slice(0, 3)}) ${value.slice(3)}`;
  } else if (value.length <= 8) {
      formatted += `(${value.slice(0, 3)}) ${value.slice(3, 5)}-${value.slice(5, 8)}`;
  } else if (value.length <= 10) {
      formatted += `(${value.slice(0, 3)}) ${value.slice(3, 5)}-${value.slice(5, 8)}-${value.slice(8, 10)}`;
  } else {
      formatted += `(${value.slice(0, 3)}) ${value.slice(3, 5)}-${value.slice(5, 8)}-${value.slice(8, 10)}-${value.slice(10, 12)}`;
  }

  input.value = formatted;
});



document.querySelector(".form__review").addEventListener("submit", (e) => {
  e.preventDefault();

  const fullName = document.querySelector(".full_name");
  const phoneNumber = document.querySelector(".phone_number");
  const nickName = document.querySelector(".nick_name");
  const csrf = document.querySelector('[name="csrfmiddlewaretoken"]');
  
  let phoneValue = phoneNumber.value.replace(/[+()\-\s]/g, '')

  const formData = new FormData();
  formData.append("full_name", fullName.value);
  formData.append("phone", phoneValue);
  formData.append("nick_name", nickName.value);
  formData.append("csrfmiddlewaretoken", csrf.value);

  const response = fetch("/send-message/", {
    method: "POST",
    body: formData,
  });

  switchConfirmModal(true);
});

document.querySelector(".confirm__btn").addEventListener("click", (e) => {
  const optCode = document.querySelector(".opt__code").value;
  const modalBackdrop = document.querySelector(".modal-backdrop");
  const modalOpen = document.querySelector(".modal-open");
  const nickName = document.querySelector(".nick_name").value;
  const fullName = document.querySelector(".full_name").value;
  const phoneNumber = document.querySelector(".phone_number").value.replace(/[+()\-\s]/g, '');
  const csrf = document.querySelector('[name="csrfmiddlewaretoken"]').value;

  const formData = new FormData();
  formData.append("phone", phoneNumber);
  formData.append("full_name", fullName);
  formData.append("code", optCode);
  formData.append("csrfmiddlewaretoken", csrf);
  formData.append("nick_name", nickName);

  fetch("/confirm_code/", {
    method: "POST",
    body: formData
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if(data.status === 'success') {
        switchConfirmModal(false);
        switchSuccessModal(true);
        return;
      }
      alert("Invalid code")
    });
})

document.querySelector(".close__success-modal").addEventListener("click", () => {
  const successModal = document.querySelector(".success__modal");
  successModal.classList.remove("active");
  successModal.classList.remove("show");
});

document.querySelector(".btnclose__confirm-modal").addEventListener("click", () => {
  const successModal = document.querySelector(".success__modal");
  successModal.classList.remove("active");
  successModal.classList.remove("show");
});

