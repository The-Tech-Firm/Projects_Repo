
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
               
        
def check(a : str ,b : str ,c : str ,d : str ,e : str ,f : str ,g : str ,h : str ,i : str ):
    
    # Part 1:
    if a == b == c:
        return a
    if d == e == f:
        return d
    if g == h == i:
        return g
    
    # Part 2:
    if a == d == g:
        return a
    if b == e == h:
        return b
    if c == f == i:
        return c
    
    # Part 3:
    if a == e == i:
        return a
    if c == e == g:
        return c
    pass        


def overwrite(user : tuple):
    if data_dic[user[1]] != " ":
        print("Sorry the Column is already filled, Please Choose any other Column...")
        return True
    else:
        return False
    
 













   
def game():
    board()
    winner = ""
    counter = 1
    f = ""
    while counter <= 9:
        if counter%2 != 0:
            user1 = eval(input("Player 1, Enter the Cloumn: "))
            if user1[0] == 'exit':
                print("Thanks For Playing")
                f = 'a'
                break
            info = overwrite(user1)
            if info == True:
                user1 = eval(input("Player 1, Enter the Cloumn: "))
                info2 = overwrite(user1)
                if info2 == True:
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                else:
                    pass
            else:
                pass
            
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
                f = 'b'
                break
            info = overwrite(user2)
            if info == True:
                user2 = eval(input("Player 2, Enter the Cloumn: "))
                info2 = overwrite(user2)
                if info2 == True:
                    user2 = eval(input("Player 2, Enter the Cloumn: "))
                else:
                    pass
            else:
                pass
            
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


        counter += 1
    
    winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                   ,data_dic['g'],data_dic['h'],data_dic['i'])
    if f == 'a' or f == 'b':
        pass
    else:
        print(f"Congratulations! Winner of the Game is {winner}")

if __name__ == '__main__':
    game()
    
    
""" 
My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
Also need to add functionality such that A column cannot be Overwrite, and Adding color Functionality is still left.
"""
    
    


