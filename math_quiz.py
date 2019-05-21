# program will consistently give number of math
# questions that the user will answer

#random function allows random questions
import random

#state variables
addend1 = 0
addend2 = 0
user_answer = 0
correct_answer = 0

# main function gives problem and
# prompts for user answer, then prints
def main():
    intro()
    
    addend1 = random.randint( 1, 500 )
    addend2 = random.randint( 1, 500 )
    
    math_problem( addend1, addend2 )

# intro program will introduce and guide
# user to start math quiz
def intro():
    input( "Press enter/return to continue." ) 
    input( "Answer the given math problem:"  )

# defines correct_answer, prints format
def math_problem( addend1, addend2 ):
    correct_answer = addend1 + addend2

    print( '\t', addend1, '\n+\t', addend2, '\n-------------', sep='' ) 
    user_answer = int( input( "Answer: " ) ) 

    if user_answer == correct_answer:
        print(  "That is correct!" )
    else:
        print( "Incorrect! The correct answer is:", correct_answer )

# calls the main function
main()

