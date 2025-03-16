import pygame

pygame.init()

# Nueva resolución y título
tamaño_ventana = (960, 720)
ventana = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption("Haxball Deluxe")

# Carga el objeto pelota
pelota = pygame.image.load("ball.png")
rect_pelota = pelota.get_rect()
velocidad_pelota = [4, 4]
velocidad_jugador1 = [0, 0]

# Coloco la pelota en la esquina superior izquierda
rect_pelota.move_ip(tamaño_ventana[0] / 4, tamaño_ventana[1] / 4)

# Crea el objeto jugador y su rectángulo
jugador1 = pygame.image.load("player1.png")
rect_jugador1 = jugador1.get_rect()

# Coloco el jugador1 en la parte inferior de la pantalla
rect_jugador1.move_ip(tamaño_ventana[0] / 2 - rect_jugador1.width / 2, tamaño_ventana[1] - rect_jugador1.height)

# Bucle principal del juego
en_juego = True
while en_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_juego = False

    # Movimiento del jugador1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_jugador1 = rect_jugador1.move(-5, 0)  # Aumenté la velocidad del jugador
        velocidad_jugador1[0] = -5
    if keys[pygame.K_RIGHT]:
        rect_jugador1 = rect_jugador1.move(5, 0)
        velocidad_jugador1[0] = 5
    if keys[pygame.K_UP]:
        rect_jugador1 = rect_jugador1.move(0, -5)  # Aumenté la velocidad
        velocidad_jugador1[1] = -5
    if keys[pygame.K_DOWN]:
        rect_jugador1 = rect_jugador1.move(0, 5)
        velocidad_jugador1[1] = 5

    # Movimiento de la pelota
    rect_pelota = rect_pelota.move(velocidad_pelota)

    # Colisión de la pelota con los bordes
    if rect_pelota.left < 0 or rect_pelota.right > ventana.get_width():
        velocidad_pelota[0] = -velocidad_pelota[0]
    if rect_pelota.top < 0 or rect_pelota.bottom > ventana.get_height():
        velocidad_pelota[1] = -velocidad_pelota[1]

    # Colisión entre pelota y jugador1 (simplificada)
    if rect_pelota.colliderect(rect_jugador1):
        velocidad_pelota[1] = -velocidad_pelota[1]  # Rebote de la pelota

    # Limpio la ventana con un nuevo color de fondo
    ventana.fill((135, 206, 235))  # Fondo azul cielo

    # Dibujo la pelota
    ventana.blit(pelota, rect_pelota)

    # Dibujo al jugador1
    ventana.blit(jugador1, rect_jugador1)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Cierre de Pygame
pygame.quit()