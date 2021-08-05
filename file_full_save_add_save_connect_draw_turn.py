
import file_reformat_data

def func_full_save_add_save_connect_draw_turn(counter, what_button, whose_turn, winner, game_status, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data):

    # Check if the column which the user has chosen is already full
    import file_is_column_full
    is_column_full = file_is_column_full.func_is_column_full(counter, what_button)

##    print("\n is_column_full: ", is_column_full)

    # Only add a counter to the column if the column is not already full
    if is_column_full == "no":
        # if the column has space for another counter then:


        # save snapshot of counter
        if whose_turn == 1:
            import file_save_counter
            store_counter_1 = file_save_counter.func_save_counter(store_counter_1, counter)
            
        elif whose_turn == 2:
            import file_save_counter
            store_counter_2 = file_save_counter.func_save_counter(store_counter_2, counter)


        # add a counter into the connect 4 board
        import file_add_counter
        counter = file_add_counter.func_add_counter(counter, what_button, whose_turn)

        print("\n counter ...\n", counter)

        # save the choice
        choice = what_button
        
        if whose_turn == 1:
            store_choice_1.append( choice )
        elif whose_turn == 2:
            store_choice_2.append( choice )


        # check if there are 4 connected counters
        import file_check_connect_4
        winner = file_check_connect_4.func_main(counter, whose_turn)


        # if there is a win: save the last 3 moves of this winner to training_data
        if winner == 1:
            store_n_times = 3
            
            training_data = file_reformat_data.func_reformat_data(training_data, store_counter_1, store_choice_1, winner, store_n_times)
            print("\n   Player 1 won")
            print("\n training_data ...\n", training_data)

            if store_choice_1[-1] != store_choice_2[-1]:
                # save the move that the other player should have done in hindsight
                store_n_times = 1
                training_data = file_reformat_data.func_reformat_data(training_data, store_counter_2, store_choice_1, 2, store_n_times)
                print("\n   Added hindsight to training_data...")
                print("\n training_data ...\n", training_data)
            else:
                print("\n   Did not add hindsight to training_data")

        if winner == 2:
            store_n_times = 3
            
            training_data = file_reformat_data.func_reformat_data(training_data, store_counter_2, store_choice_2, winner, store_n_times)
            print("\n   Player 2 won")
            print("\n training_data ...\n", training_data)

            if store_choice_1[-1] != store_choice_2[-1]:
                # save the move that the other player should have done in hindsight
                store_n_times = 1
                training_data = file_reformat_data.func_reformat_data(training_data, store_counter_1, store_choice_2, 1, store_n_times)
                print("\n   Added hindsight to training_data...")
                print("\n training_data ...\n", training_data)
            else:
                print("\n   Did not add hindsight to training_data")


        if winner == 1 or winner == 2:
##            print("\n\n   The winner is player {}".format(winner))
            game_status = "stopped"

            return (counter, whose_turn, winner, game_status, is_column_full, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data)
                # if there is a winner then immediately exit
                # this func_full_add_connect_draw_turn function so that
                # the section of code below doesn't run and make game_status change from being "stopped" to being something else


        # check if the columns are all full up
        import file_check_draw
        game_status = file_check_draw.func_check_draw(counter)
        
##        if game_status == "draw":
##            print("\n   It's a draw")
            

        # next player's turn
        if whose_turn == 1:
            whose_turn = 2
        else:
            whose_turn = 1


    return (counter, whose_turn, winner, game_status, is_column_full, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data)


                
