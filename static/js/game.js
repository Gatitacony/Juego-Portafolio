        // Create the application
        let app = new PIXI.Application({ width: 800, height: 600 });
        document.body.appendChild(app.view);

        // Load images
        PIXI.Loader.shared
            .add('background', 'ruta/a/tu/fondo.jpg')
            .add('character', 'ruta/a/tu/personaje.png')
            .load(setup);

        let character, background;

        function setup() {
            // Background
            background = new PIXI.Sprite(PIXI.Loader.shared.resources['background'].texture);
            app.stage.addChild(background);

            // Character
            character = new PIXI.Sprite(PIXI.Loader.shared.resources['character'].texture);
            character.x = 400;
            character.y = 300;
            character.anchor.set(0.5);
            app.stage.addChild(character);

            // Listen for frame updates
            app.ticker.add(delta => gameLoop(delta));
            
            // Listen for keyboard events
            window.addEventListener('keydown', onKeyDown);
            window.addEventListener('keyup', onKeyUp);
        }

        let keys = {};

        function onKeyDown(e) {
            keys[e.code] = true;
        }

        function onKeyUp(e) {
            keys[e.code] = false;
        }

        function gameLoop(delta) {
            // Character movement
            if (keys['ArrowLeft']) {
                character.x -= 5 * delta;
            }
            if (keys['ArrowRight']) {
                character.x += 5 * delta;
            }
            if (keys['ArrowUp']) {
                character.y -= 5 * delta;
            }
            if (keys['ArrowDown']) {
                character.y += 5 * delta;
            }

            // Check collisions (example with boundaries)
            if (character.x < 0) {
                character.x = 0;
            }
            if (character.x > app.screen.width) {
                character.x = app.screen.width;
            }
            if (character.y < 0) {
                character.y = 0;
            }
            if (character.y > app.screen.height) {
                character.y = app.screen.height;
            }
        }