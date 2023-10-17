import pygame
import numpy as np

#Updata cells Function
def update(screen, cells):

    #Create new cells
    new_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for r, c in np.ndindex(cells.shape):

        #Calculate number alives
        num_alive = np.sum(cells[r-1:r+2, c-1:c+2]) - cells[r, c]

        #Conditions
        if (cells[r, c] == 1 and 2 <= num_alive <= 3) or (cells[r, c] == 0 and num_alive == 3):
            new_cells[r, c] = 1
            color = (0, 0, 255)

        #Set color
        if cells[r, c] == 1:
            color = color  
        else:
            color = (255, 255, 255)

        #Create rect
        pygame.draw.rect(screen, color, (c*5, r*5, 5, 5))

    return new_cells


pygame.init()
screen = pygame.display.set_mode((640, 480))

#Create cells
cells = np.zeros((96, 128))

#Input alive cells
pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])


#Select range pattern
start_point = (1,1)
cells[start_point[0]:start_point[0]+pattern.shape[0], start_point[1]:start_point[1]+pattern.shape[1]] = pattern


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Call new cells and run game
    cells = update(screen, cells)

    pygame.display.flip()
pygame.quit()
