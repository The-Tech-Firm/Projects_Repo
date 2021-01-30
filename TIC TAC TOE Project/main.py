
data_dic = {'a': " ", 'b': " ", 'c': " ", 'd': " ", 'e': " ", 'f': " ", 'g': " ", 'h': " ", 'i': " "}


def board(container : str = "", screenwidth : int = 59):
    counter = 0
    while counter <= 21:
        if counter == 0 or counter == 14 or counter == 7 or counter == 21:
            container = "-" * screenwidth
            print(container)
            counter += 1
            continue
        
        if counter == 3:
            container = f"|          {data_dic['a']}       |          {data_dic['b']}        |          {data_dic['c']}       |"
            print(container)
            counter += 1 
            continue
        
        if counter == 10 :
            container = f"|          {data_dic['d']}       |          {data_dic['e']}        |          {data_dic['f']}       |"
            print(container)
            counter += 1
            continue
            
        if counter == 17:
            container = f"|          {data_dic['g']}       |          {data_dic['h']}        |          {data_dic['i']}       |"
            print(container)
            counter += 1
            continue
            
        else:
            container = "|                  |                   |                  |"
            print(container)
            counter += 1
               
        
        



    
def game():
    board()
    winner = ""
    counter = 1
    dict1 = []
    while counter <= 9:
        if counter%2 != 0:
            user1 = eval(input("Player 1, Enter the Cloumn: "))
            if user1[0] == 'exit':
                print("Thanks For Playing")
                break
            if user1[1] == 'a':
                data_dic['a'] = user1[0]
                board()
            if user1[1] == 'b':
                data_dic['b'] = user1[0]
                board()
            if user1[1] == 'c':
               data_dic['c'] = user1[0]
               board()
            if user1[1] == 'd':
                data_dic['d'] = user1[0]
                board()
            if user1[1] == 'e':
                data_dic['e'] = user1[0]
                board()
            if user1[1] == 'f':
                data_dic['f'] = user1[0]
                board()
            if user1[1] == 'g':
                data_dic['g'] = user1[0]
                board()
            if user1[1] == 'h':
                data_dic['h'] = user1[0]
                board()
            if user1[1] == 'i':
                data_dic['i'] = user1[0]
                board()
            
                
        else:
            user2 = eval(input("Player 2, Enter the Column: "))
            if user2[0] == 'exit':
                print("Thanks For Playing")
                break
            if user2[1] == 'a':
                data_dic['a'] = user2[0]
                board()
            if user2[1] == 'b':
                data_dic['b'] = user2[0]
                board()
            if user2[1] == 'c':
                data_dic['c'] = user2[0]
                board()
            if user2[1] == 'd':
                data_dic['d'] = user2[0]
                board()
            if user2[1] == 'e':
                data_dic['e'] = user2[0]
                board()
            if user2[1] == 'f':
                data_dic['f'] = user2[0]
                board()
            if user2[1] == 'g':
                data_dic['g'] = user2[0]
                board()
            if user2[1] == 'h':
                data_dic['h'] = user2[0]
                board()
            if user2[1] == 'i':
               data_dic['i'] = user2[0]
               board()

        # checkResult = board()
        # if checkResult[1] == "winner":
        #     print(f"Congratulations {checkResult[0]} is the Winner") 
        # else:
        #     continue
        counter += 1
    pass


if __name__ == '__main__':
    game()
    
    
""" 
My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
Also need to add functionality such that A column cannot be Overwrite.
"""
    
# x = eval(input("Enter: "))
# print(x[0],x[1])