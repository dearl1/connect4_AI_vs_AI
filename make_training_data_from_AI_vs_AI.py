import numpy as np
import math
import random

import file_AI_turn

##6 down, 7 across
##0 for empty, 1 for aqua, 2 for red

def func_make_training_data(biases_1, weights_1, biases_2, weights_2):

    winner = 0
##    play_again = True

    training_data = []

    while len(training_data) == 0:

        counter = np.zeros((6, 7))
##        print("\n counter ...\n", counter)

        whose_turn = 1

        store_counter_1 = []
        store_counter_2 = []
        store_choice_1 = []
        store_choice_2 = []

        # Run until an end condition occurs (i.e. a win or a draw)
        game_status = "running"

        while game_status == "running":
            
            if whose_turn == 1:
                (counter, whose_turn, winner, game_status, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data) = file_AI_turn.func_AI_turn(game_status, whose_turn, counter, biases_1, weights_1, winner, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data)
            elif whose_turn == 2:
                (counter, whose_turn, winner, game_status, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data) = file_AI_turn.func_AI_turn(game_status, whose_turn, counter, biases_2, weights_2, winner, store_counter_1, store_counter_2, store_choice_1, store_choice_2, training_data)


    ##print("\n training_data ...\n", training_data)

    return training_data



