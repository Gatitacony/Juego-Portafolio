const canvas = document.getElementById('matrix');
const context = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const letters = Array(256).join(1).split('');

const draw = () => {
    context.fillStyle = 'rgba(0, 0, 0, 0.05)'; // Fondo semi-transparente para el efecto de desvanecimiento
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = '#00ff00'; // Color del texto de la "Matrix"
    context.font = '16pt monospace';

    letters.map((y_pos, index) => {
        const text = String.fromCharCode(65 + Math.random() * 33);
        const x_pos = index * 20;
        context.fillText(text, x_pos, y_pos);

        letters[index] = y_pos > canvas.height + Math.random() * 1e4 ? 0 : y_pos + 20;
    });
};

setInterval(draw, 33);

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

function startGame() {
    fetch('/start_game')
        .then(response => response.text())
        .then(data => {
            alert(data);
            document.getElementById('startButtonContainer').style.display = 'none';
            document.getElementById('skillCarousel').style.display = 'block';
            document.getElementById('gameInfo').style.display = 'block';
            $('.owl-carousel').owlCarousel({
                loop: true,
                margin: 10,
                nav: true,
                responsive: {
                    0: {
                        items: 1
                    },
                    600: {
                        items: 3
                    },
                    1000: {
                        items: 5
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}

function reloadPage() {
    location.reload();
}