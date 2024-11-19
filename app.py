import random

def winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        return "It's a tie!"
    elif (user_choice =='rock' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper') or (user_choice =='paper' and computer_choice=='rock'):
        return "You Win!"
    else:
        return "Computer Wins"
    
def play_game(rounds):
    user_score = 0
    computer_score = 0
    choices=['rock', 'paper', 'scissors']
    
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}")
        
        user_choice = input("Enter your choice (rock, paper or scissors:)").lower()
        
        while user_choice not in choices:
            print("Invalid choice! Please enter 'rock','paper', or 'scissors'")
            user_choice = input("Enter your choice (rock, paper or scissors:)").lower()
            
        computer_choice = random.choice(choices)
        print(f"Computer choice: {computer_choice}")
        
        
        result = winner(user_choice, computer_choice)
        print(result)
        
        if result=="You Win!":
            user_score+=1
        elif result == "Computer Wins":
            computer_score+=1
            
            
        if user_score==(rounds //2) +1:
            print("You won the game!")
            break
        elif computer_score==(rounds//2)+1:
            print("Computer won the game!")
            break
    if user_score> computer_score:
        print(f"You won the game with {user_score} points!")
    elif computer_score > user_score:
        print(f"Computer won the game with {computer_score} points!")
    else:
        print("It's a tie game!")
        
        
rounds= int(input("Enter the number of rounds (3 or 5): "))
while rounds not in [3 , 5]:
    print("Invalid number of rounds! Choose 3 or 5.")
    rounds = int(input("Enter the number of rounds (3 or 5): "))
    
play_game(rounds)