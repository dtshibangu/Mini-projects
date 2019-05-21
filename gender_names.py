# this program will search for boy or girl names
# from the girlnames.txt and boynames.txt files

def main():
    # define variable for search
    gender = ''
    found = False
    
    # create a list
    boy_list = []

    # ask the user which list they want
    gender = input( "Enter boy or girl search: "  )
    if gender == 'boy':
        search =  input( "Enter boy name: " )

        if search in boy_search( search, boy_list ):
            print( search, "is there." )
    



# boy_seach function searches for boy name
# returns bool if found or not
def boy_search( search, boy_list ):
    # open the file
    boyfile = open( 'boynames.txt', 'r' )

    for line in boyfile:
        names = boyfile.readline()
        names = names.rstrip( '\n' )
        boy_list.append( names )
        
    # Close the file
    boyfile.close()

    return boy_list

# call main function
main()

    
