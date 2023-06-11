# Enter you module contents here
"""Helper functions for triangles."""
 
__author__ = "Mitiku Wubetie"
__version__ = "1.0"
 
import math
 
def hypothenuse(a, b):
    """Computes the length of the hypothenuse of a right-angled triangle
with sides of length a and b."""
    return math.sqrt(a**2 + b**2)
 
def area(a, b):
    """Computes the area of a right-angled triangle
    with sides of length a and b."""
    return a*b/2