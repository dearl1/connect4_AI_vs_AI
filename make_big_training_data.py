
import make_training_data_from_AI_vs_AI

def func_make_big_training_data(number_of_games, biases_1, weights_1, biases_2, weights_2):

    big_training_data = []

    for game in range(number_of_games):
        training_data_1game = make_training_data_from_AI_vs_AI.func_make_training_data(biases_1, weights_1, biases_2, weights_2)
##        print(len(training_data_1game))

        for instance in training_data_1game:
            big_training_data.append(instance)

    return big_training_data

##print()
##print(len(big_training_data))

##print()
##print(big_training_data)

##print(type(training_data_1game))
##print(make_training_data.func_make_training_data())

##print(func_make_big_training_data(2))
