
# randomly initialise biases and weights twice
import file_init_bia_wei__feedforward
sizes = [42, 20, 7]
(biases_1, weights_1) = file_init_bia_wei__feedforward.func_randomly_init_bia_wei(sizes)
(biases_2, weights_2) = file_init_bia_wei__feedforward.func_randomly_init_bia_wei(sizes)


# play the first AI against the other AI as many times as is needed to have a winning result
# return the training_data of this game
import make_training_data_from_AI_vs_AI
training_data = make_training_data_from_AI_vs_AI.func_make_training_data(biases_1, weights_1, biases_2, weights_2)

print("\n training_data ...\n", training_data)
