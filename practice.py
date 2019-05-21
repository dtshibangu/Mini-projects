# Program 1
#Daniel Tshibangu
#Obj: Design program that calculates purchase including tax.

# prompt for price, store in var purchase 
purchase = float( input( "Enter the price of the item: $" ) )

# initialize state tax, print result
state_tax = purchase * 0.05
print( "The state sales tax for this item is:$", format( state_tax, '.2f' ) )

# initialize country tax, print result 
country_tax = purchase * 0.025
print( "The country sales tax for this item is:$", format( country_tax, '.2f' ) )

# add both taxes, store result in total_tax, then print
total_tax = state_tax + country_tax
print( "The total tax is:$", format( total_tax, '$.2f' ) )

#add purchase and tax for total amount, then print
total = purchase + total_tax
print( "\nThe total price is", format( total, '.2f' ) )

