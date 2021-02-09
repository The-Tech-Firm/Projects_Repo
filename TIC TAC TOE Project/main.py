# -------------------------------------- Global Variables -------------------------------------#
import random
data_dic = {'a': " ", 'b': " ", 'c': " ", 'd': " ", 'e': " ", 'f': " ", 'g': " ", 'h': " ", 'i': " "}
Choice_dict = {'Player 1' : " ", 'Player 2' : " ", 'Computer': " "}
var = random.choice(['X','O','$','#','%','&','@'])
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
RESET = '\u001b[0m'
RED = '\u001b[31m'
CYAN = '\u001b[36m'
MAGENTA = '\u001b[35m'
BLUE = '\u001b[34m'
BOLD = '\u001b[1m'


def Notice():
    print("""Welcome to the Tic Tac Toe Game,
                               by Apurba Ghosh
This Game involves two Functionality, 1. Player vs Player 
                                      2. Player vs Computer
Choose an Option from 1 or 2 to Start the game, There are some
functionalities to be noticed, if you want to Quit the game at 
any point of time, just type ('exit',) as input, 
Rules:
    1) You can't choose a column already filled, doing that it will
    give a prompt as many times as you do that.
    
    2) Type your name at the very first starting of the program.
    
    3) Avoid Choosing the same variable for both the user, if played 
    Player vs Player.
    
    4) You will always have to Give the same Variable which you have 
    given as the very first input at the starting of the game, note: 
    that you are free to choose any Variables or even numbers and not
    limited to only (X/O). Henceforth, Freedom is granted.
                \n\n""")
    

def choice():
    x = int(input("""1. Player vs Player
2. Player vs Computer \t Choose: """))
    return (x)


def board(container : str = "", screenwidth : int = 59, sign1 = " ", sign2 = " ", sign3 = " "):
    counter = 0
    while (counter <= 21):
        if (counter == 0 or counter == 14 or counter == 7 or counter == 21):
            container = f"{YELLOW}-{RESET}" * screenwidth
            print(container)
            counter += 1
            continue
        
        if (counter == 3):
            container = f"{YELLOW}|{RESET}          {data_dic['a']}       {YELLOW}|{RESET}          {data_dic['b']}        {YELLOW}|{RESET}          {data_dic['c']}       {YELLOW}|{RESET}" f"{sign1}"
            print(container)
            counter += 1 
            continue
        
        if (counter == 10):
            container = f"{YELLOW}|{RESET}          {data_dic['d']}       {YELLOW}|{RESET}          {data_dic['e']}        {YELLOW}|{RESET}          {data_dic['f']}       {YELLOW}|{RESET}" f"{sign2}"
            print(container)
            counter += 1
            continue
            
        if (counter == 17):
            container = f"{YELLOW}|{RESET}          {data_dic['g']}       {YELLOW}|{RESET}          {data_dic['h']}        {YELLOW}|{RESET}          {data_dic['i']}       {YELLOW}|{RESET}" f"{sign3}"
            print(container)
            counter += 1
            continue
            
        else:
            container = f"{YELLOW}|                  |                   |                  |"
            print(container)
            counter += 1
               
        
def check(a : str ,b : str ,c : str ,d : str ,e : str ,f : str ,g : str ,h : str ,i : str ):
    
    # Part 1:
    if (a == b == c):
        return (a)
    if (d == e == f):
        return (d)
    if (g == h == i):
        return (g)
    
    # Part 2:
    if (a == d == g):
        return (a)
    if (b == e == h):
        return (b)
    if (c == f == i):
        return (c)
    
    # Part 3:
    if (a == e == i):
        return (a)
    if (c == e == g):
        return (c)
    else:
        return (" ")
    
      
def computerOverwrite(user : str):
    if (data_dic[user] != " "):
        return (True)
    else:
        return (False)

def overwrite(user : tuple):
    if (data_dic[user[1]] != " "):
        print(f"{RED}Sorry the Column is already filled, Please Choose any other Column...{RESET}")
        return (True)
    else:
        return (False)

 
