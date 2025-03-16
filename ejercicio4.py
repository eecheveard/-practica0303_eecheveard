import pygame

# Definir el tamaño de la ventana
resolution = (960, 720)
white = (255, 255, 255)

class Ball:
    def __init__(self):
        self.x = resolution[0] / 4
        self.y = resolution[1] / 4
        self.radius = 20
        self.dx = 4
        self.dy = 4
        self.color = (255, 0, 0)  # Rojo

    def update(self, gameObjects):
        # Reducir la velocidad con el tiempo
        timer = pygame.time.get_ticks()
        if timer > 7500:
            timer = 0
            if self.dx > 0:
                self.dx -= 0.01
            elif self.dx < 0:
                self.dx += 0.01
            if self.dy > 0:
                self.dy -= 0.01
            elif self.dy < 0:
                self.dy += 0.01

        # Movimiento de la pelota
        self.x += self.dx
        self.y += self.dy

        # Colisión con los bordes
        if self.x - self.radius < 0 or self.x + self.radius > resolution[0]:
            self.dx = -self.dx
        if self.y - self.radius < 0 or self.y + self.radius > resolution[1]:
            self.dy = -self.dy

        # Colisión con el jugador (Player)
        for gameObj in gameObjects:
            if isinstance(gameObj, Player):
                if (gameObj.x - self.x)**2 + (gameObj.y - self.y)**2 <= (gameObj.radius + self.radius)**2:
                    self.dx = -(self.dx * 0.95)
                    self.dy = -(self.dy * 0.95)

                    if gameObj.keys[pygame.K_SPACE]:
                        self.dx = gameObj.dx
                        self.dy = gameObj.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Player:
    def __init__(self):
        self.x = resolution[0] / 2
        self.y = resolution[1] - 50
        self.radius = 30
        self.dx = 0
        self.dy = 0
        self.color = (0, 255, 0)  # Verde
        self.keys = pygame.key.get_pressed()

    def update(self, gameObjects):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT]:
            self.x -= 5
            self.dx = -5
        if self.keys[pygame.K_RIGHT]:
            self.x += 5
            self.dx = 5
        if self.keys[pygame.K_UP]:
            self.y -= 5
            self.dy = -5
        if self.keys[pygame.K_DOWN]:
            self.y += 5
            self.dy = 5

        # Evitar que el jugador se salga de la pantalla
        if self.x - self.radius < 0:
            self.x = self.radius
        if self.x + self.radius > resolution[0]:
            self.x = resolution[0] - self.radius
        if self.y - self.radius < 0:
            self.y = self.radius
        if self.y + self.radius > resolution[1]:
            self.y = resolution[1] - self.radius

        # Comprobamos las colisiones de la pelota con el jugador
        for gameObj in gameObjects:
            if isinstance(gameObj, Ball):
                gameObj.update(gameObjects)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Ball())
        self.gameObjects.append(Player())

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def run(self):
        while True:
            self.handleEvents()

            # Actualizar todos los objetos del juego
            for gameObj in self.gameObjects:
                gameObj.update(self.gameObjects)

            # Limpiar la pantalla
            self.screen.fill(white)

            # Dibujar todos los objetos del juego
            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            # Actualizar la pantalla
            pygame.display.flip()

            # Controlar los FPS
            self.clock.tick(60)

# Ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.run()