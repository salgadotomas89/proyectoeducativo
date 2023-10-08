document.addEventListener('DOMContentLoaded', function () {
    var navbar = document.querySelector('.navbar');
    var megaMenu = document.querySelector('.mega-menu');
    var navbarItem = document.querySelector('.nav-item.colegio');
    var isMouseOnNavbarItem = false;
    var isMouseOnMegaMenu = false;

    // Obtain the height of the navbar and adjust the value of 'top' for the mega menu
    var navbarHeight = navbar.offsetHeight;
    megaMenu.style.top = navbarHeight + 'px';
    

    navbarItem.addEventListener('mouseenter', function () {
        isMouseOnNavbarItem = true;
        megaMenu.style.display = 'flex';  // Show the menu when the mouse enters the navbar item
    });

    navbarItem.addEventListener('mouseleave', function () {
        isMouseOnNavbarItem = false;
        setTimeout(function() {
            if (!isMouseOnMegaMenu) {
                megaMenu.style.display = 'none';  // Hide the menu if the mouse is not on the mega menu
            }
        }, 100);  // Slight delay to check for mouse on mega menu
    });

    megaMenu.addEventListener('mouseenter', function () {
        isMouseOnMegaMenu = true;
    });

    megaMenu.addEventListener('mouseleave', function () {
        isMouseOnMegaMenu = false;
        setTimeout(function() {
            if (!isMouseOnNavbarItem) {
                megaMenu.style.display = 'none';  // Hide the menu if the mouse is not back on the navbar item
            }
        }, 100);  // Slight delay to check for mouse back on navbar item
    });


   
   
});


