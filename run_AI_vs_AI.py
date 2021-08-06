
# import files
import make_big_training_data
import file_init_bia_wei__feedforward
import network

# randomly initialise biases and weights twice
sizes = [42, 50, 20, 7]
##sizes = [42, 20, 7]
(biases_1, weights_1) = file_init_bia_wei__feedforward.func_randomly_init_bia_wei(sizes)
(biases_2, weights_2) = file_init_bia_wei__feedforward.func_randomly_init_bia_wei(sizes)


# do: ( 'AI_1 play AI_2', 'train AI_1 and AI_2' ) multiple times
for i in range(10):
    # play the first AI against the other AI as many times as is needed to have a winning result
        # do this multiple times to make a big array called big_training_data
    number_of_games = 100
    big_training_data = make_big_training_data.func_make_big_training_data(number_of_games, biases_1, weights_1, biases_2, weights_2)
    
    print("\n   Finished making training data")


    # train both AIs using their current biases and weights
    # first we initialise both of the neural networks
    if i == 0: # we only need to do this once: initialise the biases and weights of the two nets
        net_1 = network.Network(sizes, biases_1, weights_1)
        net_2 = network.Network(sizes, biases_2, weights_2)

    # train these nets using the training_data (from a single game) (made above)
    # return what the new, tuned biases and weights are for each of the nets
    pass_to_SGD = (big_training_data, "big", 30, 10, 3.0)
    (biases_1, weights_1) = net_1.SGD(pass_to_SGD)
    # the arguments that are passed are:
        # the data to train on
        # whether the training data is big or small - which determines if it needs
            # to be split into mini batches
        # number of epochs to train through
        # mini_batch_size - which isn't actually used if training_data_size == "small"
        # eta

    # similarly we need to train net_2
    (biases_2, weights_2) = net_2.SGD(pass_to_SGD)

    ##print("\n biases_1 ...\n", biases_1)
    ##print("\n weights_1 ...\n", weights_1)
    ##print("\n biases_2 ...\n", biases_2)
    ##print("\n weights_2 ...\n", weights_2)
    print("\n   Finished training both nets. Biases and weights of both nets have been tuned.")

    print("Cycle {} of ( 'make training data', 'train nets' ) complete".format(i))
    print()


# use biases_1 and weights_1 in a pygame against a human
import file_connect4_human_vs_trained_AI
file_connect4_human_vs_trained_AI.func_connect4_human_vs_trained_AI(biases_1, weights_1)

















