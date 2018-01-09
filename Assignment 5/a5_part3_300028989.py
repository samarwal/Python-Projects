#Name: Samarth Agarwal
#Student number:  300028989
#Course: IT1 1120 
#Assignment Number 5, Part 3


def digit_sum(n):
    ''' (number)->number
    calculates the sum of all digits in n
    Precondition: n is an non-negative integer
    '''
    if n == 0:
        return 0
    else:
        return (n % 10) + digit_sum(n // 10)
    



def digital_root(n):
    ''' (number)->number
    calculates the digital root of n
    Precondition: n is an integer
    '''
    if n < 10:
        return n
    else:
        return digital_root(digit_sum(n))


    
    
    
