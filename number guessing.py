import random
secret_number = random.randint(1,100)
#print("guess a random number")
i = 0
while True:
        try:
            guess=int(input("enter a guess"))
            i+=1
            if guess < secret_number:
                print("ur number is too low")
            elif guess > secret_number:
                print("ur number is too high")
            else:
                print("the values is correct")
                break
        except ValueError:
            print("enter valid number")
