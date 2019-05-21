# ransom note
# this program will determine elements of a given string are in
# a ransom through a dictionary

# the main fucntion will prompt for a string
# create a dictioanry for letters in magazine
# and call fucntions to assess the strings
def main():
    ransom_note = input( "Enter ransom note: " )
    magazine = input( "Enter magazine text: " )

    result = decoder( ransom_note, magazine )

    # print results
    print( "Is it possible to create the given ransom note?" )  
    if 0 in result.values():
        print( False )
    else:
        print( True ) 


# the decoder function will compare both
# strings, detect if note in magazine
def decoder( ransom_note, magazine ):
    dictionary = {}

    # initialize ransom letter to dict
    for letter in ransom_note:
        dictionary[ letter ] = 0


    # get letter count, stores in dict 
    # onlyt if num of letters is enough
    for letter in ransom_note:
        if magazine.count( letter ) >= ransom_note.count( letter ):
            dictionary[ letter ] = magazine.count( letter )

    return dictionary

# call the main function
if __name__ == '__main__':
    main()

            
    
                
                
    

    

    
