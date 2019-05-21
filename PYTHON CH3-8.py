# program that outputs color based on number input 

#prompt user for number and store 
num = int( input( "Input a number and corressponding color: " ) )

#create heirarchy for color selection based on numbers
if num == 0:
    print( "You have selected green." )
else:
    if num >= 1 and num <= 10:
        if num % 2 == 1:
            print( "You have selected red." )
        else:
            print( "You have selected black." )
    else:
        if num >= 11 and num <= 18:
            if num % 2 == 1:
                print( "You have selected black." )
            else:
                print( "You have selected red." )
        else:
            if num >= 19 and num <= 28:
                if num % 2 == 1:
                    print( "You have selected red." )
                else:
                    print( "You have selected black." )
            else:
                if num >= 29 and num <= 36:
                    if num % 2 == 1:
                        print( "You have selected black." )
                    else:
                        print( "You have selected red." )
                else:
                    print( 'INVALID ENTRY! MUST BE BETWEEN 1 AND 36!' )
                    

