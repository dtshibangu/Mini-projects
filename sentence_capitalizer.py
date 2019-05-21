# this program will return a string with first letter capitalized

def capitalize( sentence, user_sent ):

    # append each charcter to list
    for char in user_sent:
        sentence.append( char )

    # uppercase the first word of sentence
    sentence[0] = sentence[0].upper()

    user_sent = "".join( sentence )

# call the main function
capitalize( sentence, user_sent )
