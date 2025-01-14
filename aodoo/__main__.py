import sys
import re

from aodoo import __version__

from aodoo.operationHandlers import generate_module_handler as module_h
from aodoo.operationHandlers import generate_security_handler as sec_h
from aodoo.operationHandlers import generate_model_handler as model_h
from aodoo.operationHandlers import generate_view_handler as view_h
from aodoo.operationHandlers.send_help import send_help


# @TODO(Allow the user to specify dependencies on module, model and view generation. In case of view generation, even the inherit_id)
# @TODO(At module/application generation maybe generate an __init__.py file in wizards/?)
# @TODO(At view generation allow the user to pass the model for which the view is being created.)
# @TODO(...continues: and maybe in the future allow the user to pass even the inherit_id and other view params)
# @TODO(Allow the user to create security groups)
# @TODO(Handle multiple languages [how?])

def _get_param_from_command_line(index, arguments):
    
    if len(arguments) > index: 
        return arguments[index]

    return False


# view model name
# view inherit_id (module+id)
def handle_generate(what_to_generate: str, name: str, **kwargs):

    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name.replace(' ', '_')).lower()
    
    match what_to_generate:
        case 'application' | 'a':
            module_h.handle_generate_module(name, True)
            
        case 'module' | 'm':
            module_h.handle_generate_module(name, False)
        
        case 'view' | 'v':
            view_h.handle_generate_view(
                view_name=name.replace('.xml', ''), 
                model=kwargs['view_model_name'] if kwargs.get('view_model_name') else None
            )
        
        case 'model' | 'M': 
            model_h.handle_generate_model(name.replace('.py', ''))
        
        case 'security' | 's':
            sec_h.handle_generate_security(name)

        case _:
            send_help()


# def main(given_action: str, given_detail: str, given_name: str, **kwargs):
def main(cli_params: list)

    action = _get_param_from_command_line(1, cli_params)
    detail = _get_param_from_command_line(2, cli_params)
    name = _get_param_from_command_line(3, cli_params)

    
    
    match action:
        case 'generate' | 'g':
            assert detail and name, "Not enough params!" # @todo(handle this without the assert)
            handle_generate(detail, name, **optional_params)
        case _:
            # handle non existent
            print("The action you inserted does not exist! Here's some help:")
            send_help()


def aodoo_entrypoint():
    if len(sys.argv) == 1:
        send_help()
        sys.exit()

    if '--version' in sys.argv or '-v' in sys.argv:
        print("Your installed Aodoo version is: ", __version__)
        sys.exit()

    # this short part of code that is below this comment
    # makes me think that it should be in the main function
    # and that to main() i should just pass sys.argv...
    

    # optional_params = {}
    
    # if action == 'g' and detail == 'v':
    #     if (view_model_name := _get_param_from_command_line(4, sys.argv)):
    #         optional_params['view_model_name'] = view_model_name
    
    main(action, detail, name, **optional_params)
    

if __name__ == '__main__': # for testing purposes
    aodoo_entrypoint()
