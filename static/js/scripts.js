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

