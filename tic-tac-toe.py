def r_win(arr):
    val=False

    for i in range(len(arr)):

        if (arr[i][0]==arr[i][1] and arr[i][2]==arr[i][0]):
            print(arr[i][0] + "Wins!")
            val = True
            break
        
    if(val==True):
        return(True)
    else:
        return(False)

def c_win(arr):
    val = False

    for i in range(len(arr)):

        if (arr[0][i]==arr[1][i] and arr[2][i]==arr[0][i]):
            print(arr[0][i] + "Wins!")
            val = True
            break
        
    if(val==True):
        return(True)
    else:
        return(False)
    
def d_win(arr):
    val = False
    if ((arr[1][1]==arr[0][0] and arr[1][1]==arr[2][2]) or (arr[0][2]==arr[1][1]) and arr[2][0]==arr[1][1]):
            print(arr[1][1] + "Wins!")
            val = True  
    if(val==True):
        return(True)
    else:
        return(False)
    
def win_check():
    if(r_win(arr)==False):
        if(c_win(arr)==False):
            if(d_win(arr)==False):
                return(False)

def print_game(arr):
    for i in range(0,3):
        print(" ")
        print(arr[i][0] , end=" | ")
        print(arr[i][1] , end=" | ")
        print(arr[i][2])


arr = [ [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' '] ]

print_game(arr)


for i in range(0,3):
    x_input_r = int(float(input('chose X input row')))
    x_input_c = int(float(input("chose X input col")))
    arr[x_input_r][x_input_c]='X'
    o_input_r = int(float(input("chose O input row")))
    o_input_c = int(float(input("chose O input col")))
    arr[o_input_r][o_input_c]='O'
    print_game(arr)

if(win_check()==False):
    x_input_r = int(float(input("chose X input row")))
    x_input_c = int(float(input("chose X input col")))
    arr[x_input_r][x_input_c]='X'
    print_game(arr)
    if(win_check()==False):
        o_input_r = int(float(input("chose O input row")))
        o_input_c = int(float(input("chose O input col")))
        arr[o_input_r][o_input_c]='O'
        print_game(arr)
        if(win_check()==False):
            x_input_r = int(float(input("chose X input row")))
            x_input_c = int(float(input("chose X input col")))
            arr[x_input_r][x_input_c]='X'
            print_game(arr)
            if(win_check()==False):
                print("No one wins")




