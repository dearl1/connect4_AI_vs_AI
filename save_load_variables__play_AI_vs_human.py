
import pickle

##with open('bia_wei.pickle', 'wb') as my_file:
##	pickle.dump([biases_1, weights_1], my_file)

with open('bia_wei.pickle', 'rb') as my_file:
    [biases_1, weights_1] = pickle.load(my_file)

# use biases_1 and weights_1 in a pygame against a human
import file_connect4_human_vs_trained_AI
file_connect4_human_vs_trained_AI.func_connect4_human_vs_trained_AI(biases_1, weights_1)

















