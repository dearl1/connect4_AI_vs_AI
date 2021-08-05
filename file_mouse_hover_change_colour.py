import pygame
import sys

def func_mouse_hover_change_colour(screen, left, top, width, height):
    import pygame
      
    # light shade of the button
    color_light = (170,170,170)
      
    # dark shade of the button
    color_dark = (100,100,100)

            
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if left <= mouse[0] <= left + width and top <= mouse[1] <= top + height:
        pygame.draw.rect(screen,color_light,[left, top, width, height])
          
    else:
        pygame.draw.rect(screen,color_dark,[left, top, width, height])
      
