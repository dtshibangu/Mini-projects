# program aks users to enter a year and identify a leap year

# set up programming constants for february 
LEAP_YEAR = 29
NORM_YEAR = 28

# prompt user for number of years and store 
year = int( input( "Enter a year: " ) )

# create conditional statemtents for years entered
if year % 100 == 0:
    if year % 400:
        print( 'In', year, 'February has', LEAP_YEAR, 'days.' )
else:
    if year % 4 == 0:
        print( 'In', year, 'February has', LEAP_YEAR, 'days.' )
    else:
        print( 'In', year, 'February has', NORM_YEAR, 'days.' )
