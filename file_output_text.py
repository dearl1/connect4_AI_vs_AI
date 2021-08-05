import pygame

def func_output_text(screen, winner, SCREEN_WIDTH, SCREEN_HEIGHT, num_for_height, draw=None):

    pygame.font.init()
    smallfont = pygame.font.SysFont('Corbel',35)

    # Initialise colors
    black = (0, 0, 0) # black
    blue = (0, 128, 128) # aqua
    red = (255, 0, 0) # red


    # rendering text
    if winner == 1:
        color = blue
    elif winner == 2:
        color = red
        
        
    text = smallfont.render("The winner is player {}".format(winner) , True , color)

    screen.blit(text, (SCREEN_WIDTH/2 - 80, SCREEN_HEIGHT/num_for_height*(0.5)))


