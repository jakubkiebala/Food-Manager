window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    const logoPlaceHeight = document.querySelector('.logo_place').offsetHeight;
    const content = document.querySelector('.content');

    if (window.scrollY > logoPlaceHeight) {
        navbar.classList.add('sticky');
        content.style.marginTop = navbar.offsetHeight + 'px';
    } else {
        navbar.classList.remove('sticky');
        content.style.marginTop = '0';
    }
});