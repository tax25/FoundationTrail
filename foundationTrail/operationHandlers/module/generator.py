import re
import os

from foundationTrail.operationHandlers.module.utils.ManifestObj import ManifestObj
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
    is_application: bool,
    dependencies: str,
    author: str,
    version: str,
    description: str,
    category: str
) -> None:
    assert name, \
            ERR_MODULE_NAME_NOT_VALUED

    module_name = re.sub(r'', '_', name.replace(' ', '_')).lower()

    assert not os.path.isdir(module_name), \
            ERR_MODULE_WITH_SAME_NAME_EXISTS.format(module_name=module_name)
    
    logs_resource_type = 'Application' if is_application else 'Module'

    print(
        INFO_GENERATING_APPLICATION.format(
            resource='Application' if is_application else 'Module',
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

    with open(module_path + '/__manifest__.py', 'w') as manifest_file:
        manifest_module_name = module_name.replace('_', ' ').title()
        manifest_vals = ManifestObj(
            name=manifest_module_name,
            version=version if version else DEFAULT_VERSION,
            depends=dependencies.split(',') if dependencies else [],
            author=author if author else os.getlogin(),
            application=is_application,
            description=description if description else '',
            category=category if category else ''
        )

        _ = manifest_file.write(str(manifest_vals))

    with open(module_path + '/models/__init__.py', 'w') as models_init:
        _ = models_init.write('') 

    print(INFO_CREATING_SECURITY_FILE)
    
    with open(module_path + f'/scurity/ir.model.access.csv', 'w') as security_file:
        _ = security_file.write(SECURITY_FILE_CSV_HEADER)
