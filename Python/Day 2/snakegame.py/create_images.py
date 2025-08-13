import pygame
import os

# Initialize Pygame
pygame.init()

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCREEN_DIR = os.path.join(SCRIPT_DIR, "Screen")

# Create Screen directory if it doesn't exist
if not os.path.exists(SCREEN_DIR):
    os.makedirs(SCREEN_DIR)

# Create background image (bg2.jpg)
bg_size = (800, 600)
bg = pygame.Surface(bg_size)
bg.fill((50, 150, 50))  # Green background
pygame.image.save(bg, os.path.join(SCREEN_DIR, "bg2.jpg"))

# Create intro image
intro = pygame.Surface(bg_size)
intro.fill((0, 0, 0))  # Black background
font = pygame.font.Font(None, 64)
text = font.render("Snake Game", True, (255, 255, 255))
text_rect = text.get_rect(center=(bg_size[0]/2, bg_size[1]/2))
intro.blit(text, text_rect)
pygame.image.save(intro, os.path.join(SCREEN_DIR, "intro1.png"))

# Create outro image
outro = pygame.Surface(bg_size)
outro.fill((0, 0, 0))  # Black background
text = font.render("Game Over", True, (255, 0, 0))
text_rect = text.get_rect(center=(bg_size[0]/2, bg_size[1]/2))
outro.blit(text, text_rect)
pygame.image.save(outro, os.path.join(SCREEN_DIR, "outro.png"))

print("Created game images successfully!")
