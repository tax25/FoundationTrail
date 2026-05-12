import argparse
import sys

from foundationTrail import (
    __version__ as foundationTrailVersion,
    FOUNDATION_TRAIL_INSTALLED_VERSION
)

from foundationTrail.utils import FTArguments

from foundationTrail.operationHandlers.send_help import (
    send_help,
    explain_module_generation,
    explain_model_generation, 
    explain_view_generation, 
    explain_security_generation
)

def foundationTrail_entrypoint() -> None:
    if len(sys.argv) == 1:
        send_help()
        sys.exit()
    
    parser = argparse.ArgumentParser(
        prog='FoundationTrail',
        description='A tool for Odoo developing',
        epilog='Stay the reading of our swan song and epilogue',
        add_help=False
    )
    
    _ = parser.add_argument_group('Miscellaneous')
    _ = parser.add_argument('--help', action='store_true')
    _ = parser.add_argument('-V', '--version', action='store_true', type=bool)
    _ = parser.add_argument('-I', '--interactive', action='store_true')
    _ = parser.add_argument('-e', '--explain', type=str)

    _ = parser.add_argument_group('Basic Actions')
    _ = parser.add_argument('-g', '--generate', action='store_true')

    _ = parser.add_argument_group('Specifics')
    _ = parser.add_argument_group('Modules')
    _ = parser.add_argument('-M', '--module', action='store_true')
    _ = parser.add_argument('-a', '--app', action='store_true')
    _ = parser.add_argument('-d', '--deps', type=str)
    _ = parser.add_argument('-A', '--author', type=str)
    _ = parser.add_argument('-mv', '--m-version', type=str)
    _ = parser.add_argument('-D', '--description', type=str)
    _ = parser.add_argument('-c', '--category', type=str)

    _ = parser.add_argument_group('Models')
    _ = parser.add_argument('-m', '--model', action='store_true')
    _ = parser.add_argument('-mt', '--model-type', type=str)
    _ = parser.add_argument('-i', '--inherit', type=str)
    _ = parser.add_argument('-wz', '--wizard', action='store_true')
    _ = parser.add_argument('-mp', '--m-perms', type=str)

    _ = parser.add_argument_group('Views')
    _ = parser.add_argument('-v', '--view', action='store_true')
    _ = parser.add_argument('-vm', '--view-model', type=str)
    _ = parser.add_argument('-wv', '--wizard-view', action='store_true')
    _ = parser.add_argument('-iv', '--inherit-view', type=str)
    
    _ = parser.add_argument_group('Security')
    _ = parser.add_argument('-s', '--security', action='store_true')
    _ = parser.add_argument('-id', '--line-id', type=str)
    _ = parser.add_argument('-ln', '--line-name', type=str)
    _ = parser.add_argument('-mid', '--model-id', type=str)
    _ = parser.add_argument('-gid', '--group-id', type=str)
    _ = parser.add_argument('-pr', '--perm-read', action='store_true')
    _ = parser.add_argument('-pw', '--perm-write', action='store_true')
    _ = parser.add_argument('-pc', '--perm-create', action='store_true')
    _ = parser.add_argument('-pu', '--perm-unlink', action='store_true')
    
    cli_args = FTArguments()
    _ = parser.parse_args(namespace=cli_args)
    
    if cli_args.version:
        print(FOUNDATION_TRAIL_INSTALLED_VERSION.format(version=foundationTrailVersion))
        sys.exit()
    
    if cli_args.help:
        send_help()
        sys.exit()
    
    if cli_args.explain:
        if cli_args.explain in ('M', 'module', '-M', '--module'):
            explain_module_generation()
        elif cli_args.explain in ('m', 'model', '-m', '--model'):
            explain_model_generation()
        elif cli_args.explain in ('v', 'view', '-v', '--view'):
            explain_view_generation()
        elif cli_args.explain in ('s', 'security', '-s', '--security'):
            explain_security_generation()


if __name__ == '__main__':
    foundationTrail_entrypoint()
