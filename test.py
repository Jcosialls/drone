from djitellopy import Tello
import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre Pygame (non affichée)
pygame.display.set_mode((1, 1))

# Connexion au drone Tello
tello = Tello()
tello.connect()
tello.takeoff()

# Définir la vitesse de déplacement du drone (ajustez selon vos besoins)
speed = 50

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tello.send_rc_control(0, speed, 0, 0)  # Avancer
            elif event.key == pygame.K_DOWN:
                tello.send_rc_control(0, -speed, 0, 0)  # Reculer
            elif event.key == pygame.K_LEFT:
                tello.send_rc_control(-speed, 0, 0, 0)  # Aller à gauche
            elif event.key == pygame.K_RIGHT:
                tello.send_rc_control(speed, 0, 0, 0)  # Aller à droite

        elif event.type == pygame.KEYUP:
            tello.send_rc_control(0, 0, 0, 0)  # Arrêter les mouvements

        elif event.type == pygame.QUIT:
            running = False

# Atterrissage lorsque la fenêtre est fermée
tello.land()
pygame.quit()