def game():
    Notice()
    choices = choice()
    name2 = ""
    if choices == 2:
        name1 = input('Player 1, Enter Your Name: ')
    else:
        name1 = input('Player 1, Enter Your Name: ')
        name2 = input('Player 2, Enter Your Name: ')
    board()
    winner = ""
    counter = 1
    continuous_check = " "
    f = ""
    while (counter <= 9):
        if (counter%2 != 0):
            user1 = eval(input("Player 1, Enter the Cloumn: "))
            if (user1[0] == 'exit'):
                print("Thanks For Playing")
                f = 'a'
                break
            if (Choice_dict['Player 1'] == " "):
                pass
            else:
                if (Choice_dict['Player 1'] == user1[0]):
                    pass
                else:
                    print(f"{RED}Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}{RESET}")
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                    if (user1[0] == 'exit'):
                        print(f"{BLUE}Thanks For Playing{RESET}")
                        f = 'a'
                        break
                    while (user1[0] != Choice_dict['Player 1']):
                        print(f"{RED}Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}{RESET}")
                        user1 = eval(input("Player 1, Enter the Cloumn: "))
                        if (user1[0] == 'exit'):
                            print(f"{BLUE}Thanks For Playing{RESET}")
                            f = 'a'
                            break
                    if (user1[0] == 'exit'):
                        f = 'a'
                        break
                    else:
                        pass
            info = overwrite(user1)
            if (info == True):
                user1 = eval(input("Player 1, Enter the Cloumn: "))
                if (user1[0] == 'exit'):
                    print(f"{BLUE}Thanks For Playing{RESET}")
                    f = 'a'
                    break
                while (user1[0] != Choice_dict['Player 1']):
                    print(f"{RED}Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}{RESET}")
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                    if (user1[0] == 'exit'):
                        print(f"{BLUE}Thanks For Playing{RESET}")
                        f = 'a'
                        break
                if (user1[0] == 'exit'):
                    f = 'a'
                    break
                info2 = overwrite(user1)
                while (info2 != False):
                    user1 = eval(input("Player 1, Enter the Cloumn: "))
                    if (user1[0] == 'exit'):
                        print(f"{BLUE}Thanks For Playing{RESET}")
                        f = 'a'
                        break
                    info2 = overwrite(user1)
                    if (Choice_dict['Player 1'] == user1[0]):
                        pass
                    else:
                        print(f"{RED}Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}{RESET}")
                        user1 = eval(input("Player 1, Enter the Cloumn: "))
                        if (user1[0] == 'exit'):
                            print(f"{BLUE}Thanks For Playing{RESET}")
                            f = 'a'
                            break
                        while (user1[0] != Choice_dict['Player 1']):
                            print(f"{RED}Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}{RESET}")
                            user1 = eval(input("Player 1, Enter the Cloumn: "))
                            if (user1[0] == 'exit'):
                                print(f"{BLUE}Thanks For Playing{RESET}")
                                f = 'a'
                                break
                        info2 = overwrite(user1)
                        
                if (user1[0] == 'exit'):
                    f = 'a'
                    break   
                else:
                    pass
            else:
                pass
            
            if (user1[1] == 'a'):
                data_dic['a'] = f"{RED}{user1[0]}{RESET}"
                board(sign1=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'b'):
                data_dic['b'] = f"{RED}{user1[0]}{RESET}"
                board(sign1=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'c'):
                data_dic['c'] = f"{RED}{user1[0]}{RESET}"
                board(sign1=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'd'):
                data_dic['d'] = f"{RED}{user1[0]}{RESET}"
                board(sign2=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'e'):
                data_dic['e'] = f"{RED}{user1[0]}{RESET}"
                board(sign2=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'f'):
                data_dic['f'] = f"{RED}{user1[0]}{RESET}"
                board(sign2=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'g'):
                data_dic['g'] = f"{RED}{user1[0]}{RESET}"
                board(sign3=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'h'):
                data_dic['h'] = f"{RED}{user1[0]}{RESET}"
                board(sign3=f"{GREEN} <<--- {RESET}")
            if (user1[1] == 'i'):
                data_dic['i'] = f"{RED}{user1[0]}{RESET}"
                board(sign3=f"{GREEN} <<--- {RESET}")
            Choice_dict['Player 1'] = user1[0]
            winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                   ,data_dic['g'],data_dic['h'],data_dic['i'])
            if (winner != " "):
                continuous_check = (True,winner)
                break
        else:
            if choices == 2:
                print("Computer's Turn...")
                column = ''
                for j in range(1):
                    column = random.choice(['a','b','c','d','e','f','g','h','i'])
                    info = computerOverwrite(column)
                    while (info != False):
                        column = random.choice(['a','b','c','d','e','f','g','h','i'])
                        info = computerOverwrite(column)
                if (column == 'a'):
                    data_dic['a'] = f"{CYAN}{var}{RESET}"
                    board(sign1=f"{YELLOW} <<--- {RESET}")
                if (column == 'b'):
                    data_dic['b'] = f"{CYAN}{var}{RESET}"
                    board(sign1=f"{YELLOW} <<--- {RESET}")
                if (column == 'c'):
                    data_dic['c'] = f"{CYAN}{var}{RESET}"
                    board(sign1=f"{YELLOW} <<--- {RESET}")
                if (column == 'd'):
                    data_dic['d'] = f"{CYAN}{var}{RESET}"
                    board(sign2=f"{YELLOW} <<--- {RESET}")
                if (column == 'e'):
                    data_dic['e'] = f"{CYAN}{var}{RESET}"
                    board(sign2=f"{YELLOW} <<--- {RESET}")
                if (column == 'f'):
                    data_dic['f'] = f"{CYAN}{var}{RESET}"
                    board(sign2=f"{YELLOW} <<--- {RESET}")
                if (column == 'g'):
                    data_dic['g'] = f"{CYAN}{var}{RESET}"
                    board(sign3=f"{YELLOW} <<--- {RESET}")
                if (column == 'h'):
                    data_dic['h'] = f"{CYAN}{var}{RESET}"
                    board(sign3=f"{YELLOW} <<--- {RESET}")
                if (column == 'i'):
                    data_dic['i'] = f"{CYAN}{var}{RESET}"
                    board(sign3=f"{YELLOW} <<--- {RESET}")
                winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                    ,data_dic['g'],data_dic['h'],data_dic['i'])
                Choice_dict['Computer'] = var
                if (winner != " "):
                    continuous_check = (True,winner)
                    break
            else:
                user2 = eval(input("Player 2, Enter the Cloumn: "))
                if (user2[0] == 'exit'):
                    print(f"{BLUE}Thanks For Playing{RESET}")
                    f = 'b'
                    break
                if (Choice_dict['Player 2'] == " "):
                    pass
                else:
                    if (Choice_dict['Player 2'] == user2[0]):
                        pass
                    else:
                        print(f"{RED}Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}{RESET}")
                        user2 = eval(input("Player 2, Enter the Cloumn: "))
                        if (user2[0] == 'exit'):
                            print(f"{BLUE}Thanks For Playing{RESET}")
                            f = 'b'
                            break
                        while (user2[0] != Choice_dict['Player 2']):
                            print(f"{RED}Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}{RESET}")
                            user2 = eval(input("Player 2, Enter the Cloumn: "))
                            if (user2[0] == 'exit'):
                                print(f"{BLUE}Thanks For Playing{RESET}")
                                f = 'b'
                                break
                        if (user2[0] == 'exit'):
                            f = 'b'
                            break
                        else:
                            pass
                info = overwrite(user2)
                if (info == True):
                    user2 = eval(input("Player 2, Enter the Cloumn: "))
                    if (user2[0] == 'exit'):
                        print(f"{BLUE}Thanks For Playing{RESET}")
                        f = 'b'
                        break
                    while (user2[0] != Choice_dict['Player 2']):
                        print(f"{RED}Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}{RESET}")
                        user2 = eval(input("Player 2, Enter the Cloumn: "))
                        if (user2[0] == 'exit'):
                            print(f"{BLUE}Thanks For Playing{RESET}")
                            f = 'b'
                            break
                    if (user2[0] == 'exit'):
                        f = 'b'
                        break
                    info2 = overwrite(user2)
                    while (info2 != False):
                        user2 = eval(input("Player 2, Enter the Cloumn: "))
                        if (user2[0] == 'exit'):
                            print(f"{BLUE}Thanks For Playing{RESET}")
                            f = 'b'
                            break
                        info2 = overwrite(user2)
                        if (Choice_dict['Player 2'] == user2[0]):
                            pass
                        else:
                            print(f"{RED}Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}{RESET}")
                            user2 = eval(input("Player 2, Enter the Cloumn: "))
                            if (user2[0] == 'exit'):
                                print(f"{BLUE}Thanks For Playing{RESET}")
                                f = 'b'
                                break
                            while (user2[0] != Choice_dict['Player 2']):
                                print(f"{RED}Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}{RESET}")
                                user2 = eval(input("Player 2, Enter the Cloumn: "))
                                if (user2[0] == 'exit'):
                                    print(f"{BLUE}Thanks For Playing{RESET}")
                                    f = 'b'
                                    break
                            info2 = overwrite(user2)
                            
                    if (user2[0] == 'exit'):
                        f = 'b'
                        break   
                    else:
                        pass
                else:
                    pass
                
                if (user2[1] == 'a'):
                    data_dic['a'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign1=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'b'):
                    data_dic['b'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign1=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'c'):
                    data_dic['c'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign1=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'd'):
                    data_dic['d'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign2=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'e'):
                    data_dic['e'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign2=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'f'):
                    data_dic['f'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign2=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'g'):
                    data_dic['g'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign3=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'h'):
                    data_dic['h'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign3=f"{YELLOW} <<--- {RESET}")
                if (user2[1] == 'i'):
                    data_dic['i'] = f"{CYAN}{user2[0]}{RESET}"
                    board(sign3=f"{YELLOW} <<--- {RESET}")
                    
                Choice_dict['Player 2'] = user2[0]
                winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
                    ,data_dic['g'],data_dic['h'],data_dic['i'])
                if (winner != " "):
                    continuous_check = (True,winner)
                    break


        counter += 1
    
    
    if f == 'a' or f == 'b':
        pass
    else:
        if (continuous_check[0] == True):
            key_list = list(Choice_dict.keys())
            value_list = list(Choice_dict.values())
            if (choices == 2):
                position1 = value_list.index('X')
                position2 = value_list.index(var) 
            else:
                position1 = value_list.index('X')
                position2 = value_list.index('O') 
            if (continuous_check[1] == f'{RED}X{RESET}'):
                if choices == 2:
                    if (key_list[position1] == "Player 1"):
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} {name1}")
                    else:
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} Computer.")
                else:
                    if (key_list[position1] == "Player 1"):
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} {name1}")
                    else:
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} {name2}")
            else:
                if choices == 2:
                    if (key_list[position2] == "Player 1"):
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} {name1}")
                    else:
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} Computer.")
                else:
                    if (key_list[position2] == "Player 1"):
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} {name1}")
                    else:
                        print(f"{MAGENTA}Congratulations! Winner of the Game is{BOLD} {name2}")
                    
        else:
            pass
if __name__ == '__main__':
    game()
    
    
""" 
My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
Also the Colors of each Variable and the Arrows pointing to the current input column is given, the Warning situation such as If entered a column 
already filled then it will give warning and choice to re-enter and if Choosed a variable which is not the same as choosed in the beginning
it will give a Warning and choice to re-enter, and all the Warnings and choice to re-enter are given untill the Choice is True with the given Conditions,
as mentioned before.The Player who takes the winning variable, his name gets displayed at the end while declearing the winner, and this is acheived 
by storing the variable choosed by each user at the beginning and then calling the key of the dictionary from the value. 
"""
  



