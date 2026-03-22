Player1=input("Player 1, Enter Rock, Paper, or Scissors ")

Player2=input("PLayer 2, Enter Rock, Paper or Scissors ")

while True:
    if Player1 == "Rock" and Player2 == "Scissors":
        print("Player 1 wins!")

    elif Player1 == "Paper" and Player2 == "Scissors":
        print("Player 2 wins!")

    elif Player1 == "Scissors" and Player2 == "Rock":
        print("PLayer 2 wins!")

    elif Player1 == "Rock" and Player2 == "Paper":
        print("Player 2 wins!")

    elif Player1 == "Scissors" and Player2 == "Paper":
        print("Player 1 wins!")

    elif Player1 == "Paper" and Player2 == "Rock":
        print("Player 1 wins!")

    elif (Player1 == "Rock"  or Player1 == "Scissors" or Player1 ==  "Paper") and (Player2 == "Rock" or Player2 == "Scissors" or Player2 == "Paper") and Player1==Player2:
            print("Tie")

    else:
        print("Error, Please enter Rock, Paper or Scissors")
        Player1 = input("Player 1, Enter Rock, Paper, or Scissors ")

        Player2 = input("PLayer 2, Enter Rock, Paper or Scissors ")

    user_input= input("Would you like to play again?")
    if user_input == "Yes" or user_input == "yes":
        Player1 = input("Player 1, Enter Rock, Paper, or Scissors ")

        Player2 = input("PLayer 2, Enter Rock, Paper or Scissors ")
    else:
        exit()











