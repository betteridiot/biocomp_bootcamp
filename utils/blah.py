#!/usr/bin/env python
""" Compares two ages

Finds the difference of years between an age and a birthdate

Usage: python basic_template.py 9001 12

Args:
    (str): age of the navigator
    (str): age of the driver

Returns:
    (int): difference of age in years

"""
import sys

print('Hello, Me!')
        
def main(navigator_age, driver_age):
    """ Finds the difference between an age and birthdate in years
    
    Args:
        navigator_age (int): age of the navigator
        driver_age (int): age of the driver
    
    Returns:
        Difference in age
    """
    diff = abs(navigator_age - driver_age)
    print(f'Difference of {diff} years')
    return diff
            
    
if __name__ == '__main__':
    n_age = int(sys.argv[1])
    d_age = int(sys.argv[2])
    main(n_age, d_age)