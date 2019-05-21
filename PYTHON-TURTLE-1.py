#import turtle and view turtle 
import turtle
turtle.showturtle()

# set color of the cursor
turtle.fillcolor( 'blue' )
turtle.begin_fill()

# set first diagonal line
turtle.setheading( 45 )
turtle.forward( 100 )

# set second diagonal line
turtle.setheading( 315 )
turtle.forward( 100 )

# set third diagonal line
turtle.setheading( 225 )
turtle.forward( 100 )

# set final diagonal line, set first of second diamond
turtle.setheading( 135 )
turtle.forward( 200 )

# set second diagonal line
turtle.setheading( 225 )
turtle.forward( 100 )

# set third diagonal line
turtle.setheading( 315 )
turtle.forward( 100 )

# set fourth diagonal line
turtle.setheading( 45 )
turtle.forward( 100 )

# fill both shapes with blue color, cursor 
turtle.end_fill()
turtle.hideturtle()

