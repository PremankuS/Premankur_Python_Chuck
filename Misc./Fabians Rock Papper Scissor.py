import random;

options = (1,2,3)

while True:
    user_input = raw_input("Please enter your choice:")
    uinput = user_input.lower()
    if uinput != "rock" "paper" "scissor":
        print ("input valid words only! 'rock' 'paper' or 'scissor'")

    computer_input = random.choice(options)
    if computer_input == 1:
        cinput = "rock"
    elif computer_input == 2:
        cinput = "paper"
    elif computer_input == 3:
        cinput = "scissor"

    print uinput,cinput

    try:
        if uinput == ("done"):
            break
        elif cinput == uinput:
            print("draw")
        elif uinput == "rock" and cinput == "paper":
            print("computer wins")
        elif uinput == "paper" and cinput == "rock":
            print("you win")
        elif uinput == "scissor" and cinput == "rock":
            print("computer wins")
        elif uinput == "rock" and cinput == "scissor":
            print("you win")
        elif uinput == "paper" and "cinput" == "scissor":
            print("computer wins")
        elif uinput == "scissor" and cinput == "paper":
            print("you win")
    except ValueError:
        print("input valid words")



