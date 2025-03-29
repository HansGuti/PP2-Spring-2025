import pygame
import math

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint in Pygame')

# Additional layer, on which we will save the painted   
base_layer = pygame.Surface((width, height))
base_layer.fill((255, 255, 255)) # Let's paint it white

clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

current_color = RED # Current painting color

# Tools (modes):
# - 'line' (simple pencil, as in original)
# - 'rect' (rectangular)
# - 'circle' (cirlce)
# - 'eraser' (eraser :))

mode = 'line'

drawing = False
starting_position = (0, 0)
thickness = 5

def draw_line(surface, color, start, end, thickness):
    pygame.draw.line(surface, color, start, end, thickness)

def draw_rect(surface, color, start, end, thickness):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(start[0]- end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_circle(surface, color, start, end, thickness):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = int(math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) / 2)
    pygame.draw.circle(surface, color, (center_x, center_y), radius, thickness)

def erase(surface, pos, size):
    eraser_rect = pygame.Rect(pos[0] - size // 2, pos[1] - size // 2, size, size)
    pygame.draw.rect(surface, WHITE, eraser_rect)

running = True
while running:
    screen.fill(WHITE)
    screen.blit(base_layer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 'line'
            elif event.key == pygame.K_2:
                mode = 'rect'
            elif event.key == pygame.K_3:
                mode = 'circle'
            elif event.key == pygame.K_4:
                mode = 'eraser'

            
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color == BLUE
            elif event.key == pygame.K_k:
                current_color = BLACK

            if event.key == pygame.K_EQUALS:
                thickness += 1
            elif event.key == pygame.K_MINUS:
                thickness = max(1, thickness - 1)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                starting_position = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                ending_position = event.pos

                if mode == 'rect':
                    draw_rect(base_layer, current_color, starting_position, ending_position, thickness)
                elif mode == 'circle':
                    draw_circle(base_layer, current_color, starting_position, ending_position, thickness)


        if event.type == pygame.MOUSEMOTION and drawing:
            current_position = event.pos

            if mode == 'line':
                draw_line(base_layer, current_color, starting_position, current_position, thickness)
                starting_position = current_position
            elif mode == 'eraser':
                erase(base_layer, current_position, thickness * 2)



    if drawing and (mode == 'rect' or mode == 'circle'):
        mouse_position = pygame.mouse.get_pos()
        if mode == 'rect':
            draw_rect(screen, current_color, starting_position, mouse_position, thickness)
        elif mode == 'circle':
            draw_circle(screen, current_color, starting_position, mouse_position, thickness)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()