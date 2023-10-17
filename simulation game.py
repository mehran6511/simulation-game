
### This Project Authored By Mehran Moein ###
### Linkedin: https://www.linkedin.com/in/mehran6511 ###

# Import Libraries
import pygame
import numpy as np
from time import sleep

### Key Word Project ###

# Empty == 0
# Conductive == 1
# Electron Head == 2
# Electron Tail == 3

###################################### Start Code ######################################

# Updata Cells Function
def update(screen, cells, key_run):

    # Create New Cells
    new_cells = cells.copy()

    # Select Index
    for r, c in np.ndindex(cells.shape):

        # Run Condition
        if key_run == 1:

            # Calculate Number Neighbor
            num_conductive = 0
            if r <= cells.shape[0]-2 and c <= cells.shape[1]-2:
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if (i!=r or j!=c) and cells[i, j] == 2:

                            # Find Electron Head Neighbor
                            num_conductive += 1

                            # Set Electron Tail In New Cell
                            new_cells[i,j] = 3

                        # Clear Last Electron Tail In New Cell
                        if (i!=r or j!=c) and cells[i, j] == 3:
                            new_cells[i, j] = 1
                        
            # Set Electron Head In New Cell
            if (cells[r, c] == 1 and num_conductive == 1) or (cells[r, c] == 1 and num_conductive == 2):
                new_cells[r, c] = 2



        # Set Color
        if cells[r, c] == 1:
            color = (250, 253, 15)
        elif cells[r, c] == 2:
            color = (0, 0, 255)
        elif cells[r, c] == 3:
            color = (250, 0, 0)
        else:
            color = (0, 0, 0)

        # Create Rect
        pygame.draw.rect(screen, color, (c*10, r*10, 9, 9))

    return new_cells

# Run Pygame
pygame.init()

# Set Screen
screen = pygame.display.set_mode((640, 480))

# Create Cells
cells = np.zeros((47, 65))

# Default Variable
running = True
key_run = 0

# Text
font = pygame.font.SysFont(None, 17)
img1 = font.render('     Run: Space Key | Stop: P Key | Conductive: Left Click | Electron Head: Right Click | Electron Tail: Double Right Click     ', True, "RED", "White")
img2 = font.render('     Run: Space Key | Stop: P Key | Conductive: Left Click | Electron Head: Right Click | Electron Tail: Double Right Click     ', True, "White", "White")

# Run Game
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Click And Key Condition
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            x = mouse[1]//10
            y = mouse[0]//10
            if x < 46 and y < 64:
                if event.button == 1 and cells[x, y] == 0:
                    cells[x, y] = 1
                elif event.button == 1 and cells[x, y] == 1:
                    cells[x, y] = 0
                elif event.button == 3 and cells[x, y] == 1:
                    cells[x, y] = 2
                elif event.button == 3 and cells[x, y] == 2:
                    cells[x, y] = 3
                elif event.button == 3 and cells[x, y] == 3:
                    cells[x, y] = 1
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                key_run = 1
            if event.key == 112:
                key_run = 0

    # Screen Color        
    screen.fill((127, 127, 127))
    
    # Call New Cells
    cells = update(screen, cells, key_run)

    # Run Text And Cells
    screen. blit(img1, (0, 461))
    screen. blit(img2, (0, 473))
    pygame.display.flip()

    # Time
    sleep(0.5)

# End Game
pygame.quit()

###################################### End Code ######################################