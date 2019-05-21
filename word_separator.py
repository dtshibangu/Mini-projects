# split sentence and capitalize first

def main():
    # get sentence from user 
    user_string = input( "Enter a sentence:\n->" )
    sentence_holder = []

    # split the sentence and capitalize first character 
    for letter in user_string:  
        if letter.isupper() and letter.isalpha():
            letter_mod = " "  + letter 
            correct_string = user_string.replace( letter, letter_mod )
            
        # make all letters lowercase 
        correct_string[ 0 ].upper()

        capitalize( sentence_holder, user_string )  

    print( correct_string  )

def capitalize( sentence_holder, user_string ):

    # append each charcter to list
    for char in user_string:
        sentence_holder.append( char )

    # uppercase the first word of sentence
    sentence_holder[0] = sentence_holder[0].upper()

    user_string = "".join( sentence_holder )

# call the main function
main()
