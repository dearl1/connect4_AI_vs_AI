
def func_full_add_connect_draw_turn(counter, what_button, whose_turn, winner, game_status):

    # Check if the column which the user has chosen is already full
    import file_is_column_full
    is_column_full = file_is_column_full.func_is_column_full(counter, what_button)

    print("\n is_column_full: ", is_column_full)

    # Only add a counter to the column if the column is not already full
    if is_column_full == "no":
        # if the column has space for another counter then:

        # add a counter into the connect 4 board
        import file_add_counter
        counter = file_add_counter.func_add_counter(counter, what_button, whose_turn)

        print("\n counter ...\n", counter)


        # check if there are 4 connected counters
        import file_check_connect_4
        winner = file_check_connect_4.func_main(counter, whose_turn)

        if winner == 1 or winner == 2:
            print("\n\n   The winner is player {}".format(winner))
            game_status = "stopped"

            return (counter, whose_turn, winner, game_status, is_column_full) # if there is a winner then immediately exit
                # this func_full_add_connect_draw_turn function so that
                # the section of code below doesn't run and make game_status change from being "stopped" to being something else


        # check if the columns are all full up
        import file_check_draw
        game_status = file_check_draw.func_check_draw(counter)
        
        if game_status == "draw":
            print("\n   It's a draw")
            

        # next player's turn
        if whose_turn == 1:
            whose_turn = 2
        else:
            whose_turn = 1


    return (counter, whose_turn, winner, game_status, is_column_full)


                
