
import numpy as np

import file_init_bia_wei__feedforward

def func_AI_turn(game_status, whose_turn, counter, biases, weights, winner, store_counter_1, store_counter_2, store_choice_1, store_choice_2):

    # AI's turn
    # This deals with the case where the AI keeps trying to drop a counter into a column which is full
    if game_status == "running":

        import file_counter_to_a
        # reshape counter to (42, 1), make all the elements that are 2 be 0.5 instead
        a = file_counter_to_a.func_counter_to_a(counter)
##        print("\n a ...\n", a)
        
        AI_choice_list = file_init_bia_wei__feedforward.func_feedforward(a, biases, weights)
        AI_choice = np.argmax(AI_choice_list)

        while sum(AI_choice_list) > 0:

            import file_full_save_add_save_connect_draw_turn
            (counter, whose_turn, winner, game_status, is_column_full) = file_full_save_add_save_connect_draw_turn.func_full_save_add_save_connect_draw_turn(counter, AI_choice, whose_turn, winner, game_status, store_counter_1, store_counter_2, store_choice_1, store_choice_2)
                                                                                                                                                            
     
            if is_column_full == "yes":

                # make the index in AI_choice_list associated with the connect 4 column which is full be 0
                AI_choice_list[AI_choice] = 0
                
                AI_choice = np.argmax(AI_choice_list)
                
            elif is_column_full == "no":
                break

    return (counter, whose_turn, winner, game_status)
