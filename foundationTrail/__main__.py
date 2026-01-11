import argparse
import sys
import re

from foundationTrail import __version__

from foundationTrail.operationHandlers import generate_module_handler as module_helper
from foundationTrail.operationHandlers import generate_security_handler as security_helper
from foundationTrail.operationHandlers import generate_model_handler as model_helper
from foundationTrail.operationHandlers import generate_view_handler as view_helper
from foundationTrail.operationHandlers import send_help

HANDLE_GENERATE_ERROR_STRING = """
HANDLE_GENERATE_ERROR: What are you trying to generate?
Available options are:
    1. module (-M, --odule)
    2. model (-m, --model)
    3. view (-v, --view)
    4. security (-s, --security)
"""

def handle_generate(cli_params) -> None:
    if cli_params.module:
        module_helper.handle_generate_module(
            name=cli_params.name,
            is_application=cli_params.app,
            dependencies=cli_params.deps,
            author=cli_params.author,
            version=cli_params.m_version,
            description=cli_params.description,
            category=cli_params.category
        )

    elif cli_params.model:
        model_helper.handle_generate_model(
            name=cli_params.name,
            chosen_type=cli_params.model_type,
            is_wizard=cli_params.wizard,
            inherit=cli_params.inherit,
            file_name=cli_params.file_name,
            cli_perms=cli_params.m_perms,
        )

    elif cli_params.view:
        view_helper.handle_generate_view(
            view_name=cli_params.name,
            model=cli_params.view_model,
            inherit_id=cli_params.inherit_view,
            is_for_wizard=cli_params.wizard_view
        )

    elif cli_params.security:
        security_helper.handle_generate_security(
            security_file_name=cli_params.file_name,
            line_id=cli_params.line_id,
            line_name=cli_params.line_name,
            model_id=cli_params.model_id,
            group_id=cli_params.group_id,
            perm_read=cli_params.perm_read,
            perm_write=cli_params.perm_write,
            perm_create=cli_params.perm_create,
            perm_unlink=cli_params.perm_unlink
        )

    else:
        print(HANDLE_GENERATE_ERROR_STRING)


def foundationTrail_entrypoint():
    if len(sys.argv) == 1:
        send_help.send_help()
        sys.exit()

    parser = argparse.ArgumentParser(
        prog='FoundationTrail',
        description='A tool for odoo developing',
        epilog='Stay the reading of our swan song and epilogue', # see what i did here? :D
        add_help=False
    )

    parser.add_argument('-h', '--help', action='store_true')
    
    parser.add_argument('-e', '--explain', type=str)

    parser.add_argument('-V', '--version', action='store_true')
    parser.add_argument('-g', '--generate', action='store_true')
    
    # NOTE: these arguments are used in multiple categories, 
    # thus reported before every other flag:

    # NOTE: used in - `-m`, `-v`, `-s` 
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
    parser.add_argument('-id', '--line-id', type=str)
    parser.add_argument('-ln', '--line-name', type=str)
    parser.add_argument('-mid', '--model-id', type=str)
    parser.add_argument('-gid', '--group-id', type=str)
    parser.add_argument('-pr', '--perm-read', action='store_true')
    parser.add_argument('-pw', '--perm-write', action='store_true')
    parser.add_argument('-pc', '--perm-create', action='store_true')
    parser.add_argument('-pu', '--perm-unlink', action='store_true')

    cli_args = parser.parse_args()

    if cli_args.version:
        print("Your installed FoundationTrail version is: ", __version__)
        sys.exit()

    if cli_args.help:
        send_help.send_help()
        sys.exit()

    if cli_args.explain:
        if cli_args.explain in ('M', 'module', '-M', '--module'):
            send_help.explain_module_generation()
        elif cli_args.explain in ('m', 'model', '-m', '--model'):
            send_help.explain_model_generation()
        elif cli_args.explain in ('v', 'view', '-v', '--view'):
            send_help.explain_view_generation()
        elif cli_args.explain in ('s', 'security', '-s', '--security'):
            send_help.explain_security_generation()

        sys.exit()

    if cli_args.generate:
        handle_generate(cli_args)
    

if __name__ == '__main__':
    foundationTrail_entrypoint()
