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

  _______ _______ _______ _______ _______ _______ 
 |\     /|\     /|\     /|\     /|\     /|\     /|
 | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
 | |   | | |   | | |   | | |   | | |   | | |   | |
 | |R  | | |E  | | |A  | | |L  | | |L  | | |Y  | |
 | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
 |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|

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


def generate_really(count):
    '''Construct Really class'''

    class_header = r'''
class Really():
    """Really Class:
    
    To be continued...
    """
'''

    methods = r'''
    def __init__(self, num):
        """Initialize Really instance"""

        self.num = num


    def __str__(self):
        """String representation"""

        return "Really(num=\"" + self.num + "\")"

'''

    # Generate methods
    for n in range(count):

        methods += r'''
    def is_''' + number_to_word(n) + r'''(self):
        """Verify whether num property is ''' + str(n) + r'''"""

        return self.num == ''' + str(n) + r'''

'''

    return class_header + methods


def generate_notreally():
    '''Construct NotReally class'''

    class_header = r'''
class NotReally():
    """NotReally Class:

    To be continued...
    """
'''

    methods = r'''
'''

    return class_header + methods


#
# Execute on Script Call
#
if __name__ == '__main__':

    # Command-Line Interface
    parser = argparse.ArgumentParser(
            description='The missing package for Python 3')
    parser.add_argument('version', metavar='version_number',
            help='Version number for build')
    parser.add_argument('methods', metavar='method_count',
            help='Number of comparison methods')

    args = vars(parser.parse_args())
    VERSION = str(args['version'])
    METHOD_COUNT = int(args['methods'])

    # Write Module
    module = open('__init__.py', 'w')
    module.write(generate_header(VERSION))
    module.write(generate_really(METHOD_COUNT))
    module.write(generate_notreally())
    module.close()

