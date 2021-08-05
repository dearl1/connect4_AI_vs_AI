
##if 1==1==1:
##    print("same")

##if 1==1==1 and 2==2:
##    print("print_me")

def func_check_connect_4(counter):

    # check for connect 4 in a row
    for i in range(6):
        for j in range(7-3):
            if counter[i][j] == counter[i][j+1] == counter[i][j+2] == counter[i][j+3] and counter[i][j] != 0:
                return "got connect 4"

    # check for connect 4 in a column
    for i in range(6-3):
        for j in range(7):
            if counter[i][j] == counter[i+1][j] == counter[i+2][j] == counter[i+3][j]  and counter[i][j] != 0:
                return "got connect 4"

    # check for connect 4 in a forward slash (\) diagonal
    for i in range(6-3):
        for j in range(7-3):
            if counter[i][j] == counter[i+1][j+1] == counter[i+2][j+2] == counter[i+3][j+3]  and counter[i][j] != 0:
                return "got connect 4"

    # check for connect 4 in a back slash (/) diagonal
    for i in [3, 4, 5]:
        for j in range(7-3):
            if counter[i][j] == counter[i-1][j+1] == counter[i-2][j+2] == counter[i-3][j+3]  and counter[i][j] != 0:
                return "got connect 4"

    return "no connect 4"


def func_main(counter, whose_turn):
    if func_check_connect_4(counter) == "got connect 4":
        return whose_turn
    else:
        return 0


