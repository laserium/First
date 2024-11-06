import pygame
import random
import sys

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 480
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Tetris")

# Set the font
font = pygame.font.Font(None, 36)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the block size and number of rows and columns
block_size = 40
rows = screen_height // block_size
columns = screen_width // block_size

# Define the shapes of the tetrominoes
tetrominoes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 1, 0]]  # T
]

# Define the colors of the tetrominoes
tetromino_colors = [CYAN, YELLOW, RED, GREEN, BLUE, ORANGE, MAGENTA]

# Initialize the game variables
grid = [[0] * columns for _ in range(rows)]
falling_piece = random.choice(tetrominoes)
falling_piece_color = random.choice(tetromino_colors)
falling_piece_x = columns // 2 - len(falling_piece[0]) // 2
falling_piece_y = 0
score = 0

# Set the game clock
clock = pygame.time.Clock()

# Function to draw the game grid
def draw_grid():
    for row in range(rows):
        for column in range(columns):
            color = grid[row][column]
            if color != 0:
                pygame.draw.rect(screen, color, (column * block_size, row * block_size, block_size, block_size))

# Function to draw a single block
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * block_size, y * block_size, block_size, block_size))

# Function to check if a piece can move to a given position
def is_valid_position(piece, x, y):
    for row in range(len(piece)):
        for column in range(len(piece[0])):
            if piece[row][column]:
                if (
                    x + column < 0
                    or x + column >= columns
                    or y + row >= rows
                    or grid[y + row][x + column] != 0
                ):
                    return False
    return True

# Function to rotate a piece
def rotate_piece(piece):
    return [list(reversed(row)) for row in zip(*piece)]

# Function to clear completed rows
def clear_rows():
    rows_cleared = 0
    for row in range(rows):
        if all(grid[row]):
            grid.pop(row)
            grid.insert(0, [0] * columns)
            rows_cleared += 1
    return rows_cleared

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if is_valid_position(falling_piece, falling_piece_x - 1, falling_piece_y):
                    falling_piece_x -= 1
            elif event.key == pygame.K_RIGHT:
                if is_valid_position(falling_piece, falling_piece_x + 1, falling_piece_y):
                    falling_piece_x += 1
            elif event.key == pygame.K_DOWN:
                if is_valid_position(falling_piece, falling_piece_x, falling_piece_y + 1):
                    falling_piece_y += 1
            elif event.key == pygame.K_UP:
                rotated_piece = rotate_piece(falling_piece)
                if is_valid_position(rotated_piece, falling_piece_x, falling_piece_y):
                    falling_piece = rotated_piece

    # Update game logic
    if is_valid_position(falling_piece, falling_piece_x, falling_piece_y + 1):
        falling_piece_y += 1
    else:
        for row in range(len(falling_piece)):
            for column in range(len(falling_piece[0])):
                if falling_piece[row][column]:
                    grid[falling_piece_y + row][falling_piece_x + column] = falling_piece_color
        rows_cleared = clear_rows()
        score += rows_cleared * 100

        falling_piece = random.choice(tetrominoes)
        falling_piece_color = random.choice(tetromino_colors)
        falling_piece_x = columns // 2 - len(falling_piece[0]) // 2
        falling_piece_y = 0

        if not is_valid_position(falling_piece, falling_piece_x, falling_piece_y):
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the game grid
    draw_grid()

    # Draw the falling piece
    for row in range(len(falling_piece)):
        for column in range(len(falling_piece[0])):
            if falling_piece[row][column]:
                draw_block(falling_piece_x + column, falling_piece_y + row, falling_piece_color)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (20, 20))

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(5)

# Quit the game
pygame.quit()
