import os

from foundationTrail.operationHandlers.model.constants import (
    INIT_FILENAME,
    SECURITY_FILENAME,
    DEFAULT_PERMS,
    MODEL_FILE_CONTENTS,
    SECURITY_FILE_CONTENTS,
    ERR_MODEL_NAME_NOT_VALUED,
    ERR_PERMS_NOT_VALUED,
    ERR_MODELS_DIR_NOT_FOUND
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
    chosen_type: str,
    is_wizard: bool,
    inherit: str,
    file_name: str,
    cli_perms: str
) -> None:
    assert name and name is not None, ERR_MODEL_NAME_NOT_VALUED
    assert cli_perms, ERR_PERMS_NOT_VALUED

    # NOTE: turns `name` and `inherit` into 'something_like_this'.
    model_name: str = re.sub(
        r'(?<!^)(?=[A-Z])', 
        name.replace(' ', '_')
    ).lower()

    adapted_inherit = re.sub(
        r'(?<!^)(?=[A-Z])', 
        inherit.replace(' ', '_')
    ).lower()

    model_type = 'Model'
    if chosen_type:
        model_type = re.sub(
            '^(M|m)odels.?',
            '',
            chosen_type
        ).capitalize()

    elif is_wizard:
        model_type = 'TransientModel'

    model_created = False
    model_added_to_init = False
    model_added_to_security = False

    perms = {
        'group_id': '',
        'perm_read': '',
        'perm_write': '',
        'perm_create': '',
        'perm_unlink': '',
    }

    splitted_cli_perms = cli_perms.split(',')
    # NOTE: if `splitted_cli_perms[0]` is an integer, then it's not 
    # a valid value for the group_id field, so the first value
    # passed must be `perm_read`, and the `group_id` is simply left empty.
    if _check_if_int(cli_perms[0]):
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
    new_model_dir = 'wizards' if is_wizard else 'models'
    tmp_filename = (file_name if file_name else model_name).replace('.py', '')

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
        name_or_inherit = '_name' if not inherit else '_inherit'

        model_file.write(
            MODEL_FILE_CONTENTS.format(
                model_class=new_class,
                model_type=model_type,
                name_or_inherit=name_or_inherit,
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
        init_file.write(import_stmt)
        model_added_to_init = True
        print(
            INFO_MODEL_ADDED_TO_INIT.format(
                init_path=init_file_path,
                import_statement=import_stmt
            )
        )
    
    # NOTE: meh... this is strange...
    security_file_path = None
    if 'security' in os.getcwd() and os.path.isfile(SECURITY_FILENAME):
        security_file_path = SECURITY_FILENAME
    elif os.path.isfile(os.getcwd() + f'security/{SECURITY_FILENAME}'):
        security_file_path = f'security/{SECURITY_FILENAME}'

    if not security_file_path:
        return

    with open(security_file_path, 'a') as sec_file:
        sec_file.write(
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
