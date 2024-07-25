const canvas = document.getElementById('matrix');
const context = canvas.getContext('2d', { willReadFrequently: true });

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

function goBack() {
    location.reload();
}

function reloadPage() {
    location.reload();
}

function chooseRole(role) {
    if (role === 'observer') {
        window.location.href = 'portfolio.html';
    } else if (role === 'player') {
        document.getElementById('options').style.display = 'none';
        document.getElementById('startButtonContainer').style.display = 'block';
        document.getElementById('titulo').style.display = 'none';
        document.getElementById('parrafo').style.display = 'none';        
        document.getElementById('audioControls').style.display = 'block';  // Mostrar controles de audio
        playFireworks();
        document.getElementById('backgroundMusic').play();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const audio = document.getElementById('backgroundMusic');
    audio.play().catch(error => {
        console.log('Audio no apto para reproducción automática, necesita interacción del usuario');
    });
});

function toggleAudio() {
    const backgroundMusic = document.getElementById('backgroundMusic');
    if (backgroundMusic.paused) {
        backgroundMusic.play();
    } else {
        backgroundMusic.pause();
    }
}

function setVolume(volume) {
    const backgroundMusic = document.getElementById('backgroundMusic');
    backgroundMusic.volume = volume;
}

function startGame() {
    document.getElementById('startButton').style.display = 'none'; // Ocultar el botón "Iniciar Juego"
    window.location.href = "{{ url_for('start_game') }}";
}

function playFireworks() {
    const buttons = document.querySelectorAll('.option-button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            button.classList.add('explode');
            setTimeout(() => {
                button.classList.remove('explode');
            }, 500);
        });
    });
}

playFireworks();
