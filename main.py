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

# Goal
goal = pygame.Rect(600, 600, 30, 30)

# Walls for a larger and more complex maze
walls = [
    # Outer boundary (with an entrance at the top-left)
    pygame.Rect(150, 50, 500, 20),    # Top boundary with a larger gap for entrance
    pygame.Rect(50, 50, 20, 600),     # Left boundary
    pygame.Rect(650, 50, 20, 600),    # Right boundary
    pygame.Rect(50, 650, 600, 20),    # Bottom boundary

    # Maze structure
    pygame.Rect(150, 100, 400, 20),   # Horizontal wall near the top
    pygame.Rect(150, 100, 20, 150),   # Vertical wall near the top-left
    pygame.Rect(300, 100, 20, 200),   # Vertical wall near the center-left
    pygame.Rect(400, 150, 200, 20),   # Horizontal wall near the center
    pygame.Rect(150, 250, 150, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(400, 250, 20, 200),   # Vertical wall near the center-right
    pygame.Rect(300, 400, 200, 20),   # Horizontal wall near the bottom-center
    pygame.Rect(150, 400, 20, 200),   # Vertical wall near the bottom-left
    pygame.Rect(400, 500, 200, 20),   # Horizontal wall near the bottom-right
    pygame.Rect(550, 350, 20, 200),   # Vertical wall near the bottom-right
    pygame.Rect(200, 600, 300, 20),   # Horizontal wall near the bottom-center

    # Additional complexity
    pygame.Rect(200, 200, 20, 150),   # Vertical wall near the middle-left
    pygame.Rect(350, 250, 20, 150),   # Vertical wall near the middle-center
    pygame.Rect(500, 100, 20, 150),   # Vertical wall near the top-right
    pygame.Rect(300, 300, 200, 20),   # Horizontal wall near the middle
    pygame.Rect(150, 500, 150, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(350, 500, 20, 100),   # Vertical wall near the bottom-center

    # New walls for increased difficulty
    pygame.Rect(250, 150, 20, 100),   # Vertical wall near the top-center
    pygame.Rect(450, 200, 100, 20),   # Horizontal wall near the center-right
    pygame.Rect(100, 300, 100, 20),   # Horizontal wall near the middle-left
    pygame.Rect(250, 350, 20, 100),   # Vertical wall near the middle-left
    pygame.Rect(500, 400, 100, 20),   # Horizontal wall near the bottom-right
    pygame.Rect(200, 450, 100, 20),   # Horizontal wall near the bottom-left
    pygame.Rect(550, 150, 20, 100),   # Vertical wall near the top-right
    pygame.Rect(450, 550, 100, 20),   # Horizontal wall near the bottom-right
    pygame.Rect(300, 550, 20, 100),   # Vertical wall near the bottom-center
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

    # Win condition
    if player.colliderect(goal):
        print("You win!")
        running = False

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, GREEN, goal)
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    pygame.display.flip()

pygame.quit()
