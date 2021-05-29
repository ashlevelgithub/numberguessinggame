import random
number_range = random.randrange(1,10)

print ("Hey! I'm Autobot, I am a guess the number robot!")
print ("Please pick an integer number between 1-10 and I will tell you if you got the number in question!")

question_answer = input( ("Are you ready to proceed? Please type yes or no in lowercase to proceed "))

if question_answer == "yes":
    print ("Perfect!")
    player_input = int(input("Please enter your guess: "))
    if player_input == number_range:
        print ("Dang! You actually got it! Congratulations!! You win :)")

    elif player_input <number_range:
        print ("Your guess was too low, just like your self esteem.")

    else:
        print ("Your guess was too high, just like you right now.")


elif question_answer == "no":
    print ("No worries, we will play another day!")
    quit()

else:
    print ("Thats not one of the given choices, i'm leaving because you are being a terrible sport.")
    quit()