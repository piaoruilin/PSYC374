import random

def random_num():
    return str(random.randint(100, 999))

def game_user_input(user_input, answer):
    for i in range(len(user_input)):
        if user_input[i] in answer:
            if user_input[i] == answer[i]:
                print(f"{user_input[i]} is in the correct position: {i+1}")
            else:
                print(f"{user_input[i]} is included but in the wrong position.")

def play_game():
    answer = random_num()
    turn_left = 0
    
    while True:
        user_input = input("Input a three digit number: ")
        
        if not user_input.isnumeric() or len(user_input) != 3:
            print("Try again.")
            continue
            
        turn_left += 1
        if user_input == answer:
            print("That's correct!")
            break
        else:
            game_user_input(user_input, answer)
        
        if turn_left >= 3:
            choice = input("You have failed more than 3 times. Would you like to try again? (y/n)")
            if choice == 'n':
                break
            else:
                answer = random_num()
                turn_left = 0

play_game()
