import sys

from foundationTrail import (
    __version__ as foundationTrailVersion,
    FOUNDATION_TRAIL_INSTALLED_VERSION
)

from foundationTrail.utils.FTArguments import FTArguments
from foundationTrail.utils.FTConfig import FTConfig

from foundationTrail.operationHandlers.module.generator \
        import handle_generate_module

from foundationTrail.operationHandlers.model.generator \
        import handle_generate_model
from foundationTrail.operationHandlers.model.interactive_config import INTERACTIVE_CONFIG as model_interactive_config

from foundationTrail.operationHandlers.security.generator \
        import handle_generate_security

from foundationTrail.operationHandlers.view.generator \
        import handle_generate_view


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
    
    configuration = FTConfig()
    cli_args = FTArguments(configuration)
    
    if cli_args.version:
        print(
            FOUNDATION_TRAIL_INSTALLED_VERSION.format(
                version=foundationTrailVersion
            )
        )
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
    
    if cli_args.generate:
        if cli_args.module:
            handle_generate_module(**cli_args.fn_get_module_props_in_dict()) # pyright: ignore[reportArgumentType]
        elif cli_args.model:
            cli_args.fn_args_from_interactive(model_interactive_config)
            handle_generate_model(**cli_args.fn_get_model_props_in_dict()) # pyright: ignore[reportArgumentType]
        elif cli_args.view:
            handle_generate_view(**cli_args.fn_get_view_props_in_dict()) # pyright: ignore[reportArgumentType]
        elif cli_args.security:
            handle_generate_security(**cli_args.fn_get_security_props_in_dict()) # pyright: ignore[reportArgumentType]


if __name__ == '__main__':
    foundationTrail_entrypoint()
