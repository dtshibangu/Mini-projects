# asks for month, day, two digit year
# determine if month * day == year number
#if so display message saying date is magic
# display message if not magic

#prompt for times of month
month = int( input( 'Enter numerical month between 1-12: ' ) )
day = int( input ( 'Enter number of day: ' ) )
year = int( input( 'Enter last two digits of year: ' ) )

#create conditions and limits
if month < 1 or month > 12:
    print( "INVALID ENTRY!" )
    month = 2
    if day < 1 or day > 31:
        print( "INVALID ENTRY!" )
        day = 2
        if year < 0 or year > 99:
            print( "INVALID ENTRY!" )
            year = 2

        
print( '\nYou entered: ', end="" )
print( month, day, year, sep='/' )

if (month * day) == year:
    print( 'WOW!! THIS DAY IS MAGICAL~~~' )
else:
    print( 'Oh.... man this day sucks....' )

