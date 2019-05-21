# program that asks for the length and width of two rectangles
# should tell the user which rectangle has greater area, of if equal

length1 = float( input( "Enter first triangle length: " ) )
width1 = float( input( "Enter first triangle width: " ) )

rect1_area = length1 * width1

length2 = float( input( "Enter second triangle length: " ) )
width2 = float( input( "Enter second triangle width: " ) )

rect2_area = length2 * width2

if rect1_area > rect2_area:
    print( 'Rectangle 1 Area: ', rect1_area )
    print( 'Rectangle 2 Area: ', rect2_area )
    print( 'Rectangle 1 has a greater area than Rectangle 2.' )
elif rect1_area < rect2_area:
    print( 'Rectangle 1 Area: ', rect1_area )
    print( 'Rectangle 2 Area: ', rect2_area )
    print( 'Rectangle 2 has a greater area than Rectangle 1.' )
else:
    print( "Rectangle 1 and Rectangle 2 have equal areas." )
