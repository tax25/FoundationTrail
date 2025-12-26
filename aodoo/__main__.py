import argparse
import sys
import re

from aodoo import __version__

from aodoo.operationHandlers import generate_module_handler as module_helper
from aodoo.operationHandlers import generate_security_handler as security_helper
from aodoo.operationHandlers import generate_model_handler as model_helper
from aodoo.operationHandlers import generate_view_handler as view_helper
from aodoo.operationHandlers.send_help import send_help

def handle_generate(cli_params: list) -> None:
    if cli_params.module:
        module_helper.handle_generate_module(
            cli_params.name,
            is_application=cli_params.app,
            dependencies=cli_params.deps,
            author=cli_params.author,
            version=cli_params.m_version,
            description=cli_params.description,
            category=cli_params.category
        )

    elif cli_params.model:
        model_helper.handle_generate_model(
            cli_params.name,
            type=cli_params.model_type,
            is_wizard=cli_params.wizard,
            inherit=cli_params.inherit,
            file_name=cli_params.file_name,
            cli_perms=cli_params.m_perms,
        )

    elif cli_params.view:
        view_helper.handle_generate_view(
            cli_params.name,
            model=cli_params.view_model,
            inherit_id=cli_params.inherit_view,
            is_for_wizard=cli_params.wizard_view
        )

    elif cli_params.security:
        security_helper.handle_generate_security()

    else:
        print("What are you trying to generate?")



# def main(cli_params: list):
#     if cli_params.generate:
#         if not cli_params.name:
#             raise Exception('Name not valued!')
        
#         name = re.sub(r'(?<!^)(?=[A-Z])', '_', cli_params.name.replace(' ', '_')).lower()

#         match cli_params.generate:
#             case 'module' | 'm':
#                 module_helper.handle_generate_module(
#                     name,
#                     is_application=cli_params.app,
#                     dependencies=cli_params.deps
#                 )

#             case 'view' | 'v':
#                 assert cli_params.view_model, 'Model not valued!'
#                 view_helper.handle_generate_view(
#                     view_name=name,
#                     model=cli_params.view_model,
#                     inherit_id=cli_params.inherit_id,
#                     is_for_wizard=cli_params.wizard
#                 )

#             case 'model' | 'M':
#                 model_helper.handle_generate_model(name.replace('.py', ''), cli_params.model_type, cli_params.wizard, cli_params.perms)

#             case 'security' | 's':
#                 sec_helper.handle_generate_security(name)

#     else:
#         send_help()
        # sys.exit()


def aodoo_entrypoint():
    parser = argparse.ArgumentParser(
        prog='Aodoo',
        description='A tool for odoo developing',
        epilog='Stay the reading of our swan song and epilogue' # see what i did here?
    )

    # New Parser
    parser.add_argument('-V', '--version', action='store_true')
    parser.add_argument('-g', '--generate', action='store_true')
    
    # NOTE: this arguments are used in multiple categories, 
    # thus reported before every other flag:

    # NOTE: used in - `-m`, `-v`, 
    parser.add_argument('-fn', '--file-name', type=str)
    # NOTE: used in - `-m`, `-M`, `-v`
    parser.add_argument('-n', '--name', type=str)


    parser.add_argument('-M', '--module', action='store_true')
    parser.add_argument('-a', '--app', action='store_true')
    parser.add_argument('-d', '--deps', type=str)
    parser.add_argument('-A', '--author', type=str)
    parser.add_argument('-mv', '--m-version', type=str)
    parser.add_argument('-D', '--description', type=str)
    parser.add_argument('-c', '--category', type=str)

    parser.add_argument('-m', '--model', action='store_true')
    parser.add_argument('-mt', '--model-type', type=str)
    parser.add_argument('-i', '--inherit', type=str)
    parser.add_argument('-wz', '--wizard', action='store_true')
    parser.add_argument('-mp', '--m-perms', type=str)

    parser.add_argument('-v', '--view', action='store_true')
    parser.add_argument('-vm', '--view-model', type=str)
    parser.add_argument('-wv', '--wizard-view', action='store_true')
    parser.add_argument('-iv', '--inherit-view', type=str)

    parser.add_argument('-s', '--security', action='store_true')
    parser.add_argument('-id', type=str)
    parser.add_argument('-mid', '--model-id', type=str)
    parser.add_argument('-gid', '--group-id', type=str)
    parser.add_argument('-pr', '--perm-read', action='store_true')
    parser.add_argument('-pw', '--perm-write', action='store_true')
    parser.add_argument('-pc', '--perm-create', action='store_true')
    parser.add_argument('-pu', '--perm-unlink', action='store_true')


    cli_args = parser.parse_args()
    
    if cli_args.version:
        print("Your installed Aodoo version is: ", __version__)
        sys.exit()

    # print(cli_args)
    
    # main(cli_args)

    if cli_args.generate:
        handle_generate(cli_args)
    

if __name__ == '__main__': # for testing purposes
    aodoo_entrypoint()
