
import numpy as np

def func_counter_to_a(counter):
    
    a = np.zeros((42, 1))
    a = a + [np.reshape(counter, (42, 1))]
    a = np.reshape(a, (42, 1)) # for some reason 'a' changes shape to: (1, 42, 1) (if I remember correctly) when the above addition line of code is run
    # so I need to change the shape of 'a' back to: (42, 1)

    # make all the elements in 'a' be: 0, 0.5, 1 for: self (player 2), empty, other color (player 1)
    a[a==2.0] = 0.1 # actually we'll make it 0 later
    a[a==0.0] = 0.5

    a[a==0.1] = 0.0 # here we actually make it 0   

    return a



