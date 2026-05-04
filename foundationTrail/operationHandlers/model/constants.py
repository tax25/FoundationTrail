# MISCELLANEOUS

INIT_FILENAME = '__init__.py'

SECURITY_FILENAME = 'ir.model.access.csv'

DEFAULT_PERMS = {
    'group_id': '',
    'perm_read': 0, 
    'perm_write': 0, 
    'perm_create': 0, 
    'perm_unlink': 0
}

MODEL_FILE_CONTENTS = """
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class {model_class}(models.{model_type}):
    {name_or_inherit} = {model_name_or_inherit}
"""

SECURITY_FILE_CONTENTS = '\naccess_{model_name},access_{model_name},model_{model_name},{group_id},{perm_read},{perm_write},{perm_create},{perm_unlink}\n'

IMPORT_IN_INIT = 'from . import {filename}\n'

# INFO
INFO_MODEL_FILE_CREATED = 'Model file created in {filepath}.'

INFO_MODEL_ADDED_TO_INIT = "Model added to {init_path} with '{import_statement}'."

INFO_MODEL_ADDED_TO_SECURITY = "Model added to {sec_file_path} with perms = {perms_values}."

# ERRORS

ERR_MODEL_NAME_NOT_VALUED = 'Model name not valued!'

ERR_PERMS_NOT_VALUED = "Perms not valued! Please attribute a value to the permissions of the model you're about to create!"

ERR_MODELS_DIR_NOT_FOUND = "Cannot find /{directory} directory, so creating the file in the current directory ({current_directory})."
