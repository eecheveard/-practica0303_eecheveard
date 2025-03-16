import pygame

pygame.init()

# Nueva resolución y título
tamaño_ventana = (960, 720)
ventana = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption("Ultimate Haxball")

# Carga el objeto pelota
pelota = pygame.image.load("ball.png")

# Obtengo el rectángulo del objeto pelota
rect_pelota = pelota.get_rect()

# Inicializo los valores con los que se va a mover la pelota
velocidad_pelota = [5, 4]  # Cambié la velocidad

# Coloco la pelota en el centro
rect_pelota.move_ip(tamaño_ventana[0] / 2, tamaño_ventana[1] / 2)

# Bucle principal del juego
en_juego = True
while en_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_juego = False

    # Muevo la pelota
    rect_pelota = rect_pelota.move(velocidad_pelota)

    # Comprobamos si la pelota llega a los límites de la ventana
    if rect_pelota.left < 0 or rect_pelota.right > ventana.get_width():
        velocidad_pelota[0] = -velocidad_pelota[0]
            
    if rect_pelota.top < 0 or rect_pelota.bottom > ventana.get_height():
        velocidad_pelota[1] = -velocidad_pelota[1]
    
    # Fondo de la ventana con nuevo color
    ventana.fill((100, 149, 237))  # Fondo azul claro

    # Dibujo la pelota
    ventana.blit(pelota, rect_pelota)

    pygame.display.flip()
    pygame.time.Clock().tick(90)  # Aumenté los FPS a 90

# Cierre de Pygame
pygame.quit()