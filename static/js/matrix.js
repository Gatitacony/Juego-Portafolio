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

function startGame() {
    if (!gameStarted) {
        gameStarted = true;
        document.getElementById('gameCanvas').style.display = 'block';
        const config = {
            type: Phaser.AUTO,
            width: 800,
            height: 600,
            backgroundColor: '#1679AB',
            physics: {
                default: 'arcade',
                arcade: {
                    gravity: { y: 200 }
                }
            },
            scene: {
                preload: preload,
                create: create,
                update: update
            }
        };

        const game = new Phaser.Game(config);

        function preload() {
            this.load.image('jugador', 'static/images/hacker.png');
        }
        
        function create() {
            // Crear el personaje del jugador
            this.jugador = this.physics.add.image(100, 450, 'jugador');
            this.jugador.setCollideWorldBounds(true); // Para que el jugador no salga del área de juego
        
            // Aquí puedes añadir más configuraciones y comportamientos al jugador
        }                        

        function update() {
            // Ejemplo básico de movimiento del jugador con las teclas de flecha
            if (this.cursors.left.isDown) {
                this.jugador.setVelocityX(-160);
            } else if (this.cursors.right.isDown) {
                this.jugador.setVelocityX(160);
            } else {
                this.jugador.setVelocityX(0);
            }
        
            if (this.cursors.up.isDown) {
                this.jugador.setVelocityY(-160);
            } else if (this.cursors.down.isDown) {
                this.jugador.setVelocityY(160);
            } else {
                this.jugador.setVelocityY(0);
            }
        }
        
    

        function preload() {
            this.load.image('protector', 'static/images/personaje-protector.png');
        }
        
        function create() {
            this.protector = this.physics.add.image(400, 300, 'protector');
            this.protector.setBounce(0.8);
            this.protector.setCollideWorldBounds(true);
        
            // Configurar teclas para movimiento
            this.cursors = this.input.keyboard.createCursorKeys();
        }
        
        
        function update() {
            this.ball.setVelocityX(100);
        }
    }
}

let gameStarted = false;

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
