import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sims")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
BLUE = (70, 130, 180)
BROWN = (139, 69, 19)

# Player attributes
player = pygame.Rect(280, 180, 40, 40)
player_color = BLUE
speed = 4

# Needs (hunger, energy, happiness)
needs = {"hunger": 100, "energy": 100, "happiness": 100}

# Objects (bed, fridge, computer)
bed = pygame.Rect(50, 50, 60, 40)
fridge = pygame.Rect(500, 50, 40, 60)
computer = pygame.Rect(250, 300, 80, 40)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    
    # Collision with objects
    if player.colliderect(bed):
        needs["energy"] = min(100, needs["energy"] + 1)
    if player.colliderect(fridge):
        needs["hunger"] = min(100, needs["hunger"] + 1)
    if player.colliderect(computer):
        needs["happiness"] = min(100, needs["happiness"] + 1)
    
    # Decrease needs over time
    for key in needs:
        needs[key] -= 0.05
    
    # Draw objects
    pygame.draw.rect(screen, BROWN, bed)
    pygame.draw.rect(screen, GREEN, fridge)
    pygame.draw.rect(screen, BLACK, computer)
    pygame.draw.rect(screen, player_color, player)
    
    # Display needs
    font = pygame.font.Font(None, 24)
    y_offset = 10
    for key, value in needs.items():
        text = font.render(f"{key.capitalize()}: {int(value)}", True, BLACK)
        screen.blit(text, (10, y_offset))
        y_offset += 20
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()