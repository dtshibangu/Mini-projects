# money counting game gets user to enter coins required to make dollar
# should prompt user to enter certain coin
# if coins equal to dollar, congratualte user
# if user loses prompt for how over or how under

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

total = 0

# prompt and store num of pennies, print current total 
penny_num = int( input( "Number of pennies: " ) )

total = total + ( penny * penny_num )

print( "Your current total:", format( total, '.2f' ))

# prompt and store num of nickels, print current total 
nickel_num = int( input( "\nNumber of nickels: " ) )

total = total + ( nickel * nickel_num )

print( "Your current total:", format( total, '.2f' ) )

# prompt and store num of dimes, print current total 
dime_num = int( input( "\nNumber of dime: " ) )

total = total + ( dime * dime_num )

print( "Your current total:", format( total, '.2f' ) )

# prompt and store num of quarters, print current total 
quarter_num = int( input( "\nNumber of quarter: " ) )

total = total + ( quarter * quarter_num )

print( "Your current total:", format( total, '.2f' ))

# conditional output for winning or losing
if total == 1.00:
    print( "\nCongratulations! You wiiiinnn!! :)" )
else:
    print( "\nBummer~" ) 
