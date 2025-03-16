import pygame

# Inicialización de Pygame
pygame.init()

# Nueva resolución y título
tamaño_ventana = (800, 600)
pantalla = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption("Super Haxball 2.0")

# Bucle principal del juego
en_juego = True
while en_juego:
    # Comprobamos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_juego = False

    # Se pinta la ventana con un color de fondo diferente
    pantalla.fill((0, 0, 0))  # Fondo negro

    # Actualización de la pantalla
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(120)  # Aumenté los FPS a 120

# Cierre de Pygame
pygame.quit()