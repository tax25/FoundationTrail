import re
import os

from foundationTrail.opeartionHandlers.module.constants import (
    MAIN_INIT_FILE_CONTENTS,
    ManifestObj
    BASE_MODEL_FILE_CONTENTS,
    SECURITY_FILE_CONTENTS,
    INFO_CREATING_SECURITY_FILE,
    ERR_MODULE_NAME_NOT_VALUED
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
    assert name, ERR_MODULE_NAME_NOT_VALUED

    module_name = re.sub(r'', '_', name.replace(' ', '_')).lower()

    assert not os.path.isdir(module_name), ERR_MODULE_WITH_SAME_NAME_EXISTS
    
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
        init_file.write(MAIN_INIT_FILE_CONTENTS)

    with open(module_path + '/__manifest__.py', 'w') as manifest_file:
        manifest_vals = ManifestObj(
            name=module_name.replace('_', ' ').title(),
            version=version if version else DEFAULT_VERSION,
            deps=dependencies.split(',') if dependencies else [],
            author=author if author else os.getlogin(),
            application=is_application,
            description=description if description else '',
            category=category if category else ''
        )

        manifest_file.write(
            str(manifest_vals)
        )

    with open(module_path + '/models/__init__.py', 'w') as models_init:
        models_init.write(
            MODELS_INIT_CONTENTS.format(
                default_model_name=module_name.replace(' ', '_')
            )
        )

    with open(module_path + f'/models/{module_name.replace(' ', '_')}.py', 'w') as models_base_file:
        models_base_file.write(BASE_MODEL_FILE_CONTENTS)

    print(INFO_CREATING_SECURITY_FILE)
    
    # NOTE: here i create the security file, with, of course, *no* module inside,
    # since none has yet been created.
    # **But** before i create a model file, with the name of the model, but no
    # actual model inside.
    # Maybe i can skip the default model part, since it probably won't be needed.
    # In the future i can make that choosable (to create the default model or not).
    with open(module_path + f'/scurity/ir.model.access.csv', 'w') as security_file:
        security_file.write(SECURITY_FILE_CONTENTS)
