# program that prompts for weight of package, shows shipping charges

# prompt and store weight 
weight = float( input( 'Enter weight of package in pounds: ' ) )

# create conditionals for weight
if weight <= 2:
    rate = 1.50
else:
    if weight > 2 and weight <= 6:
        rate = 3.00
    else:
        if weight > 6 and weight <= 10:
            rate = 4.00
        else:
            if weight > 10:
                rate = 4.75

# print info 
print( "Weight entered in Pounds:", weight, 'lbs' )
print( "Rate per Pound: ${}".format( rate, '.2f' ) )
