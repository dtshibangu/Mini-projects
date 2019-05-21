# program should display a letter grade
# for each score and average test score

# define variables
average = 0.0
test1 = 0
test2 = 0
test3 = 0
test4 = 0
test5 = 0

# define constants
A = 100
B = 89
C = 79
D = 69
F = 60

# main function prompts for 5 scores
# call calc_average and grade functions
# display results of both functions
def main():
    test1 = int( input( "Enter 1st test score: " ) ) 
    test2 = int( input( "Enter 2nd test score: " ) )
    test3 = int( input( "Enter 3rd test score: " ) )
    test4 = int( input( "Enter 4th test score: " ) )
    test5 = int( input( "Enter 5th test score: " ) )

    determine_grade( test1, test2, test3, test4, test5 )
    grade_list = determine_grade( test1, test2, test3, test4, test5 )

    calc_average( test1, test2, test3, test4, test5 )
    

    print( "Score\tGrade" )
    print( "---------------------" )
    for num in range( 1, ...... conotinue later 
    

        determine_grade( test1, test2, test3, test4, test5 ) )


# determine_grade returns letter grade
# of each argument
def determine_grade( test1, test2, test3, test4, test5 ):
    grades[] = { test1, test2, test3, test4, test5 }
    
    for num in range( 1, 5 ):
        if grade[num] < 100 and grade[num] > 89:
            return A
        elif grade[num] < 90 and grade[num] > 79:
            return B
        elif grade[num] < 80 and grade[num] > 69:
            return C
        elif grade[num] < 70:
            return D
        else:
            return F

# calc_average func returns the average
def calc_average( test1, test2, test3, test4, test5 ):
    average = test1 + test2 + test3 + test4 + test5 )
    return average

# call main fucntion
main()

    
