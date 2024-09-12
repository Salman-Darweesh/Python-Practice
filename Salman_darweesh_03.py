    # Welcoming the user, asking if they want to play a game -  SAW Version
choice_1 = input("Hello! Wanna play a game? (yes/no): ")
    # using and using .lowwer conversion to change character to lowercase
if (choice_1.lower() == "yes"):
    print("you cannot go back now")
    print
    
if choice_1 == "no":
    print("you have chosen the safe route of not playing")   

    # creating a counter
counter = 0 

if counter > 3 and counter < 2 == "Correct!":
    print("You Failed :P")

    # answers to the riddles
riddle_1 = "Your left hand"
riddle_2 = "A towel"
riddle_3 = "a rubber band"
rid_ans_4 = "G"
rid_ans_5 = "When it is ajar"

    #riddles given to the user
rid_ans_1 = input("What can you hold in your right hand, but never in your left hand? ")
if rid_ans_1.lower() == riddle_1: #creating a coutner to add to the original value of 0
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")

rid_ans_2 = input("What gets wet while drying? ")
if rid_ans_2 == "A towel":
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
rid_ans_3 = input("What kind of band never plays music? ")
if rid_ans_3 == "A rubber band":
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
rid_ans_4 = input("What is the end of everything? ")
if rid_ans_4 == "G":
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
rid_ans_5 = input("When is a door no longer a door? ")
if rid_ans_5 == "When it is ajar":
    print("Correct!")
    counter +=1
else:
    print("You got it wrong, L")
    
if counter < 3 and counter < 5 == "You escaped":
    print(f"there were", counter, "correct answers.")
else:
    print("You died")