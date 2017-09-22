import random 
min = 1 
max = 6
roll_again = "yes"
rolling = True
while rolling:
    print "Rolling the dice" 
    print "The values are"
    print random.randint(min,max)
    print random.randint(min,max)
    roll_again = raw_input("Roll the dice again?")
    roll1 = random
    print roll1
    roll2 = random
    print roll2
    if roll_again in [3, 5]:
        print "Win" 
    if roll_again in [1, 2, 4]:
        print "Lose"
    elif roll_again == 6:
        print "Win whole game"
roll_again("want to roll again? ")
    if roll_again!= "yes":
    rolling = False 