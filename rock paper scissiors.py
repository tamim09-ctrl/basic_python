import random
print("welcome to rock paper scissors game good luck mate")
while True:
    
    user = input("enter rock paper scissiors or (exit)?:").lower()

    if user == "exit":
       print("byee")
       break
    if user not in ["rock","paper","scissors"]:
       print("invalid")
       continue
    computer_choice=random.choice(["rock","paper","scissors"])
    print("choice of computer",computer_choice)
    if user == computer_choice:
        print("its a tie")
    elif (user == "rock" and computer_choice == "scissors") or (user == "paper" and computer_choice == "rock") or (user == "rock" and computer_choice =="paper"):
          
              print("yaaaaah you won")
    else:
        print("you loser")
