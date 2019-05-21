# create a program that returns phone number

def main():
    # create a list
    phone_num_list = []
    
    # create var
    phone_num = input( "Enter phone number: " )

    letter_to_num( phone_num ) 

    print( phone_num_list )

def letter_to_num( phone_num, phone_num_list ):
    for num.upper() in phone_num:
        if num == 'A' or num == 'B' or num == 'C':
            num = 2
        elif num == 'D' or num == 'E' or num == 'F':
            num = 3
        elif num == 'G' or num == 'H' or num == 'I':
            num = 4
        elif num == 'J' or num == 'K' or num == 'L':
            num = 5
        elif num == 'M' or num == 'N' or num == 'O':
            num = 6
        elif num == 'P' or num == 'Q' or num == 'R' or num == 'S':
            num = 7
        elif num == 'T' or num == 'U' or num == 'V':
            num = 8
        elif num == 'W' or num == 'X' or num == 'Y' or num == 'Z':
            num = 9
            
        phone_num_list.append( num )

# call the main function
main()
    
    
