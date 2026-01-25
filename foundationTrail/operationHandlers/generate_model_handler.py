import os
import re

INIT_FILENAME = '__init__.py'
SECURITY_FILENAME = 'ir.model.access.csv'
DEFAULT_PERMS = {
    'group_id': '',
    'perm_read': 0, 
    'perm_write': 0, 
    'perm_create': 0, 
    'perm_unlink': 0
}

# WARNING: A model can have a `_name` and still a valid `_inherit`. 
MODEL_FILE_CONTENTS = """from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class {model_class}(models.{model_type}):
    {name_or_inherit} = {model_name_or_inherit}
"""

SECURITY_FILE_CONTENTS = "\naccess_{model_name},access_{model_name},model_{model_name},{group_id},{perm_read},{perm_write},{perm_create},{perm_unlink}\n"

# WARNING TODO: This is important
# If an exception is detected, then delete all the files that were created [and, if possible, also delete modifications to existing files *] 
# * => so that means that we write to file only at the very end of the function.

def _check_if_int(value: str) -> bool:
    try:
        int(value)
    except ValueError:
        return False
    else:
        return True


GENERATE_MODEL_PARAMETERS = [
    {
        'property_name': 'name',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify model name'
    },
    {
        'property_name': 'chosen_type',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify model type'
    },
    {
        'property_name': 'is_wizard',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Is this model for a wizard?'
    },
    {
        'property_name': 'inherit',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the model this new model has to inherit from'
    },
    {
        'property_name': 'file_name',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': "Please specify the file name in which you'd like the module to be created"
    },
    {
        'property_name': 'cli_perms',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the permissions for the model to be created'
    },

]

def handle_generate_model(
    name: str,
    chosen_type: str,
    is_wizard: bool,
    inherit: str,
    file_name: str,
    cli_perms: str
):
    
    assert name and name is not None, "Did not pass the model name!"

    model_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name.replace(' ', '_')).lower()
    model_type = re.sub('^(M|m)odels.?', '', chosen_type).capitalize() if chosen_type else 'Model' if not is_wizard else 'TransientModel'
   
    # NOTE: reserved for future use.
    _model_created = False
    _model_added_to_init = False
    _model_added_to_security = False

    perms = {
        'group_id': '',
        'perm_read': '',
        'perm_write': '',
        'perm_create': '',
        'perm_unlink': '',
    }
    
    assert cli_perms, "Perms not valued! Please value the permissions of the model you're about to create!"

    splitted_cli_perms = cli_perms.split(',')
    # NOTE: if `splitted_cli_perms[0]` is an integer, then it's not 
    # a valid value for the group_id field, so the first value
    # is `perm_read`, and the `group_id` is simply left empty.
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
    if 'models' in os.getcwd():
        file_name_and_path = os.getcwd() + f"/{file_name.replace('.py','') if file_name else model_name}.py"
    elif os.path.exists(os.getcwd() + f"/{'models' if not is_wizard else 'wizards'}"):
        file_name_and_path = os.getcwd() + f"/{'models' if not is_wizard else 'wizards'}/{file_name.replace('.py','') if file_name else model_name}.py"
    else:
        print(f"Cannot find /models directory so creating the file in current directory ({os.getcwd()})")
        file_name_and_path = os.getcwd() + f"/{'models' if not is_wizard else 'wizards'}/{file_name.replace('.py','') if file_name else model_name}.py"

    with open(file_name_and_path, 'w') as model_file:
        model_file.write(
            MODEL_FILE_CONTENTS.format(
                model_class=model_name.replace('_', ' ').title().replace(' ', ''),
                model_type=model_type,
                # NOTE: a model can both have `_name` and `_inherit`. How to handle this situation?
                name_or_inherit='_name' if not inherit else '_inherit',
                model_name_or_inherit=f"'{model_name.replace('_', '.')}'",
            )
        )
        print(f"Model created in {file_name_and_path}")
        
    # add file to __init__
    init_file_path = ''
    if f"{'models' if not is_wizard else 'wizards'}" in os.getcwd():
        init_file_path = INIT_FILENAME
    else:
        init_file_path = f"{'models' if not is_wizard else 'wizards'}/{INIT_FILENAME}"

    with open(init_file_path, 'a' if os.path.isfile(init_file_path) else 'w') as init_file:
        init_file.write(f"from . import {file_name.replace('.py', '') if file_name else model_name}\n")

    print(f"Model added to {init_file_path} with 'from . import {file_name.replace('.py','') if file_name else model_name}'.")

    # add model to ir.model.access.csv in security folder
    security_file_path = None
    if 'security' in os.getcwd() and os.path.isfile(SECURITY_FILENAME):
        security_file_path = SECURITY_FILENAME
    elif os.path.isfile(os.getcwd() + f'/security/{SECURITY_FILENAME}'):
        security_file_path = f'security/{SECURITY_FILENAME}'

    if security_file_path:
        with open(security_file_path, 'a') as sec_file:
            sec_file.write(SECURITY_FILE_CONTENTS.format(model_name=model_name, **perms))
            print(f"Model added to {security_file_path} with perms = {perms}") # TODO: allow the user to handle the group too
            
