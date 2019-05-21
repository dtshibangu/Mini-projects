# desihn program that gets two colors for mixing and prints result
# if anything other than select colors are inoutted, error output

red_color = 'red'
blue_color = 'blue'
yellow_color = 'yellow'

color1 = input( "Enter the first color: " )

if color1 == red_color:
    print( "The first color is red.\n" )
else:
    if color1 == blue_color:
        print( "The first color is blue.\n" )
    else:
        if color1 == yellow_color:
            print( "The first color is yellow.\n" )
        else:
            print( "INVALID COLOR!\n" )



color2 = input( "Enter the second color: " )

if color2 == red_color:
    print( "The second color is red.\n" )
else:
    if color2 == blue_color:
        print( "The second color is blue.\n" )
    else:
        if color2 == yellow_color:
            print( "The second color is yellow.\n" )
        else:
            print( "INVALID COLOR!\n" )


if color1 == red_color and color2 == blue_color:
    print( "Red and Blue make PURPLE~" )
else:
    if color1 == red_color and color2 == yellow_color:
        print( "Red and Yellow make ORANGE!" )
    else:
        if color1 == blue_color and color2 == yellow_color:
            print( "Blue and Yellow make GREEN" )
        else:
            print( "INVALID ENTRIES!" )



