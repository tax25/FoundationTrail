import os
import re

from foundationTrail.operationHandlers.model.constants import (
    INIT_FILENAME,
    IMPORT_IN_INIT,
    SECURITY_FILENAME,
    MODEL_FILE_CONTENTS,
    SECURITY_FILE_CONTENTS,
    INFO_MODEL_FILE_CREATED,
    INFO_MODEL_ADDED_TO_INIT,
    INFO_MODEL_ADDED_TO_SECURITY,
    ERR_MODEL_NAME_NOT_VALUED,
    ERR_PERMS_NOT_VALUED,
    ERR_MODELS_DIR_NOT_FOUND,
    ERR_COULD_NOT_FIND_SECURITY_FILE_PATH
)

def _check_if_int(value: str) -> bool:
    try:
        _ = int(value)
    except ValueError:
        return False
    else:
        return True

def handle_generate_model(
    name: str,
    model_type: str,
    wizard: bool,
    inherit: str,
    filename: str,
    m_perms: str
) -> None:
    assert name and name is not None, ERR_MODEL_NAME_NOT_VALUED
    assert m_perms, ERR_PERMS_NOT_VALUED

    # NOTE: turns `name` and `inherit` into 'something_like_this',
    model_name: str = re.sub(
        r'(?<!^)(?=[A-Z])', 
        '_',
        name.replace(' ', '_')
    ).lower()

    adapted_inherit = re.sub(
        r'(?<!^)(?=[A-Z])', 
        '_',
        inherit.replace(' ', '_')
    ).lower() if inherit else ""

    chosen_type = 'Model'
    if model_type:
        chosen_type = re.sub(
            '^(M|m)odels.?',
            '',
            model_type 
        ).capitalize()

    elif wizard:
        chosen_type = 'TransientModel'
    
    # NOTE: for future use
    model_created: bool = False
    model_added_to_init: bool = False
    model_added_to_security: bool = False

    perms = {
        'group_id': '',
        'perm_read': '',
        'perm_write': '',
        'perm_create': '',
        'perm_unlink': '',
    }

    splitted_cli_perms = m_perms.split(',')
    # NOTE: if `splitted_cli_perms[0]` is an integer, then it's not 
    # a valid value for the group_id field, so the first value
    # passed must be `perm_read`, and the `group_id` is simply left empty.
    if _check_if_int(m_perms[0]):
        perms = {
            'group_id': '',
            'perm_read': splitted_cli_perms[0],
            'perm_write': splitted_cli_perms[1],
            'perm_create': splitted_cli_perms[2],
            'perm_unlink': splitted_cli_perms[3],
        }
    else:
        perms = {
            'group_id': splitted_cli_perms[0],
            'perm_read': splitted_cli_perms[1],
            'perm_write': splitted_cli_perms[2],
            'perm_create': splitted_cli_perms[3],
            'perm_unlink': splitted_cli_perms[4],
        }
    
    file_name_and_path = ''
    new_model_dir = 'wizards' if wizard else 'models'
    tmp_filename = (filename if filename else model_name).replace('.py', '')

    if new_model_dir in os.getcwd():
        file_name_and_path = os.getcwd() + f"/{tmp_filename}.py"
    
    elif os.path.exists(os.getcwd() + f"/{new_model_dir}"):
        file_name_and_path = os.getcwd() + f"/{new_model_dir}/{tmp_filename}.py"

    else:
        print(
            ERR_MODELS_DIR_NOT_FOUND.format(
                directory=new_model_dir, 
                current_directory=os.getcwd()
            )
        )
        file_name_and_path = os.getcwd() + f"/{tmp_filename}.py"
    
    with open(file_name_and_path, 'w') as model_file:
        new_class = model_name.replace('_', ' ').title().replace(' ', '')
        name_or_inherit = '_name' if not adapted_inherit else '_inherit'
        model_name_or_inherit_val = \
                f"'{(adapted_inherit if adapted_inherit else model_name).replace('_', '.')}'"

        _ = model_file.write(
            MODEL_FILE_CONTENTS.format(
                model_class=new_class,
                model_type=chosen_type,
                name_or_inherit=name_or_inherit,
                model_name_or_inherit=model_name_or_inherit_val 
            )
        )
        model_created = True
        print(INFO_MODEL_FILE_CREATED.format(filepath=file_name_and_path))

    init_file_path = ''
    if new_model_dir in os.getcwd():
        init_file_path = INIT_FILENAME
    else:
        init_file_path = f"{new_model_dir}/{INIT_FILENAME}"
    
    append_or_write = 'a' if os.path.isfile(init_file_path) else 'w'
    with open(init_file_path, append_or_write) as init_file:
        import_stmt = IMPORT_IN_INIT.format(filename=tmp_filename)
        _ = init_file.write(import_stmt)
        model_added_to_init = True
        print(
            INFO_MODEL_ADDED_TO_INIT.format(
                init_path=init_file_path,
                import_statement=import_stmt.replace('\n', '')
            )
        )
    
    # NOTE: meh... this is strange...
    security_file_path = None
    if 'security' in os.getcwd() and os.path.isfile(SECURITY_FILENAME):
        security_file_path = SECURITY_FILENAME
    elif os.path.isfile(os.getcwd() + f'security/{SECURITY_FILENAME}'):
        security_file_path = f'security/{SECURITY_FILENAME}'

    if not security_file_path:
        print(ERR_COULD_NOT_FIND_SECURITY_FILE_PATH)
        return

    with open(security_file_path, 'a') as sec_file:
        _ = sec_file.write(
            SECURITY_FILE_CONTENTS.format(
                model_name=model_name,
                **perms
            )
        )
        model_added_to_security = True
        print(
            INFO_MODEL_ADDED_TO_SECURITY.format(
                sec_file_path=security_file_path,
                perms_values=perms
            )
        )
