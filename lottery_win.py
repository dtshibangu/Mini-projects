# make a powerball application

import random

def main():
    # list constants
    NUM_LIMIT = 5
    counter = 0
    
    # make lists
    lotto_ticket = []
    winning_ticket = []

    # ask for manual or random ticket
    ticket_type = input( "Would you like a manual ticket(M)" +
                         "or a random ticket(R)?" )
    
    if ticket_type.upper() == 'R':
        # add normal 5 numbers 
        for counter in range( NUM_LIMIT ):
            random_lotto = random.randint( 1, 70 )
            lotto_ticket.append( random_lotto )

        # add powerball num to your ticket 
        for powerball_num in range( 1, 27 ):
            lotto_ticket.append( powerball_num )
    else:
        # tell to input numbers
        while len( lotto_ticket ) <= NUM_LIMIT:
            print( "Input ticket number",
                   str( index( lotto_ticket[0])+1 ),  ": " )
            choice_num = input() 
            lotto_ticket.append( choice_num )

    # make the winning lotto ticket
    for counter in range( NUM_LIMIT ):
        random_winner = random.randint( 1, 70 )
        winning_ticket.append( random_winner )

    # add powerball num to winning ticket 
    powerball_num = random.randint( 1, 27 ) 
    winning_ticket.append( powerball_num )

    # see if they match
    for lotto_num in lotto_ticket:
        for win_num in winning_ticket:
            if lotto_ticket[ lotto_num ] == winning_ticket[ win_num ]:
                counter += 1

    print( "The winning numbers of today's lottery are:",
           winning_ticket ) 
    if counter == 6:
        print( "Congratulations!! You've won!!")
    else:
        print( "Try again next time." )

# call the main function
main()

    
            
            

    
