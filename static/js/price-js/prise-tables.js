document.addEventListener("DOMContentLoaded", function() {

	const priceSwitchBtnList = document.querySelectorAll(".pricing-switcher button");
	const priceItemList = document.querySelectorAll(".pricing__item");
	
	priceSwitchBtnList[0].addEventListener('click', function() {
		if(!this.classList.contains('active')) {
			this.classList.add('active');
			priceSwitchBtnList[1].classList.remove('active');
		}
		if(priceItemList[1].classList.contains('active')) {
			priceItemList[1].classList.remove('active');
			priceItemList[0].classList.add('active');
		}
	});
	priceSwitchBtnList[1].addEventListener('click', function() {
		if(!this.classList.contains('active')) {
			this.classList.add('active');
			priceSwitchBtnList[0].classList.remove('active');
		}
		if(priceItemList[0].classList.contains('active')) {
			priceItemList[0].classList.remove('active');
			priceItemList[1].classList.add('active');
		}
	});



	const accordionButton = document.querySelectorAll('.accordion-button');
	
	accordionButton.forEach((item) => {
		item.addEventListener("click", () => {
			const childBtn = item.querySelector('.accordion-header-btn')
			accordionButton.forEach((btn) => {
				const innerBtn = btn.querySelector('.accordion-header-btn');
				innerBtn.innerHTML = "Больше";
				innerBtn.classList.remove("active");
				btn.classList.add("collapsed")
				btn.nextElementSibling.classList.remove('show')
			});
			if(item.getAttribute('aria-expanded') === 'true') {
				childBtn.innerHTML = "Меньше";
				childBtn.classList.add("active")
				item.classList.remove('collapsed')
				return;
			}
			childBtn.innerHTML = "Больше";
			childBtn.classList.remove("active");
			item.classList.add('collapsed');
		
		})
	})



	document.querySelectorAll(".mentors__images-item").forEach((item) => {
		item.addEventListener("click", function() {
			const clickedElement = this;
			const imgSrc = clickedElement.querySelector(".mentors__images-img");
			const descriptionText = clickedElement.querySelector(".mentors__images-item-description").textContent;
			const jobType = clickedElement.querySelector(".mentors__images-item-job").textContent;
			const fullName = clickedElement.querySelector(".mentors__images-item-name").textContent;
			const jobTitle = clickedElement.querySelector(".mentors__images-item-spec").textContent;

			const mainImg = document.querySelector(".mentors__main-img img");
			const mainJobType = document.querySelector(".mentors__main-specialist");
			const mainFullName = document.querySelector(".mentors__main-info-name");
			const mainJobTitle = document.querySelector(".mentors__main-info-specialist");
			const mainDescription = document.querySelector(".mentors__main-info-text");
			console.log(this)
			mainImg.src = imgSrc.src;
			mainJobType.textContent = jobType;
			mainFullName.textContent = fullName;
			mainJobTitle.textContent = jobTitle;
			mainDescription.textContent = descriptionText;
		})
	})
});