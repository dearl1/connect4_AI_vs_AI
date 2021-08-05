
##test = list(range(5, 0, -1))
##print(test)

def func_add_counter(counter, what_button, whose_turn):
    for i in list(range(0, 6, 1)):
        if counter[i][what_button] != 0:
            counter[i-1][what_button] = whose_turn
            break

    if counter[5][what_button] == 0:
        counter[5][what_button] = whose_turn

    return counter


##
##import numpy as np
##counter = np.zeros((6, 7))
##
##for i in range(6):
##    counter[i][0] = i
##
##print("\n counter ...\n", counter)
##
##for i in list(range(1, 6, 1)):
##    print(counter[i][0])
