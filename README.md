# connect4 with an AI

Run connect4_as_a_game.py to play as a human vs another human (or play yourself!).  

Any .py file which says file_ at the start is a function which is used by a main script.

run_AI_vs_AI.py calls make_big_training_data.py which calls make_training_data_from_AI_vs_AI.py which calls file_AI_turn.py which calls file_full_save_add_save_connect_draw_turn.py  
make_training_data_from_AI_vs_AI.py is a function which plays one AI vs another AI.  
They each learn from their mistakes and slowly the weights and biases of each of them improve.  

In run_AI_vs_AI.py the number of layers in the neural network and the size of each layer can be changed.
* As an example, if sizes = [42, 100, 20, 7] then the neural network has 4 layers. The first layer has 42 neurons, the second has 100 and so on.
In run_AI_vs_AI.py the pass_to_SGD tuple is of the form: (big_training_data, "big", 100, 10, 3.0).
* The third element in this tuple (here 100) is the number of epochs that each of the AIs will be trained through.
* The fifth element is eta, the learning rate.

file_connect4_human_vs_trained_AI.py is a function which takes as input a set of biases and weights which are what an AI uses to play against a human.  
At the end of the run_AI_vs_AI.py script file_connect4_human_vs_trained_AI.py is called so that the trained AI is used against a human.
