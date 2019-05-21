# Python code to demonstrate printing
# pattern of numbers

def foo1( n ):
    if n == 2:
        return 1
    else:
        return 3 * foo1( n - 1 )  


'''
Recursive calls, foo1(5)

foo1(5)                == 9 * 3 = 27
    foo1(4)            == 3 * 3 = 9
        foo1(3)        == 3 * 1 = 3
            foo1(2)    == 1
'''

def foo2( n ):
    if n > 0:
        print( n, end='' )
        foo2( n-1 )

'''
Recursive calls, foo2(5)

foo2(5)                  prints 5     
    foo2(4)              prints 4
        foo2(3)          prints 3
            foo2(2)      prints 2
                foo2(1)  prints 1

Output: 54321
'''
        
if __name__ == '__main__':
    print( "foo1:", foo1( 5 ) ) 
