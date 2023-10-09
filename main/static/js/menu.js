document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.querySelector('.navbar');
    const megaMenu = document.querySelector('.mega-menu');
    const navbarItem = document.querySelector('.nav-item.colegio');

    // Check if the elements exist before proceeding
    if (!navbar || !megaMenu || !navbarItem) return;

    let isMouseOnNavbarItem = false;
    let isMouseOnMegaMenu = false;

    const navbarHeight = navbar.offsetHeight;
    megaMenu.style.top = `${navbarHeight}px`;

    const toggleMegaMenu = (show) => {
        megaMenu.style.display = show ? 'flex' : 'none';
    };

    navbarItem.addEventListener('mouseenter', function () {
        isMouseOnNavbarItem = true;
        toggleMegaMenu(true);
    });

    navbarItem.addEventListener('mouseleave', function () {
        isMouseOnNavbarItem = false;
        setTimeout(function() {
            if (!isMouseOnMegaMenu) {
                toggleMegaMenu(false);
            }
        }, 100);
    });

    megaMenu.addEventListener('mouseenter', function () {
        isMouseOnMegaMenu = true;
    });

    megaMenu.addEventListener('mouseleave', function () {
        isMouseOnMegaMenu = false;
        setTimeout(function() {
            if (!isMouseOnNavbarItem) {
                toggleMegaMenu(false);
            }
        }, 100);
    });

    const hamburgerBtn = document.getElementById("hamburger-btn");
    const dropdown = document.getElementById("hamburger-dropdown");

    // Check if the elements exist before proceeding
    if (hamburgerBtn && dropdown) {
        hamburgerBtn.addEventListener("click", function() {
            dropdown.classList.toggle("active");
        });
    }

    const submenuParents = document.querySelectorAll('.submenu-parent');

    submenuParents.forEach(parent => {
        parent.addEventListener('click', function(event) {
            const submenu = parent.querySelector('.submenu');
            if (submenu.style.display === 'flex') {
                submenu.style.display = 'none';
            } else {
                submenu.style.display = 'flex';
            }
            event.stopPropagation();  // prevent event from bubbling up
        });
    });

    // Close all submenus if user clicks outside
    document.addEventListener('click', function() {
        const allSubmenus = document.querySelectorAll('.submenu');
        allSubmenus.forEach(submenu => {
            submenu.style.display = 'none';
        });
    });

    
    

});
