# program calculates kinetic energy of object 

# define variables
mass = 0.0
velocity = 0.0
k_energy = 0.0

# main function will prompt for
# mass and velocity, call the kinetic_energy
# function and display the kinetic energy
def main():
    mass = float( input( "Enter mass in kilograms: " ) )
    velocity = float( input( "Enter velocity in m/s: " ) )

    kinetic_energy( mass, velocity )

    print( "The kinetic energy of this object is:" ) 
    print( format( kinetic_energy( mass, velocity ), ',.3f' ) )

# kinetic_energy func calculates
# kinetic energy from mass and velocity
def kinetic_energy( mass, velocity ):
    k_energy = 0.5 * mass * ( velocity ** 2 )
    return k_energy

# calls main function
main()
    

    
