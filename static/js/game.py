import pygame
import sys
import random

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Desarrolladores - Estilo Matrix")

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Códigos a descifrar
codes = [
    "print('Hola Mundo')",  # Python
    "<?php echo 'Hola Mundo'; ?>",  # PHP
    "SELECT * FROM users;",  # SQL
    "console.log('Hola Mundo');",  # JavaScript
    "<h1>Hola Mundo</h1>",  # HTML
    "body { color: green; }",  # CSS
]

# Clase para el efecto de lluvia
class MatrixRain:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.columns = [0] * (screen.get_width() // font.get_height())

    def draw(self):
        for i, value in enumerate(self.columns):
            text = self.font.render(random.choice("0123456789ABCDEF"), True, GREEN)
            pos = (i * self.font.get_height(), value * self.font.get_height())
            self.screen.blit(text, pos)

            if value * self.font.get_height() > self.screen.get_height() and random.random() > 0.975:
                self.columns[i] = 0
            else:
                self.columns[i] += 1

# Ciclo principal del juego
def game_loop():
    running = True
    current_code = random.choice(codes)
    rain = MatrixRain(screen, font)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica del juego
        screen.fill(BLACK)

        # Efecto de lluvia de código
        rain.draw()

        # Mostrar el código a descifrar
        code_text = font.render(f"Descifra este código: {current_code}", True, GREEN)
        screen.blit(code_text, (50, 50))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()