# "Guess the number" mini-project
# The first player thinks of a secret number in some known range ([0,100) or [0,1000))
# while the second player attempts to guess the number. After each guess, the first 
# player answers either “Higher”, “Lower” or “Correct!” depending on whether the secret
# number is higher, lower or equal to the guess. In this project, I built a simple
# interactive program in Python where the computer will take the role of the first player
# while you play as the second player.
# The number of guesses is limited depending on the range
# Input will come from buttons and an input field
# All output for the game will be printed in the console

import simplegui
import random
import math

# Global variables
#secret_number = 0     #Number to be guessed
limit_interval = 100   #Right limit of the interval, can be 100 o 1000
n=0                    #Number of guesses

# helper function to start and restart the game
def new_game():
    # initializes the game with a new number in [0,limit_interval)
    global secret_number
    secret_number = random.randrange(0,limit_interval)
    print "New Game! Range is [0," + str(limit_interval) +")"
    
    #Max number of guesses
    global n
    n = int(math.log(limit_interval+1)/math.log(2))+1
    print "Number of remaining guesses is " + str(n)
        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global limit_interval
    limit_interval = 100
    new_game()
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global limit_interval
    limit_interval = 1000
    new_game()
    
        
def input_guess(guess):
    # Convert string to integer	
    num_guess = int(guess)
    print
    print "Your guess was " + guess
    
    #Updaiting number of guesses
    global n
    n -=1
    print "You have " + str(n) + " remaining guesses"
    #Check for ramaining guesses
    if (n != 0):
        
        # Compares the entered number to secret_number and prints out an 
        # appropriate message 
        if (secret_number < num_guess):
            print "Lower!"
        elif (secret_number == num_guess):
            print "Correct! You won!"
            print
            new_game()
        else:
            print "Higher!"
    elif (secret_number == num_guess):
        print "You guessed the number in your last chance!"
        print
        new_game()
    else:
        print "The number was " + str(secret_number) + ". You lost"  
        print
        new_game()
    
    
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_input("Enter a guess",input_guess, 200 )
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)


# call new_game to ensure that secret_number is always initialized 
# when the program starts running
new_game()

# Start frame
frame.start()

# always remember to check your completed program against the grading rubric
