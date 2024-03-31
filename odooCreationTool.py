#! /usr/bin/env python3.11

import os
import sys

from operationHandlers import generate_module_handler as module_h
from operationHandlers import generate_model_handler as model_h
from operationHandlers import generate_security_handler as sec_h
from operationHandlers import generate_view_handler as view_h
from operationHandlers.send_help import send_help


if len(sys.argv) == 1:
    send_help()
    exit()

action = sys.argv[1]
detail = sys.argv[2] if len(sys.argv) >= 2 else send_help(); exit()
# these two parameters are not mandatory
name = sys.argv[3] if len(sys.argv) >= 4 else ''
is_application = sys.argv[4] if len(sys.argv) >= 5 else '' 


def handle_non_existent():
    print("This function does not exist...")


def handle_generate(what_to_generate: str, name: str, is_application: bool):

    match what_to_generate:
        case 'module' | 'm':
            module_h.handle_generate_module(name, is_application)
        
        case 'view' | 'v':
            view_h.handle_generate_view(name)
        
        case 'model' | 'M': 
            model_h.handle_generate_model(name)
        
        case 'security' | 's':
            sec_h.handle_generate_security(name)


def main(given_action: str, given_detail: str, given_name: str, is_application: bool):

    match action:
        case 'generate' | 'g':
            handle_generate(given_detail, given_name, is_application)
        case _:
            handle_non_existent()


if __name__ == '__main__':
    assert is_application in ['true', 'True', 'false', 'False', ''], "is_application is not a value between 'true', 'True', 'false' and 'False'"
    main(action, detail, name, True if is_application in ['true', 'True'] else False)
