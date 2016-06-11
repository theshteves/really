"""Steven Kneiser's Really library

This module is a core library that:

    - provides foundational support
    - 
    - 

This module contains the following public classes:

    - Really: 
    - NotReally: various utilities forgotten in the Python Standard Library

"""

__version__ = "0.1"
__all__ = ["Really", "NotReally"]


class Really():
    """Really Class:
    
    To be continued...
    """

    def __init__(self, num):
        """Initialize Really instance"""

        self.num = str(num)


    def __str__(self):
        """String representation"""
        
        return "Really(num='" + self.num + "')"

