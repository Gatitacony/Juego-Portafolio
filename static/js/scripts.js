function togglePasswordVisibility(inputId, eyeIcon) {
    const input = document.getElementById(inputId);
    if (input.type === "password") {
        input.type = "text";
        eyeIcon.querySelector('i').classList.remove('fa-eye');
        eyeIcon.querySelector('i').classList.add('fa-eye-slash');
    } else {
        input.type = "password";
        eyeIcon.querySelector('i').classList.remove('fa-eye-slash');
        eyeIcon.querySelector('i').classList.add('fa-eye');
    }
}

function startGame() {
    document.getElementById('startButtonContainer').style.display = 'none';
    document.getElementById('skillCarousel').style.display = 'block';
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        nav:true,
        dots:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            }
        }
    });
}
