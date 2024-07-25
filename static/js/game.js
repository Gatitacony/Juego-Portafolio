function preload() {
    this.load.image('jugador', 'static/images/hacker_personaje.png');
    this.load.image('protector', 'static/images/protector_personaje.png');
    this.load.image('matrix', 'static/images/matrix.jpg');
}

function create() {
    // Agregar la imagen de fondo primero
    var matrixImage = this.add.image(0, 0, 'matrix').setOrigin(0, 0);
    matrixImage.displayWidth = this.sys.canvas.width;
    matrixImage.displayHeight = this.sys.canvas.height;

    // Crear el personaje del jugador
    this.jugador = this.physics.add.image(100, 450, 'jugador');
    this.jugador.setCollideWorldBounds(true); // Para que el jugador no salga del área de juego

    // Crear el personaje del protector
    this.protector = this.physics.add.image(400, 300, 'protector');
    this.protector.setBounce(0.8);
    this.protector.setCollideWorldBounds(true);

    // Configurar teclas para movimiento
    this.cursors = this.input.keyboard.createCursorKeys();
}

function update() {
    // Verificar si las teclas de flecha están presionadas para mover al jugador
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

    // Ejemplo de movimiento automático del protector
    this.protector.setVelocityX(100);
}