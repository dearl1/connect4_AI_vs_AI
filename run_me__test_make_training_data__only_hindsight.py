
# import files
import make_training_data_from_AI_vs_AI
import file_init_bia_wei__feedforward

# randomly initialise biases and weights twice
sizes = [42, 20, 7]
(biases_1, weights_1) = file_init_bia_wei__feedforward.func_randomly_init_bia_wei(sizes)
(biases_2, weights_2) = file_init_bia_wei__feedforward.func_randomly_init_bia_wei(sizes)

# make training data from one connect 4 game between two AIs
training_data = make_training_data_from_AI_vs_AI.func_make_training_data(biases_1, weights_1, biases_2, weights_2)


















