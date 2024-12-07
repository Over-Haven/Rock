import random
option = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper, Scissors :")

computer_choice = random.choice(option)

print("You chose :", user_choice)
print("computer chose :", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "scissors":
    print("Rock smashes scissors, You winn!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper cover Rock, You winn!")
elif user_choice == "scissors" and computer_choice == "Paper":
    print("Scissor cuts paper, You winn!")
else:
    print("You lose!!")