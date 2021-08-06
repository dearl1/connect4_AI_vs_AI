import numpy as np
import math
import sys

import file_init_bia_wei__feedforward

def func_connect4_human_vs_trained_AI(biases, weights):

    ##6 down, 7 across
    ##0 for empty, 1 for aqua, 2 for red

    counter = np.zeros((6, 7))

    print("\n counter ...\n", counter)

    radius = 30
    num_for_width = 8
    num_for_height = 9


    # Import and initialize the pygame library
    import pygame
    pygame.init()

    # Set up the drawing window
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


    # Initialise colors
    black = (0, 0, 0) # black
    blue = (0, 128, 128) # blue
    red = (255, 0, 0) # red
    light_grey = (170,170,170)
    dark_grey = (100,100,100)


    whose_turn = 1
    winner = 0

    import file_full_add_connect_draw_turn

    # Run until the user asks to quit
    running = True
    game_status = "running"
    while running:

        # Check for events
        for event in pygame.event.get():

            # Did the user click the window close button?
            if event.type == pygame.QUIT:
                running = False


            # Did the user click one of the buttons?
            import file_capture_mouse_click

            what_button = None
            for i in range(7):
                left = math.floor(SCREEN_WIDTH/num_for_width*(i+1)) - radius
                top = math.floor(SCREEN_HEIGHT/num_for_height*(2)) - radius
                width = radius*2
                height = radius*2
                
                button_clicked = file_capture_mouse_click.func_capture_mouse_click(event, left, top, width, height)

                if button_clicked == True and game_status == "running" and whose_turn == 1: # the human is player 1 so the last condition checks it's the human's turn
                    what_button = i
                    print("\n what_button: ", what_button)

                    (counter, whose_turn, winner, game_status, is_column_full) = file_full_add_connect_draw_turn.func_full_add_connect_draw_turn(counter, what_button, whose_turn, winner, game_status)

                    # the above does:
                    # Check if the column which the user has chosen is already full
                    # Only add a counter to the column if the column is not already full
                        # if the column has space for another counter then:
                        # add a counter into the connect 4 board
                        # check if there are 4 connected counters
                        # check if the columns are all full up
                        # next player's turn

                    break # Don't check if the user has clicked another button because they already have!

        # End of checking for events


        # AI's turn (player 2)
        # This deals with the case where the AI keeps trying to drop a counter into a column which is full
        if game_status == "running" and whose_turn == 2:

            import file_counter_to_a
            # reshape counter to (42, 1)
            # make all the elements in 'a' be: 0, 0.5, 1 for: self (player 2), empty, other color (player 1)
            a = file_counter_to_a.func_counter_to_a(counter)
            print("\n a ...\n", a)
            
            AI_choice_list = file_init_bia_wei__feedforward.func_feedforward(a, biases, weights)
            AI_choice = np.argmax(AI_choice_list)

            while sum(AI_choice_list) > 0:
            
                (counter, whose_turn, winner, game_status, is_column_full) = file_full_add_connect_draw_turn.func_full_add_connect_draw_turn(counter, AI_choice, whose_turn, winner, game_status)
         
                if is_column_full == "yes":

                    # make the index in AI_choice_list associated with the connect 4 column which is full be 0
                    AI_choice_list[AI_choice] = 0
                    
                    AI_choice = np.argmax(AI_choice_list)
                    
                elif is_column_full == "no":
                    break
                    

        # Fill the background with white
        screen.fill((255, 255, 255))


        # Draw connect 4 board
        for i in range(6):
            for j in range(7):
                
                if counter[i][j] == 0:
                    color = black
                    width = 3
                elif counter[i][j] == 1:
                    color = blue
                    width = 0
                elif counter[i][j] == 2:
                    color = red
                    width = 0

                pygame.draw.circle(screen, color, ( math.floor(SCREEN_WIDTH/num_for_width*(j+1)) , math.floor(SCREEN_HEIGHT/num_for_height*(i+3)) ), radius, width)


        # cause buttons to change colour when mouse moves over them
        import file_mouse_hover_change_colour
        for i in range(7):
            left = math.floor(SCREEN_WIDTH/num_for_width*(i+1)) - radius
            top = math.floor(SCREEN_HEIGHT/num_for_height*(2)) - radius
            width = radius*2
            height = radius*2
            
            file_mouse_hover_change_colour.func_mouse_hover_change_colour(screen, left, top, width, height)


        # if the game is still running: say whose turn it is
        if game_status == "running":
            import file_whose_turn
            file_whose_turn.func_whose_turn(screen, whose_turn, SCREEN_WIDTH, SCREEN_HEIGHT, num_for_height)


        # if the game has stopped: output winner to the pygame screen
        if game_status == "stopped":
            import file_output_text
            file_output_text.func_output_text(screen, winner, SCREEN_WIDTH, SCREEN_HEIGHT, num_for_height)
        

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


