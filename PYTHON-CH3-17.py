# create a program for solving a wifi problem

# variable for solution outcome
solution = "\nProblem Solved."

# intro and prompt user for a entering input 
input( "Welcome to the WiFI Troubleshooting System." )
userIn = input( "Do you have a problem with your WiFi connectivity? " )

# create conditionals and print results
if userIn == 'no':
    print( solution )
else:
    print( "\nReboot the computer and try to connect." )
    userIn = input( "Did that fix the problem? " )
    if userIn == 'yes':
        print( solution )
    else:
        print( "\nReboot the router and try to connect." )
        userIn = input( "Did that fix the problem? " )
        if userIn == 'yes':
            print( solution )
        else:
            print( "\nMake sure the cables between the router" \
                   " & modem are plugged in firmly." )
            userIn = input( "Did that fix the problem? " )
            if userIn == 'yes':
                print( solution )
            else:
                print( "\nMove the router to a new location and try to connect." )
                userIn = input( "Did that fix the problem? " )
                if userIn == 'yes':
                    print( solution )
                else:
                    print( "\nGet a new router." )
                    print( solution )

            
