# this program converts strings to morse code

 # create list of characters
characters = [ ' ', ',', '.', '?',          # special char
               '0', '1', '2', '3', '4',     # numbers
               '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E',     # letters
               'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z' ]
    
morse = [ ' ', '--.--', '.-.-.-', '..--..',
          '-----', '.----', '..---', '...--', '....-',
          '.....', '-....', '--...', '---..', '----.',
          '.-', '-...', '-.-.', '-..', '.', '..-.',
          '--.', '....', '..', '.---', '-.-', '.-..',
          '--', '-.', '---', '.--.', '--.-', '.-.',
          '...', '-', '..-', '...-', '.--', '-..-',
          '-.-', '--..' ]
    
def main():
    my_string = input( "Enter a string: " )

    convert_to_morse( my_string )

    print( "To morse code:", convert_to_morse( my_string ) )

def convert_to_morse( my_string ):
    morse_code = ''
    
    for value in my_string:
        for char in characters:
            if value.upper() == characters[ char ]:
                for code in morse:
                    morse_code += morse[ int( character[ char ] ) ]

    return morse_code

# call the main function
main()
            
            

    
