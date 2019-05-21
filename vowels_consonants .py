# this program returns the number of vowels string contains

user_string = ''

def vc_counter( user_string ):
    # get string from the user
    user_string = input( "Enter a string: " )

    # make tuple of consonants and vowels
    vowels = ( 'a', 'e', 'i', 'o', 'u' )
    consonants = ( 'b', 'c', 'd', 'f', 'g', 'h', 'j',
                    'k', 'l', 'm', 'n', 'p', 'q', 'r',
                    's', 't', 'v', 'w', 'x', 'y', 'z' )

    # make counter for vowels and consonants
    vow_count = 0
    cons_count = 0

    # for each character in string, get vowel
    for char in user_string:
        for letter in vowels:
            if char == letter:
                vow_count += 1

    # for each chararcter in string, get consonants
    for char in user_string:
        for letter in consonants:
            if char == letter:
                cons_count += 1

    # print the results
    print( "There are", vow_count, "vowels." )
    print( "There are", cons_count, "consonants." )

# call vc_counter function
vc_counter( user_string ) 
    
                
            
