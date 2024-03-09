# File: CS112_A1_T2_1_20230117.py.
# Purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum.The player who reaches 100 wins.
# Author: Habeba Hossam
# ID: 20230117
while True:
    sum = 0 # Initialize the sum to 0 for each new game
    choice = input("1) Start new game \n2) Exit\n")
    if choice == "1":
        # Welcome message and display status
        print("Welcome to 100 game")
        print("sum is 0")
        # Game playing
        is_true = 1
        while True: # Loop until the game is finished
            if is_true == 2:    #to avoid compeating the game
                break
            elif is_true == 1:
                num1_1 = input("Player_1: Please select a number from 1 to 10: ")
                if num1_1.isdigit() == True :
                    num1 = int(num1_1)
                    if num1 >= 1 and num1 <= 10:  #cheek player_1 enter a valid number
                        sum += num1
                        if sum < 100:
                            print(f'summation = {sum}')
                            is_true = 0     # Switch to Player 2's turn
                            while is_true == 0: # Loop until Player 2 enters a valid number
                                num2_2 = input("Player_2: Please select a number from 1 to 10: ")
                                if num2_2.isdigit()==True :
                                    num2 = int (num2_2)
                                    if num2 >= 1 and num2 <= 10: #cheek player_2 enter a valid number
                                        sum += num2
                                        if sum < 100:
                                            print(f'summation = {sum}')
                                            is_true = 1  # Switch to Player 1's turn
                                        elif sum == 100:
                                            print(f'summation = {sum}')
                                            print("player_2 is the winner")
                                            is_true = 2
                                            break #to avoid compeating the game
                                        elif sum > 100:
                                            sum -= num2
                                            print("choose number makes sum 100") # to avoid  player_1 enter mumber makes um greater than 100 
                                            is_true = 0 # Stay in Player 2's turn loop
                                            continue #to allow player_2 enter a valid number
                                    else:
                                        print("please enter a valid number")
                                        is_true = 0 # Stay in Player 2's turn loop
                                        continue #to allow player_1 enter a valid number
                                else :
                                    print("please enter a valid number")
                                    continue

                        elif sum == 100:
                            print(f'summation = {sum}')
                            print("player_1 is the winner")
                            break #to avoid compeating the game
                        elif sum > 100:
                            sum -= num1
                            print("choose number makes sum 100") # to avoid  player_1 enter mumber makes um greater than 100 
                            continue #to allow player_1 enter a valid number
                    else:
                        print("please enter a valid number")
                        continue #to allow player_1 enter a valid number
                else :
                    print("please enter a valid number")
                    continue
    elif choice == "2":
        print("Exit")
        break # to exit the game
    else:
        print("please select a valid number")
        continue #allow user enter a valid choice