function startGame() {
    if (!gameStarted) {
        gameStarted = true;
        document.getElementById('startButton').style.display = 'none'; // Ocultar el botón "Iniciar Juego"
        document.getElementById('audioControls').style.display = 'block'; // Mostrar controles de audio

        const config = {
            type: Phaser.AUTO,
            width: 1000,
            height: 765,
            physics: {
                default: 'arcade',
                arcade: {
                    gravity: { y: 0 },
                    debug: false
                }
            },
            scene: {
                preload: preload,
                create: create,
                update: update
            }
        };

        const game = new Phaser.Game(config);
    }
}

let gameStarted = false;

