# MISCELLANEOUS

DEFAULT_VERSION = '0.1'

MAIN_INIT_FILE_CONTENTS = (
'from . import models\n' +
'from . import wizards\n' 
)

SECURITY_FILE_CSV_HEADER = (
        'id,'           +
        'name,'         +
        'model_id:id,'  +
        'group_id:id,'  +
        'perm_read,'    +
        'perm_write,'   +
        'perm_create,'  +
        'perm_unlink\n'
    )


# INFO

INFO_GENERATING_APPLICATION = "Generating {resource}: {resource_name}..."

INFO_CREATING_MODULE_DIR = '[1] Creating {resource} directory'

INFO_CREATING_MODULE_INTERNAL_DIRECTORY_STRUCTURE = \
        '[2] Creating {resource} internal directory structure'

INFO_CREATING_BOILERPLATE = (
        '[3] Creating __init__.py,' +
        '__manifest__.py,'          +
        'models/__init__.py'        +
        'and wizards/__init__.py'
    )

INFO_CREATING_SECURITY_FILE = '[4] Creating security/ir.model.access.csv'


# ERRORS

ERR_MODULE_NAME_NOT_VALUED = 'The module name is not valued!'

ERR_MODULE_WITH_SAME_NAME_EXISTS = \
        "A module with the name '{module_name}' already exists!"
