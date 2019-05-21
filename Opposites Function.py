# Daniel Tshibangu
# program that determines if two integers input
# by the user are of opposite signs (i.e. one is
# positive and the other negative)

# create main function
# input variables prompt for a number
def main(): 
    num1 = int( input( "Enter first number: " ) )
    num2 = int( input( "Enter second number: " ) )

    #variables run through opposites function
    opposites( num1, num2 )

    # result is printed based on num1, num2
    print( "Are these numbers opposites?", opposites( num1, num2 ) ) 

# create opposites func takes two parameters	
def opposites( num1, num2 ):
    if num1 > 0 and num2 < 0:       # if num1 is pos and num2 is neg
        return True                 # prints true
    elif num2 > 0 and num1 < 0:     # if num2 is pos and num1 is neg
        return True                 # prints true 
    else:
        return False                # anything else is false

# calls the main fucntion
main()


