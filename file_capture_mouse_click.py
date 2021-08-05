    
##for event in pygame.event.get():
# don't include this line but run the below function inside this line of code in the main code

def func_capture_mouse_click(event, left, top, width, height):
    import pygame
    
    #checks if a mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
          
        #if the mouse is clicked on the
        # button the game is terminated
        mouse = [0, 0]
        (mouse[0], mouse[1]) = event.pos
        
        if left <= mouse[0] <= left + width and top <= mouse[1] <= top + height:
            return True
##            pygame.quit()
                
    # updates the frames of the game
    pygame.display.update()

    return False
