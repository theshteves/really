#
# Really Library Generator
#
# Updates can be found at:
#   https://github.com/theshteves/really
#

import argparse
import datetime
import sys


def generate_header(version):
    '''Construct Really module header'''

    return r'''"""Steven Kneiser's Really library

This module is a core library that:

    - provides foundational support
    - 
    - 

This module contains the following public classes:

    - Really: 
    - NotReally: various utilities forgotten in the Python Standard Library

"""

__version__ = "''' + str(version) + r'''"
__all__ = ["Really", "NotReally"]

'''


def number_to_word(num):
    '''Convert number to word'''

    return str(num)


def generate_really():
    '''Construct Really class'''

    header = r'''
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

'''

    return header


def generate_notreally():
    '''Construct NotReally class'''

    return ''


#
# Execute on Script Call
#
if __name__ == '__main__':
    
    # Command-Line Interface
    parser = argparse.ArgumentParser(
            description='The missing package for Python 3')

    VERSION = 0.1

    # Write Module
    module = open('__init__.py', 'w')
    module.write(generate_header(VERSION))
    module.write(generate_really())
    module.write(generate_notreally())
    module.close()

