#! /usr/bin/env python3.11
import os
import sys

from operationHandlers import generate_module_handler as module_h
from operationHandlers import generate_model_handler as model_h
from operationHandlers import generate_security_handler as sec_h
from operationHandlers import generate_view_handler as view_h
from operationHandlers.send_help import send_help


def _get_param_from_command_line(index, arguments):
    
    if len(arguments) > index: 
        return arguments[index]

    return False


def handle_non_existent():
    print("The function you inserted does not exist! Here's some help:")
    send_help()


def handle_generate(what_to_generate: str, name: str, is_application: bool):

    match what_to_generate:
        case 'module' | 'm':
            module_h.handle_generate_module(name, is_application)
        
        case 'view' | 'v':
            print("handle generate view")
            view_h.handle_generate_view(name)
        
        case 'model' | 'M': 
            model_h.handle_generate_model(name)
        
        case 'security' | 's':
            sec_h.handle_generate_security(name)


def main(given_action: str, given_detail: str, given_name: str, is_application: bool):
    
    match given_action:
        case 'generate' | 'g':
            handle_generate(given_detail, given_name, is_application)
        case _:
            handle_non_existent()


if __name__ == '__main__':

    if len(sys.argv) == 1:
        send_help()
        exit()

    action = _get_param_from_command_line(1, sys.argv)
    detail = _get_param_from_command_line(2, sys.argv)
    name = _get_param_from_command_line(3, sys.argv)
    is_application = _get_param_from_command_line(4, sys.argv)

    main(action, detail, name, True if is_application in ['true', 'True'] else False)
