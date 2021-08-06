
import numpy as np

def func_reformat_data(training_data, store_counter, store_choice, perspective, store_n_times, storage_type = None):

    # each instance of test data is 42 element vector of 0, 1 or 2...
    # and next to that is a 7 element vector which is all 0 except a 1 where the choice was made
    sains = [ np.random.randn(y, x)
          for y, x in zip([42, 7], [1, 1]) ]


##    for i in range( len(store_choice) ):
    training_data_len = len(training_data)
    go_through_n_times = min( [store_n_times, len(store_counter)] ) # store_counter might not be as long as store_n_times
    go_through_range = range(training_data_len, go_through_n_times + training_data_len, 1)

    count = -1
    for i in go_through_range:
        count = count + 1
        
        training_data.append( [np.zeros(qwe.shape) for qwe in sains] )

        # fill the 42 element vector at the current i instance in training_data
        for counter_i in range(42):
            training_data[i][0][counter_i] = store_counter[len(store_counter) - go_through_n_times + count][counter_i]

            # 0, 0.5, 1 for self, empty, other color
            if perspective == 1:
                if training_data[i][0][counter_i] == 1:
                    training_data[i][0][counter_i] = 0
                elif training_data[i][0][counter_i] == 2:
                    training_data[i][0][counter_i] = 1
                elif training_data[i][0][counter_i] == 0:
                    training_data[i][0][counter_i] = 0.5
                    
            elif perspective == 2:
                if training_data[i][0][counter_i] == 1:
                    training_data[i][0][counter_i] = 1
                elif training_data[i][0][counter_i] == 2:
                    training_data[i][0][counter_i] = 0
                elif training_data[i][0][counter_i] == 0:
                    training_data[i][0][counter_i] = 0.5
                    

        # put a 1 in the correct place in the 7 element vector at the current i instance in training_data
        if storage_type == None:
            training_data[i][1][ store_choice[len(store_counter) - go_through_n_times + count] ] = 1
        elif storage_type == "bad move":
            # put 0.5 everywhere except a 0 where the bad move was
            for temp_i in range(7):
                training_data[i][1][temp_i] = 0.5
                
            training_data[i][1][ store_choice[len(store_counter) - go_through_n_times + count] ] = 0


    return training_data




