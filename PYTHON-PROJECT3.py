# Daniel Tshibangu
# Program prints buying and selling  of stocks based on Joe's first and second 
# week as well as printing any commissions given to broker 

# list all variables
initial_stock = 0.00
final_stock = 0.00
stock_per_share1 = 0.00
stock_per_share2 = 0.00
commission1 = 0.00
commision2 = 0.00
remaining1 = 0.00
remaining2 = 0.00

# list all constants
SHARES = 2000
BROKER_FEE = 0.03

# caculate information for the first week stock
stock_per_share1 = 40.00
initial_stock = stock_per_share1 * SHARES 
commission1 = initial_stock * BROKER_FEE

# calculate remaining amount of initial stock after commission
remaining1 = initial_stock - commission1

#calculate information for the second week stock
stock_per_share2 = 42.75
final_stock = stock_per_share2 * SHARES
commission2 = final_stock * BROKER_FEE

# calculate remaining amount of initial stock after commission
remaining2 = final_stock - commission2

# print information for second
print( "During the first week: " )
print( "\nJoe paid $", format( stock_per_share1, '.2f' ), "per share." )
print( "The total stock amounts to:$", format( initial_stock, ',.2f') )
print( "Joe paid his broker a commission of $",
       format( commission1, ',.2f' ) + "." )

#print remaining total for first week
print( "Joe gets $", format( remaining1, ',.2f' ) )


# Print information during the second week 
print( "\nDuring the second week: " )
print( "\nJoe sold the stock for $", stock_per_share2, "per share." )
print( "The total stock amounts to:$", format( final_stock, ',.2f') )
print( "Joe paid his broker a commission of $",
       format( commission2, ',.2f' ) + "." )

# Print reamining total for second week
print( "Joe gets $", format( remaining2, ',.2f' ) )






