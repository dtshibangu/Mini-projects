# program calculates and displays persons body mass index

height = float( input( "Enter your height in inches: " ) )

weight = float( input( "Enter your weight in pounds: " ) )

bmi = weight * ( 703 / height**2 )

if bmi >= 18.5 and bmi <= 25:
    result = 'optimal'
else:
    if bmi < 18.5:
        result = 'underweight'
    else:
        if bmi > 25:
            result = 'overweight'

print( 'Height entered:', height, 'in.' )
print( 'Weight entered:', weight, 'lbs.' )
print( 'Your BMI is:', format( bmi, '.2f' ) )
print( 'Evaluation: ' + result )
