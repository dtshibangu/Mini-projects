#Daniel Tshibangu
# Assignment 1: Day of the Week
# displays day of the week along with number in accordance with that day
# range from 1 - 7,if not display an error messge

# state each variable 
day = 0
mon = 0
tues = 0
wed = 0
thurs = 0
fri = 0
sat = 0
sun = 0

# set every weekday to corresponding numbers
mon, tues, wed, thurs, fri, sat, sun = 1, 2, 3, 4, 5, 6, 7

# get input from user, store in day 
day = int( input( 'Enter a number per day of the week(1-7): ' ) )

# set error condition if outside range 
if ( day < 1 or day > 7 ):
    print( "ERROR! OUT OF RANGE!" )
else:
    # otherwise print for selected day 
    if ( day == mon ):
        print( "You have selected: Monday" )
    elif day == tues :
        print( "You have selected: Tuesday" )
    elif day == wed :
        print( "You have selected: Wednesday" )
    elif day == thurs :
        print( "You have selected: Thursday" )
    elif day == fri:
        print( "You have selected: Friday" )
    elif day == sat:
        print( "You have selected: Saturday" )
    elif day == sun:
        print( "You have selected: Sunday" )

