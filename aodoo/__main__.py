import sys
import re

from aodoo import __version__

from aodoo.operationHandlers import generate_module_handler as module_helper
from aodoo.operationHandlers import generate_security_handler as security_helper
from aodoo.operationHandlers import generate_model_handler as model_helper
from aodoo.operationHandlers import generate_view_handler as view_helper
from aodoo.operationHandlers.send_help import send_help


# @TODO(Handle cli arguments with argument parser.)
# @TODO(Allow the user to specify dependencies on module, model and view generation. In case of view generation, even the inherit_id)
# @TODO(At module/application generation maybe generate an __init__.py file in wizards/?)
# @TODO(At view generation allow the user to pass the model for which the view is being created.)
# @TODO(...continues: and maybe in the future allow the user to pass even the inherit_id and other view params)
# @TODO(Allow the user to create security groups)
# @TODO(Handle multiple languages [how?])

# def _get_param_from_command_line(index, arguments):
    
#     if len(arguments) > index: 
#         return arguments[index]

#     return False


# view model name
# view inherit_id (module+id)
# def handle_generate(what_to_generate: str, name: str, **kwargs):

#     name = re.sub(r'(?<!^)(?=[A-Z])', '_', name.replace(' ', '_')).lower()
    
#     match what_to_generate:
#         case 'application' | 'a':
#             module_helper.handle_generate_module(name, True)
            
#         case 'module' | 'm':
#             module_helper.handle_generate_module(name, False)
        
#         case 'view' | 'v':
#             view_helper.handle_generate_view(
#                 view_name=name.replace('.xml', ''), 
#                 model=kwargs['view_model_name'] if kwargs.get('view_model_name') else None
#             )
        
#         case 'model' | 'M': 
#             model_helper.handle_generate_model(name.replace('.py', ''))
        
#         case 'security' | 's':
#             sec_helper.handle_generate_security(name)

#         case _:
#             send_help()


def main(cli_params: list)

    # action = _get_param_from_command_line(1, cli_params)
    # detail = _get_param_from_command_line(2, cli_params)
    # name = _get_param_from_command_line(3, cli_params)
    
    if cli_params.generate:
        assert cli_params.name, 'Name not valued!' # @TODO(handle without assert)
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', cli_params.name.replace(' ', '_')).lower()

        match cli_params.generate:
            case 'module' | 'm':
                module_helper.handle_generate_module(name, cli_params.app)

            case 'view' | 'v':
                view_helper.handle_generate_view(
                    view_name=name,
                    model=cli_params.view_model
                )

            case 'model' | 'M':
                model_helper.handle_generate_model(name.replace('.py', ''))

            case 'security' | 's':
                sec_helper.handle_generate_security(name)

    else:
        print('what')


def aodoo_entrypoint():
    parser = argparse.ArgumentParser(
        prog='Aodoo',
        description='A tool for odoo developing',
        epilog='Stay the reading of our swan song and epilogue' # see what i did there?
    )

    parser.add_argument('-V', '--version', action='store_true')
    parser.add_argument('-g', '--generate')
    parser.add_argument('-a', '--app', action='store_true')
    parser.add_argument('-n', '--name', type=str) # NOTE: here the name of the module/model/view gets passed
    parser.add_argument('-vm', '--view_model')

    cli_args = parser.parse_args()

    if cli_args.version:
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
