#! /usr/bin/env python3.11

import sys
import subprocess


def main(arguments: list):

    if sys.argv[1] == 'undo':
        testCase = int(sys.argv[2]) + 10

    elif isinstance(sys.argv[1], int):
        testCase = sys.argv[1]
    
    else:
        print("Wrong command line arguments...")
        exit()

    match testCase:
        case 1:
            # generation case
            subprocess.run(['./aodoo.py', 'generate', 'module', 'my_test_module', 'True'])

        case 11:
            subprocess.run(['rm', '-rf', 'my_test_module'])

        case _:
            print("Test case not yet implemented...")
            exit()


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print("No values have been passed")
        exit()

    main(sys.argv)