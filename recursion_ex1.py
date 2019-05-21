# gets the input of a string and returns it reversed recursivelytri

def string_reverse( string ):
    if string == "":                # base case at ""
        return string               # then return that symbol
    else:
        # switch every string, cutting off last character 
        return string_reverse( string[1:]) + string[0] 

# doesnt work
def rec_string( string, n=-1 ):
    if n != -5:
        print( string + '\n' )
        rec_string( string[-1:] ) 

# returns the euclidean gcd of both numbers 
def euclidGCD( num1, num2 ):
    if num2 == 0:                 # if second number is 0 
        return num1               # return the first number 
    else:
        return euclidGCD( num2, num1 % num2 )

def main():
    print ( string_reverse( "programming" ) ) 

    print( euclidGCD( 102, 68 ) ) 


        
if __name__ == '__main__':
    main() 
