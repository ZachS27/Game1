import pygame

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Escape")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player
player = pygame.Rect(20, 20, 30, 30)

# Define the goal (green square) at the end of the maze
goal = pygame.Rect(750, 750, 30, 30)  # Position and size of the green square

# Walls for the updated maze (filling the entire screen)
walls = [
    # Outer boundary
    pygame.Rect(0, 0, SCREEN_WIDTH, 10),    # Top boundary
    pygame.Rect(0, 0, 10, SCREEN_HEIGHT),   # Left boundary
    pygame.Rect(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT),  # Right boundary
    pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10),  # Bottom boundary

    # Maze structure
    pygame.Rect(100, 100, 20, 200),   # Vertical wall near the top-left
    pygame.Rect(300, 100, 20, 300),   # Vertical wall near the center-left
    pygame.Rect(500, 150, 200, 20),   # Horizontal wall near the center
    pygame.Rect(100, 300, 200, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(500, 300, 20, 300),   # Vertical wall near the center-right
    pygame.Rect(300, 500, 200, 20),   # Horizontal wall near the bottom-center
    pygame.Rect(100, 500, 20, 200),   # Vertical wall near the bottom-left
    pygame.Rect(500, 700, 200, 20),   # Horizontal wall near the bottom-right
    pygame.Rect(700, 400, 20, 300),   # Vertical wall near the bottom-right
    pygame.Rect(200, 750, 400, 20),   # Horizontal wall near the bottom-center

    # Additional obstacles
    pygame.Rect(200, 200, 100, 20),   # Horizontal wall near the top-left
    pygame.Rect(400, 200, 20, 100),   # Vertical wall near the center
    pygame.Rect(600, 200, 100, 20),   # Horizontal wall near the top-right
    pygame.Rect(200, 400, 20, 100),   # Vertical wall near the middle-left
    pygame.Rect(400, 400, 100, 20),   # Horizontal wall near the middle
    pygame.Rect(600, 500, 20, 100),   # Vertical wall near the middle-right

    # New obstacles
    pygame.Rect(250, 150, 20, 150),   # Vertical wall near the top-left
    pygame.Rect(450, 250, 150, 20),   # Horizontal wall near the center-right
    pygame.Rect(350, 350, 20, 150),   # Vertical wall near the middle
    pygame.Rect(150, 550, 150, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(650, 350, 20, 150),   # Vertical wall near the bottom-right
    pygame.Rect(250, 700, 100, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(550, 650, 20, 100),   # Vertical wall near the bottom-center
    pygame.Rect(450, 100, 20, 100),   # Vertical wall near the top-center
    pygame.Rect(300, 250, 100, 20),   # Horizontal wall near the top-center
    pygame.Rect(550, 550, 100, 20),   # Horizontal wall near the bottom-center
    pygame.Rect(700, 150, 20, 150),   # Vertical wall near the top-right
    pygame.Rect(200, 650, 100, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(350, 600, 20, 100),   # Vertical wall near the bottom-center
    pygame.Rect(150, 150, 100, 20),   # Horizontal wall near the top-left corner
    pygame.Rect(650, 250, 100, 20),   # Horizontal wall near the top-right
]

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 3
    if keys[pygame.K_RIGHT]:
        player.x += 3
    if keys[pygame.K_UP]:
        player.y -= 3
    if keys[pygame.K_DOWN]:
        player.y += 3

    # Collision detection with walls
    for wall in walls:
        if player.colliderect(wall):
            print("Hit wall!")
            running = False

    # Draw the green square (goal)
    pygame.draw.rect(screen, GREEN, goal)  # Green color (RGB: 0, 255, 0)

    # Check for collision between the player and the goal
    if player.colliderect(goal):
        print("You reached the goal!")  # Game-ending logic
        running = False  # End the game

    pygame.draw.rect(screen, BLUE, player)
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    # Update the display
    pygame.display.flip()

pygame.quit()
