import pygame
import random
import os

# Initialize Pygame
pygame.mixer.init()
pygame.init()

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (35, 45, 40)

# Game window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Create default background
def create_default_background(size=(900, 600), color=(50, 150, 50)):
    surface = pygame.Surface(size)
    surface.fill(color)
    return surface

# Game backgrounds
try:
    bg = create_default_background()  # Default background
    intro = create_default_background()  # Default intro screen
    intro_text = "Snake Game"
except Exception as e:
    print(f"Error creating backgrounds: {e}")
    pygame.quit()
    quit()

# Game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("Welcome to Snake Game", white, screen_width//4, screen_height//3)
        text_screen("Press Space Bar To Play", white, screen_width//4, screen_height//2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
    quit()

def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = screen_width//2
    snake_y = screen_height//2
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    fps = 30  # Slower speed for easier gameplay
    
    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(20, screen_height-20)
    
    score = 0
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(black)
            text_screen("Game Over!", red, screen_width//3, screen_height//3)
            text_screen(f"Score: {score}", white, screen_width//3, screen_height//2)
            text_screen("Press Enter To Play Again", white, screen_width//4, 2*screen_height//3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        velocity_y = -5
                        velocity_x = 0
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y = 5
                        velocity_x = 0
                    
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 10
                food_x = random.randint(20, screen_width-20)
                food_y = random.randint(20, screen_height-20)
                snk_length += 5

            gameWindow.fill(black)
            text_screen(f"Score: {score}", white, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                
            plot_snake(gameWindow, white, snk_list, snake_size)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# Start the game
if __name__ == "__main__":
    welcome()
