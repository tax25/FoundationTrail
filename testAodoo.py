#! /usr/bin/env python3.11

import sys
import subprocess


TEST_MODULE_NAME = 'my_test_module'
TEST_VIEW_NAME = 'my_test_view'

def _is_number(number_to_test: str):

    try:
        int(number_to_test)
        return True
    except:
        return False


def main(arguments: list):

    if sys.argv[1] == 'undo' and _is_number(sys.argv[2]):
        testCase = int(sys.argv[2]) + 10

    elif _is_number(sys.argv[1]):
        testCase = int(sys.argv[1])
    
    else:
        print("Wrong command line arguments...")
        exit()


    match testCase:
        case 1:
            # whole module generation case
            subprocess.run(['./aodoo.py', 'generate', 'module', TEST_MODULE_NAME, 'True'])

        case 2:
            # new view creation case
            subprocess.run(['./aodoo.py', 'generate', 'view', TEST_VIEW_NAME])

        case 11:
            subprocess.run(['rm', '-rf', TEST_MODULE_NAME])

        case 12:
            print("Undo for view creation not yet implemented")
            exit()

        case _:
            print("Test case not yet implemented...")
            exit()


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print("No values have been passed")
        exit()

    main(sys.argv)