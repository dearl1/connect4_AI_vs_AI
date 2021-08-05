import pygame

def func_whose_turn(screen, whose_turn, SCREEN_WIDTH, SCREEN_HEIGHT, num_for_height):

    pygame.font.init()
    smallfont = pygame.font.SysFont('Corbel',35)

    # Initialise colors
    black = (0, 0, 0) # black
    blue = (0, 128, 128) # aqua
    red = (255, 0, 0) # red


    # rendering text
    if whose_turn == 1:
        color = blue
    elif whose_turn == 2:
        color = red
        
        
    text = smallfont.render('Player '+str(whose_turn)+"'s turn" , True , color)
    ##text = smallfont.render('quit' , True , color)
    ##text = smallfont.render('quit' , True , (0, 0, 0))
    ##text = smallfont.render('quit' , False , (0, 0, 0))


    # say whose turn it is
    ##i = 0
    ##left = math.floor(SCREEN_WIDTH/num_for_width*(i+1)) - radius
    ##top = math.floor(SCREEN_HEIGHT/num_for_height*(1)) - radius*2
    ##    screen.blit(text, (left,top))

    screen.blit(text, (SCREEN_WIDTH/2 - 80, SCREEN_HEIGHT/num_for_height*(0.5)))


