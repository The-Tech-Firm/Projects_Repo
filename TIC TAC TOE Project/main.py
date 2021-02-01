
data_dic = {'a': " ", 'b': " ", 'c': " ", 'd': " ", 'e': " ", 'f': " ", 'g': " ", 'h': " ", 'i': " "}
Choice_dict = {'Player 1' : " ", 'Player 2' : " "}
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
RESET = '\u001b[0m'
RED = '\u001b[31m'
CYAN = '\u001b[36m'
MAGENTA = '\u001b[35m'
BOLD = '\u001b[1m'

def board(container : str = "", screenwidth : int = 59, sign1 = " ", sign2 = " ", sign3 = " "):
    counter = 0
    while counter <= 21:
        if counter == 0 or counter == 14 or counter == 7 or counter == 21:
            container = "-" * screenwidth
            print(container)
            counter += 1
            continue
        
        if counter == 3:
            container = f"|          {data_dic['a']}       |          {data_dic['b']}        |          {data_dic['c']}       |" f"{sign1}"
            print(container)
            counter += 1 
            continue
        
        if counter == 10 :
            container = f"|          {data_dic['d']}       |          {data_dic['e']}        |          {data_dic['f']}       |" f"{sign2}"
            print(container)
            counter += 1
            continue
            
        if counter == 17:
            container = f"|          {data_dic['g']}       |          {data_dic['h']}        |          {data_dic['i']}       |" f"{sign3}"
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
    else:
        return " "
    
      


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
    continuous_check = " "
    f = ""
    while counter <= 9:
        if counter%2 != 0:
            user1 = eval(input("Player 1, Enter the Cloumn: "))
            if user1[0] == 'exit':
                print("Thanks For Playing")
                f = 'a'
                break
            if Choice_dict['Player 1'] == " ":
                pass
            else:
                if Choice_dict['Player 1'] == user1[0]:
                    pass
                else:
                    print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                    if user1[0] == 'exit':
                        print("Thanks For Playing")
                        f = 'a'
                        break
                    while user1[0] != Choice_dict['Player 1']:
                        print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
                        user1 = eval(input("Player 1, Enter the Cloumn: "))
                        if user1[0] == 'exit':
                            print("Thanks For Playing")
                            f = 'a'
                            break
                    if user1[0] == 'exit':
                        f = 'a'
                        break
                    else:
                        pass
            info = overwrite(user1)
            if info == True:
                user1 = eval(input("Player 1, Enter the Cloumn: "))
                if user1[0] == 'exit':
                    print("Thanks For Playing")
                    f = 'a'
                    break
                while user1[0] != Choice_dict['Player 1']:
                    print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                    if user1[0] == 'exit':
                        print("Thanks For Playing")
                        f = 'a'
                        break
                if user1[0] == 'exit':
                    f = 'a'
                    break
                info2 = overwrite(user1)
                while info2 != False:
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                    if user1[0] == 'exit':
                        print("Thanks For Playing")
                        f = 'a'
                        break
                    info2 = overwrite(user1)
                    if Choice_dict['Player 1'] == user1[0]:
                        pass
                    else:
                        print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
                        user1 = eval(input("Player 1, Enter the Cloumn: "))
                        if user1[0] == 'exit':
                            print("Thanks For Playing")
                            f = 'a'
                            break
                        while user1[0] != Choice_dict['Player 1']:
                            print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
                            user1 = eval(input("Player 1, Enter the Cloumn: "))
                            if user1[0] == 'exit':
                                print("Thanks For Playing")
                                f = 'a'
                                break
                        info2 = overwrite(user1)
                        
                if user1[0] == 'exit':
                    f = 'a'
                    break   
                else:
                    pass
            else:
                pass
            
            if user1[1] == 'a':
                data_dic['a'] = f"{RED}{user1[0]}{RESET}"
                board(sign1=f"{GREEN} <--- {RESET}")
            if user1[1] == 'b':
                data_dic['b'] = f"{RED}{user1[0]}{RESET}"
                board(sign1=f"{GREEN} <--- {RESET}")
            if user1[1] == 'c':
                data_dic['c'] = f"{RED}{user1[0]}{RESET}"
                board(sign1=f"{GREEN} <--- {RESET}")
            if user1[1] == 'd':
                data_dic['d'] = f"{RED}{user1[0]}{RESET}"
                board(sign2=f"{GREEN} <--- {RESET}")
            if user1[1] == 'e':
                data_dic['e'] = f"{RED}{user1[0]}{RESET}"
                board(sign2=f"{GREEN} <--- {RESET}")
            if user1[1] == 'f':
                data_dic['f'] = f"{RED}{user1[0]}{RESET}"
                board(sign2=f"{GREEN} <--- {RESET}")
            if user1[1] == 'g':
                data_dic['g'] = f"{RED}{user1[0]}{RESET}"
                board(sign3=f"{GREEN} <--- {RESET}")
            if user1[1] == 'h':
                data_dic['h'] = f"{RED}{user1[0]}{RESET}"
                board(sign3=f"{GREEN} <--- {RESET}")
            if user1[1] == 'i':
                data_dic['i'] = f"{RED}{user1[0]}{RESET}"
                board(sign3=f"{GREEN} <--- {RESET}")
            Choice_dict['Player 1'] = user1[0]
            winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                   ,data_dic['g'],data_dic['h'],data_dic['i'])
            if winner != " ":
                continuous_check = (True,winner)
                break
        else:
            user2 = eval(input("Player 2, Enter the Cloumn: "))
            if user2[0] == 'exit':
                print("Thanks For Playing")
                f = 'b'
                break
            if Choice_dict['Player 2'] == " ":
                pass
            else:
                if Choice_dict['Player 2'] == user2[0]:
                    pass
                else:
                    print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
                    user2 = eval(input("Player 2, Enter the Cloumn: "))
                    if user2[0] == 'exit':
                        print("Thanks For Playing")
                        f = 'b'
                        break
                    while user2[0] != Choice_dict['Player 2']:
                        print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
                        user2 = eval(input("Player 2, Enter the Cloumn: "))
                        if user2[0] == 'exit':
                            print("Thanks For Playing")
                            f = 'b'
                            break
                    if user2[0] == 'exit':
                        f = 'b'
                        break
                    else:
                        pass
            info = overwrite(user2)
            if info == True:
                user2 = eval(input("Player 2, Enter the Cloumn: "))
                if user2[0] == 'exit':
                    print("Thanks For Playing")
                    f = 'b'
                    break
                while user2[0] != Choice_dict['Player 2']:
                    print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
                    user2 = eval(input("Player 2, Enter the Cloumn: "))
                    if user2[0] == 'exit':
                        print("Thanks For Playing")
                        f = 'b'
                        break
                if user2[0] == 'exit':
                    f = 'b'
                    break
                info2 = overwrite(user2)
                while info2 != False:
                    user2 = eval(input("Player 2, Enter the Cloumn: "))
                    if user2[0] == 'exit':
                        print("Thanks For Playing")
                        f = 'b'
                        break
                    info2 = overwrite(user2)
                    if Choice_dict['Player 2'] == user2[0]:
                        pass
                    else:
                        print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
                        user2 = eval(input("Player 2, Enter the Cloumn: "))
                        if user2[0] == 'exit':
                            print("Thanks For Playing")
                            f = 'b'
                            break
                        while user2[0] != Choice_dict['Player 2']:
                            print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
                            user2 = eval(input("Player 2, Enter the Cloumn: "))
                            if user2[0] == 'exit':
                                print("Thanks For Playing")
                                f = 'b'
                                break
                        info2 = overwrite(user2)
                        
                if user2[0] == 'exit':
                    f = 'b'
                    break   
                else:
                    pass
            else:
                pass
            
            if user2[1] == 'a':
                data_dic['a'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign1=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'b':
                data_dic['b'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign1=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'c':
                data_dic['c'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign1=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'd':
                data_dic['d'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign2=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'e':
                data_dic['e'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign2=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'f':
                data_dic['f'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign2=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'g':
                data_dic['g'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign3=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'h':
                data_dic['h'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign3=f"{YELLOW} <--- {RESET}")
            if user2[1] == 'i':
                data_dic['i'] = f"{CYAN}{user2[0]}{RESET}"
                board(sign3=f"{YELLOW} <--- {RESET}")
                
            Choice_dict['Player 2'] = user2[0]
            winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                   ,data_dic['g'],data_dic['h'],data_dic['i'])
            if winner != " ":
                continuous_check = (True,winner)
                break


        counter += 1
    
    
    if f == 'a' or f == 'b':
        pass
    else:
        if continuous_check[0] == True:
            print(f"{MAGENTA}Congratulations! Winner of the Game is {continuous_check[1]}")
        else:
            winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                ,data_dic['g'],data_dic['h'],data_dic['i'])
            print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD}{winner}")
        
if __name__ == '__main__':
    game()
    
    
""" 
My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
Also the Colors of each Variable and the Arrows pointing to the current input column is given, the Warning situation such as If entered a column 
already filled then it will give warning and choice to re-enter and if Choosed a variable which is not the same as choosed in the beginning
it will give a Warning and choice to re-enter, and all the Warnings and choice to re-enter are given untill the Choice is True with the given Conditions,
as mentioned before.
"""
  

    


