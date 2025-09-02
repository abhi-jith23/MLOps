'''
No need to execute this cell.

This is a python script meant to be run from the terminal.

It uses 'if__name__' construct at the end of the script to hook
into any function. In this case, it connects to the main() function.

The script doesn't do much except report the arguments being passed
into the script. It should serve as the foundation to create a more
powerful script. 
'''

import sys

def main(arguments):
    print("This is the main function, and it has access to the following variables:")
    for argument in arguments:
        print(argument)

if __name__ == '__main__':
    main(sys.argv)