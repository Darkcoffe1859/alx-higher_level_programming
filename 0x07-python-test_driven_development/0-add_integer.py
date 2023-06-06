#!/usr/bin/python3
"""

This module provides a function to perform addition operations on two integers


"""

def add_integer(a, b=98):
    """ Return the sum of two integers or floats as integers


    Args:
        a:  The first argument
        b:  The second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError:  If either of the arguments not an integer or a float
    """

   if ((not isinstance(a, int) and not isinstance(a, float))):
       raise TypeError("a must be integer")
   if ((not isinstance(b, int) and not isinstance(b, float))):
       raise TypeError("b must be integer")
   return (int(a) + int(b))

