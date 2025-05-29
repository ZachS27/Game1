import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
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
goal = pygame.Rect(600, 600, 30, 30)  # Position and size of the green square

# Walls for the original-sized maze
walls = [
    # Outer boundary (with an entrance at the top-left)
    pygame.Rect(100, 50, 400, 20),    # Top boundary with a gap for entrance
    pygame.Rect(50, 50, 20, 600),     # Left boundary
    pygame.Rect(550, 50, 20, 600),    # Right boundary
    pygame.Rect(50, 650, 500, 20),    # Bottom boundary

    # Maze structure
    pygame.Rect(100, 100, 300, 20),   # Horizontal wall near the top
    pygame.Rect(100, 100, 20, 100),   # Vertical wall near the top-left
    pygame.Rect(200, 100, 20, 150),   # Vertical wall near the center-left
    pygame.Rect(300, 150, 100, 20),   # Horizontal wall near the center
    pygame.Rect(100, 200, 100, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(300, 200, 20, 100),   # Vertical wall near the center-right
    pygame.Rect(200, 300, 100, 20),   # Horizontal wall near the bottom-center
    pygame.Rect(100, 300, 20, 100),   # Vertical wall near the bottom-left
    pygame.Rect(300, 350, 100, 20),   # Horizontal wall near the bottom-right
    pygame.Rect(400, 250, 20, 100),   # Vertical wall near the bottom-right
    pygame.Rect(150, 400, 150, 20),   # Horizontal wall near the bottom-center
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
    pygame.draw.rect(screen, (0, 255, 0), goal)  # Green color (RGB: 0, 255, 0)

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
