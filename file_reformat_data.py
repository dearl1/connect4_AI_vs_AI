
import numpy as np

def func_reformat_data(store_counter, store_choice, winner, store_n_times):

    # each instance of test data is 42 element vector of 0, 1 or 2...
    # and next to that is a 7 element vector which is all 0 except a 1 where the choice was made
    sains = [ np.random.randn(y, x)
          for y, x in zip([42, 7], [1, 1]) ]

    training_data = []

    for i in range( store_n_times ):
        training_data.append( [np.zeros(qwe.shape) for qwe in sains] )

        # fill the 42 element vector at the current i instance in training_data
        for counter_i in range(42):
            training_data[i][0][counter_i] = store_counter[-1 - i][counter_i]

            # 0, 0.5, 1 for self, empty, other color
            if winner == 1:
                if training_data[i][0][counter_i] == 1:
                    training_data[i][0][counter_i] = 0
                elif training_data[i][0][counter_i] == 2:
                    training_data[i][0][counter_i] = 1
                elif training_data[i][0][counter_i] == 0:
                    training_data[i][0][counter_i] = 0.5
                    
            elif winner == 2:
                if training_data[i][0][counter_i] == 1:
                    training_data[i][0][counter_i] = 1
                elif training_data[i][0][counter_i] == 2:
                    training_data[i][0][counter_i] = 0
                elif training_data[i][0][counter_i] == 0:
                    training_data[i][0][counter_i] = 0.5
                    

        # put a 1 in the correct place in the 7 element vector at the current i instance in training_data
        training_data[i][1][ store_choice[-1 - i] ] = 1


    return training_data




