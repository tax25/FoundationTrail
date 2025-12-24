import argparse
import sys
import re

from aodoo import __version__

from aodoo.operationHandlers import generate_module_handler as module_helper
from aodoo.operationHandlers import generate_security_handler as security_helper
from aodoo.operationHandlers import generate_model_handler as model_helper
from aodoo.operationHandlers import generate_view_handler as view_helper
from aodoo.operationHandlers.send_help import send_help


# TODO: At module/application generation maybe generate an __init__.py file in wizards?
# TODO: Allow the user to create security groups
# TODO: Allow i18n initialization


def main(cli_params: list):
    if cli_params.generate:
        if not cli_params.name:
            raise Exception('Name not valued!')
        
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', cli_params.name.replace(' ', '_')).lower()

        match cli_params.generate:
            case 'module' | 'm':
                module_helper.handle_generate_module(
                    name,
                    is_application=cli_params.app,
                    dependencies=cli_params.deps
                )

            case 'view' | 'v':
                assert cli_params.view_model, 'Model not valued!'
                view_helper.handle_generate_view(
                    view_name=name,
                    model=cli_params.view_model,
                    inherit_id=cli_params.inherit_id,
                    is_for_wizard=cli_params.wizard
                )

            case 'model' | 'M':
                model_helper.handle_generate_model(name.replace('.py', ''), cli_params.model_type, cli_params.wizard, cli_params.perms)

            case 'security' | 's':
                sec_helper.handle_generate_security(name)

    else:
        send_help()
        sys.exit()


def aodoo_entrypoint():
    parser = argparse.ArgumentParser(
        prog='Aodoo',
        description='A tool for odoo developing',
        epilog='Stay the reading of our swan song and epilogue' # see what i did here?
    )
    
    # NOTE: This needs to be handled in a better way. 
    # It is quite hard to remember how to create something.
    # Maybe it should be a bit more word-y?
    parser.add_argument('-V', '--version', action='store_true')
    parser.add_argument('-g', '--generate', type=str)
    parser.add_argument('-mt', '--model-type', type=str)
    parser.add_argument('-wz', '--wizard', action='store_true')
    parser.add_argument('-ps', '--perms', type=str, help='Specify perm_read,perm_write,perm_create,perm_unlink all with 0 or 1, separated by commas and no spaces.')
    parser.add_argument('-a', '--app', action='store_true')
    parser.add_argument('-n', '--name', type=str) # NOTE: here the name of the module/model/view gets passed
    parser.add_argument('-d', '--deps', type=str, help='Specify all the dependencies as comma-separated-values. No spaces!')
    parser.add_argument('-vm', '--view_model', type=str)
    parser.add_argument('-inid', '--inherit_id', type=str)

    cli_args = parser.parse_args()
    
    if cli_args.version:
        print("Your installed Aodoo version is: ", __version__)
        sys.exit()

    # print(cli_args)
    
    main(cli_args)
    

if __name__ == '__main__': # for testing purposes
    aodoo_entrypoint()
