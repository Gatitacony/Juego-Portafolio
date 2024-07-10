import pygame
import sys
import random

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Juego de Desarrolladores - Estilo Matrix")

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Preguntas y respuestas de sí o no
questions = [
    {"question": "¿Python es un lenguaje de programación?", "answer": "sí"},
    {"question": "¿HTML es un lenguaje de programación?", "answer": "no"},
    {"question": "¿CSS se usa para diseñar páginas web?", "answer": "sí"},
    {"question": "¿JavaScript puede ejecutarse en el servidor?", "answer": "sí"},
    {"question": "¿SQL es un lenguaje de marcas?", "answer": "no"},
    {"question": "¿PHP es un lenguaje de scripting?", "answer": "sí"},
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

# Clase para el personaje
class Character:
    def __init__(self):
        self.rect = pygame.Rect(100, screen.get_height() - 150, 50, 50)
        self.speed = 5
        self.jump_height = 15
        self.is_jumping = False
        self.jump_velocity = self.jump_height

    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True

        if self.is_jumping:
            self.rect.y -= self.jump_velocity
            self.jump_velocity -= 1
            if self.jump_velocity < -self.jump_height:
                self.is_jumping = False
                self.jump_velocity = self.jump_height
        else:
            self.rect.y = screen.get_height() - 150

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

# Clase para la explosión
class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        for _ in range(100):
            angle = random.uniform(0, 2 * 3.14159)
            speed = random.uniform(2, 5)
            self.particles.append([self.x, self.y, speed * pygame.math.Vector2(1, 0).rotate_rad(angle)])

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, random.choice([RED, YELLOW]), (int(particle[0]), int(particle[1])), 3)

    def update(self):
        for particle in self.particles:
            particle[0] += particle[2].x
            particle[1] += particle[2].y
            particle[2] *= 0.95  # Slow down over time

# Clase para la bomba
class Bomb:
    def __init__(self):
        self.rect = pygame.Rect(700, screen.get_height() - 150, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

# Ciclo principal del juego
def game_loop():
    running = True
    current_question = random.choice(questions)
    rain = MatrixRain(screen, font)
    character = Character()
    bomb = Bomb()

    # Configuración de las respuestas
    yes_rect = pygame.Rect(400, screen.get_height() - 300, 100, 50)
    no_rect = pygame.Rect(600, screen.get_height() - 300, 100, 50)

    answer_message = ""
    display_answer_time = 0
    explosion = None
    new_question_delay = 2000  # 2 seconds delay
    lives = 5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()

        # Lógica del juego
        screen.fill(BLACK)

        # Efecto de lluvia de código
        rain.draw()

        # Mostrar la pregunta actual
        question_text = font.render(f"Pregunta: {current_question['question']}", True, GREEN)
        screen.blit(question_text, (50, 50))

        # Movimiento del personaje
        character.move(keys)

        # Dibujar el personaje
        character.draw(screen)

        # Dibujar las respuestas
        pygame.draw.rect(screen, GREEN, yes_rect)
        pygame.draw.rect(screen, GREEN, no_rect)
        yes_text = font.render("Sí", True, BLACK)
        no_text = font.render("No", True, BLACK)
        screen.blit(yes_text, (yes_rect.x + 25, yes_rect.y + 10))
        screen.blit(no_text, (no_rect.x + 25, no_rect.y + 10))

        # Dibujar la bomba
        bomb.draw(screen)

        # Dibujar las vidas
        lives_text = font.render(f"Vidas: {lives}", True, WHITE)
        screen.blit(lives_text, (10, 10))

        # Colisiones con respuestas
        if character.rect.colliderect(yes_rect) or character.rect.colliderect(no_rect):
            answer = "sí" if character.rect.colliderect(yes_rect) else "no"
            if answer == current_question["answer"]:
                answer_message = "Correcto"
                explosion = Explosion(character.rect.x, character.rect.y)
            else:
                answer_message = "Incorrecto"
                lives -= 1
                if lives == 0:
                    running = False  # Fin del juego

            display_answer_time = pygame.time.get_ticks()

            # Elegir una nueva pregunta después de un breve tiempo
            current_question = random.choice(questions)

        # Mostrar el mensaje de la respuesta
        if answer_message:
            elapsed_time = pygame.time.get_ticks() - display_answer_time
            if elapsed_time < new_question_delay:  # Mostrar el mensaje por un período
                message = font.render(answer_message, True, WHITE)
                screen.blit(message, (character.rect.x, character.rect.y - 30))
                if explosion:
                    explosion.draw(screen)
                    explosion.update()
            else:
                answer_message = ""
                explosion = None

        # Mostrar mensaje de avance
        if character.rect.x > screen.get_width() - 100:
            display_message("Sigues vivo... por ahora!!", (screen.get_width() // 2 - 100, screen.get_height() - 100))

        pygame.display.flip()

    # Fin del juego
    pygame.quit()
    sys.exit()

# Función para mostrar mensajes
def display_message(message, position):
    text = font.render(message, True, GREEN)
    screen.blit(text, position)

if __name__ == '__main__':
    game_loop()
