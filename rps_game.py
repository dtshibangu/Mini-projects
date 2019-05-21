# program lets users play rock paper scissors

#import the random module
import random 

# define variables
rock = 1
paper = 2
scissors = 3
player_choice = 0
com_choice = 0

#define limits
CHOICE_LIMIT = 3

# main function will ask for user
# choice and call oppoenent_choice function
# then display the results
def main():
    intro()
    
    player_choice = input( "\nEnter your choice: " ) 
    com_choice = random.randint( 1, CHOICE_LIMIT )

    com_choice_trans( com_choice ) 

    rps_game( player_choice, com_choice )

    print( "\nThe computer chose", com_choice_trans( com_choice ) )
    print( rps_game( player_choice, com_choice ) )

# intro function informs player of
# whatr they need to do and win game 
def intro():
    input( "Press enter to proceed with prompts." )
    input( "Welcome to Rock, Paper, Scissors!" )
    input( "Your opponent will be COM 1," )
    input( "Please enter your choice of 'rock' " +
           "'paper' or 'scissors'." ) 

# com_choice_trans function will equate the
# integer numbers to rock,paper or scissor
def com_choice_trans( com_choice ):
    if com_choice == 1:
        return "rock"
    elif com_choice == 2:
        return "paper"
    else:
        return "scissors"

# rps_game function will initiate the game
# and choose the winner, display results
def rps_game( player_choice, com_choice ):

    if player_choice == "rock":
        if com_choice == 3:
            return "You won!"
        elif com_choice == 2:
            return "You lost!"
    elif player_choice == "paper":
        if com_choice == 1:
            return "You won!"
        elif com_choice == 3:
            return "You lost!"
    elif player_choice == "scissors":
        if com_choice == 2:
            return "You won!"
        elif com_choice == 1:
            return "You lost"
    else:
        return "It's a tie!!"

#call the main function
main()

# incomplete, no code for game tie
            
