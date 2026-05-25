import re
import os

# from foundationTrail.operationHandlers.module.utils.ManifestObj import ManifestObj
from foundationTrail.utils.ManifestUtils import Manifest

from foundationTrail.operationHandlers.module.constants import (
    # MISCELLANEOUS
    DEFAULT_VERSION,
    MAIN_INIT_FILE_CONTENTS,
    SECURITY_FILE_CSV_HEADER,

    # INFO
    INFO_GENERATING_APPLICATION,
    INFO_CREATING_MODULE_DIR,
    INFO_CREATING_MODULE_INTERNAL_DIRECTORY_STRUCTURE,
    INFO_CREATING_BOILERPLATE,
    INFO_CREATING_SECURITY_FILE,
    
    # ERRORS
    ERR_MODULE_NAME_NOT_VALUED,
    ERR_MODULE_WITH_SAME_NAME_EXISTS
)

def handle_generate_module(
    name: str,
    app: bool,
    deps: str,
    author: str,
    m_version: str,
    description: str,
    category: str
) -> None:
    assert name, \
            ERR_MODULE_NAME_NOT_VALUED

    module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name.replace(' ', '_')).lower()

    assert not os.path.isdir(module_name), \
            ERR_MODULE_WITH_SAME_NAME_EXISTS.format(module_name=module_name)
    
    logs_resource_type = 'Application' if app else 'Module'

    print(
        INFO_GENERATING_APPLICATION.format(
            resource='Application' if app else 'Module',
            resource_name=module_name
        )
    )

    module_path = os.path.join(os.getcwd(), module_name)
    print(
        INFO_CREATING_MODULE_DIR.format(resource=logs_resource_type)
    )
    os.mkdir(module_path)

    print(
        INFO_CREATING_MODULE_INTERNAL_DIRECTORY_STRUCTURE.format(
            resource=logs_resource_type
        )
    )
    os.mkdir(os.path.join(module_path, 'models'))
    os.mkdir(os.path.join(module_path, 'views'))
    os.mkdir(os.path.join(module_path, 'security'))
    os.mkdir(os.path.join(module_path, 'wizards'))

    print(
        INFO_CREATING_BOILERPLATE
    )

    with open(module_path + '/__init__.py', 'w') as init_file:
        _ = init_file.write(MAIN_INIT_FILE_CONTENTS)
    
    # TODO: implement dependencies checks
    # For every module specified in `depends`, check if it is in the addons folder(s).
    # **BUT** to be able to check this effectively, FoundationTrail has to know the 
    # name(s) of the directories that hold the addons.
    # This can be done by searching for the `odoo.conf` file.
    # Where can this file be?
    # Or maybe, which would probably be better, the user has to specify the configuration file
    # path.
    # This can be done with a flag (there's way too many flags in this project lmao), **or**
    # a configuration file in something like `~/.config/foundationTrail/conf.toml`.
    # This opens a whole new world of possibilities of configuration.
    
    with open(module_path + '/__manifest__.py', 'w') as manifest_file:
        manifest_module_name = module_name.replace('_', ' ').title()
        manifest_obj: Manifest= Manifest(
            name=manifest_module_name,
            version=m_version if m_version else DEFAULT_VERSION,
            depends=deps.split(',') if deps else [],
            author=author if author else os.getlogin(),
            application=app,
            description=description if description else '',
            category=category if category else ''
        )

        _ = manifest_file.write(manifest_obj.fn_manifest_to_pretty_string())

    with open(module_path + '/models/__init__.py', 'w') as models_init:
        _ = models_init.write('') 

    print(INFO_CREATING_SECURITY_FILE)
    
    with open(module_path + f'/security/ir.model.access.csv', 'w') as security_file:
        _ = security_file.write(SECURITY_FILE_CSV_HEADER)
