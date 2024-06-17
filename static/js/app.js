       document.addEventListener("DOMContentLoaded", () => {
           // Select all dropdown toggle buttons
           const dropdownToggles = document.querySelectorAll(".dropdown-toggle")

           dropdownToggles.forEach((toggle) => {
               toggle.addEventListener("click", () => {
                   // Find the next sibling element which is the dropdown menu
                   const dropdownMenu = toggle.nextElementSibling

                   // Toggle the 'hidden' class to show or hide the dropdown menu
                   if (dropdownMenu.classList.contains("hidden")) {
                       // Hide any open dropdown menus before showing the new one
                       document.querySelectorAll(".dropdown-menu").forEach((menu) => {
                           menu.classList.add("hidden")
                       })

                       dropdownMenu.classList.remove("hidden")
                   } else {
                       dropdownMenu.classList.add("hidden")
                   }
               })
           })

           // Clicking outside of an open dropdown menu closes it
           window.addEventListener("click", function (e) {
               if (!e.target.matches(".dropdown-toggle")) {
                   document.querySelectorAll(".dropdown-menu").forEach((menu) => {
                       if (!menu.contains(e.target)) {
                           menu.classList.add("hidden")
                       }
                   })
               }
           })

           // Mobile menu toggle

           const mobileMenuButton = document.querySelector('.mobile-menu-button')
           const mobileMenu = document.querySelector('.navigation-menu')

           mobileMenuButton.addEventListener('click', () => {
               mobileMenu.classList.toggle('hidden')
           })


       })

       new Swiper(".swiper", {
//           effect: "coverflow",
           grabCursor: true,
           centeredSlides: true,
           loop: true,
           slidesPerView: 1,
           spaceBetween: 10,
//           coverflowEffect: {
//               rotate: 20,
//               stretch: 0,
//               depth: 100,
//               modifier: 1,
//               slideShadows: true,
//           },
           breakpoints: {
               640: {
                   slidesPerView: 2,
                   spaceBetween: 20,
                  
               },
               768: {
                   slidesPerView: 3,
                   spaceBetween: 30,
               },
               1024: {
                   slidesPerView: 3,
                   spaceBetween: 40,
               },
           },

           //           autoplay: {
           //               delay: 2500,
           //               disableOnInteraction: false,
           //           },
//           pagination: {
//               el: ".swiper-pagination",
//           },
           navigation: {
               nextEl: ".swiper-button-next",
               prevEl: ".swiper-button-prev",
           },


       });
