import pygame
import sys
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event with Image & Sound")
clock = pygame.time.Clock()

# Load background image
try:
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except:
    print("⚠️ 'background.jpg' not found!")
    background = None

# Load and play background music
try:
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)  # Loop forever
except:
    print("⚠️ 'background.mp3' not found or failed to load.")

# Custom event
SPAWN_RECT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_RECT_EVENT, 2000)

# Colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0)]
rectangles = []

# Main loop
running = True
while running:
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_RECT_EVENT:
            rect_x = random.randint(0, WIDTH - 50)
            rect_y = random.randint(0, HEIGHT - 50)
            color = random.choice(colors)
            rect = pygame.Rect(rect_x, rect_y, 50, 50)
            rectangles.append((rect, color))

    # Draw rectangles
    for rect, color in rectangles:
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
