window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    const logoPlaceHeight = document.querySelector('.logo_place').offsetHeight;
    const content = document.querySelector('.content_structure');

    if (window.scrollY > logoPlaceHeight) {
        navbar.classList.add('sticky');
        content.style.marginTop = navbar.offsetHeight + 'px';
    } else {
        navbar.classList.remove('sticky');
        content.style.marginTop = '0';
    }
});


function toggleBurgerMenu() {
    const burgerMenu = document.getElementById('burgerMenu');
    burgerMenu.style.display = (burgerMenu.style.display === 'flex') ? 'none' : 'flex';
}

function toggleUserMenu() {
    const userMenu = document.getElementById('userMenu');
    userMenu.style.display = (userMenu.style.display === 'flex') ? 'none' : 'flex';
}

window.addEventListener('click', function(event) {
    const burgerMenu = document.getElementById('burgerMenu');
    const burgerIcon = document.querySelector('.burger_icon');
    const userMenu = document.getElementById('userMenu');
    const userIcon = document.querySelector('.user_icon');

    if (!burgerMenu.contains(event.target) && !burgerIcon.contains(event.target)) {
        burgerMenu.style.display = 'none';
    }

    if (!userMenu.contains(event.target) && !userIcon.contains(event.target)) {
        userMenu.style.display = 'none';
    }
});