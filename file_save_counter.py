import numpy as np

##asda = [1, 2, 3]
##print(asda[-1]) # index -1 outputs the last element


def func_save_counter(list_name, counter):
    
    list_name.append( np.zeros((42, 1)) )

    count = 0
    for i in range(6):
        for j in range(7):
            list_name[-1][count] = counter[i][j]
            count = count + 1

    return list_name


